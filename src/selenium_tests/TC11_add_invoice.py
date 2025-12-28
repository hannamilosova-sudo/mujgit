from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

INVOICES_URL = "http://localhost:3000"

invoice_number = "12345"
expected_price = "1000"  # pokud se v tabulce zobrazuje třeba "1000.00", změň na "1000.00"


def open_invoices(driver):
    driver.get(f"{INVOICES_URL}/invoices")


def click_new_invoice(driver):
    # čekáme na zelené tlačítko "Nová faktura"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-success"))
    ).click()


def fill_invoice_form(driver, invoice_number, expected_price):
    # Číslo faktury (u tebe má výchozí hodnotu 0 -> MUSÍME smazat)
    el = driver.find_element(By.NAME, "invoiceNumber")
    el.clear()
    el.send_keys(invoice_number)

    # Dodavatel
    seller_select = Select(driver.find_element(By.NAME, "seller"))
    WebDriverWait(driver, 10).until(lambda d: len(seller_select.options) > 1)
    seller_select.select_by_index(1)

    # Odběratel
    buyer_select = Select(driver.find_element(By.NAME, "buyer"))
    WebDriverWait(driver, 10).until(lambda d: len(buyer_select.options) > 1)
    # v lekci bývá 2 – když máš jen 2 možnosti, dej 1
    buyer_select.select_by_index(2 if len(buyer_select.options) > 2 else 1)

    # Data
    el = driver.find_element(By.NAME, "issued")
    el.clear()
    el.send_keys("01012020")

    el = driver.find_element(By.NAME, "dueDate")
    el.clear()
    el.send_keys("01022020")

    # Popis / produkt
    el = driver.find_element(By.NAME, "product")
    el.clear()
    el.send_keys("Testovací produkt")

    # Cena (u tebe je default 0 -> clear!)
    el = driver.find_element(By.NAME, "price")
    el.clear()
    el.send_keys(expected_price)

    # DPH (u tebe je default 0 -> clear!)
    el = driver.find_element(By.NAME, "dph")
    el.clear()
    el.send_keys("21")

    # Poznámka
    el = driver.find_element(By.NAME, "note")
    el.clear()
    el.send_keys("Poznámka k faktuře")

    # Uložit (modré tlačítko)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
    ).click()


def verify_invoice_in_list(driver, invoice_number, expected_price):
    open_invoices(driver)

    # najdi řádek podle čísla faktury
    try:
        invoice_row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//tr[td[normalize-space()='{invoice_number}']]")
            )
        )
    except TimeoutException:
        assert False, f"Test selhal: Faktura s číslem {invoice_number} nebyla nalezena!"

    # cena je v předposledním sloupci
    price_element = invoice_row.find_element(By.XPATH, ".//td[position()=last()-1]")
    actual_price = price_element.text.strip()

    assert actual_price == expected_price, (
        f"Test selhal: Faktura nemá správnou cenu! "
        f"Očekáváno: {expected_price}, nalezeno: {actual_price}"
    )


def delete_invoice(driver, invoice_number):
    open_invoices(driver)

    try:
        invoice_row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//tr[td[normalize-space()='{invoice_number}']]")
            )
        )

        delete_button = invoice_row.find_element(
            By.XPATH, ".//button[contains(text(),'Odstranit')]"
        )
        delete_button.click()

    except TimeoutException:
        # když už tam faktura není, nevadí
        pass
    except Exception:
        # úklid nesmí shodit celý běh
        pass


# ====== SPUŠTĚNÍ TESTU ======
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get(INVOICES_URL)
    driver.maximize_window()

    open_invoices(driver)
    click_new_invoice(driver)
    fill_invoice_form(driver, invoice_number, expected_price)
    verify_invoice_in_list(driver, invoice_number, expected_price)

    print("TC11 PROŠLO")

finally:
    delete_invoice(driver, invoice_number)
    driver.quit()
