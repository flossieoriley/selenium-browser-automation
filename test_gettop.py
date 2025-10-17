from encodings.punycode import selective_find

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import pytest

class TestGettop:
    browser = None

    def setup_method(self):
        # Install and start browser
        driver_path = ChromeDriverManager().install()
        self.browser = webdriver.Chrome(service=Service(driver_path))

    @pytest.mark.parametrize('link_text, expected_breadcrumb', [
        ('Laptops', 'HOME / LAPTOP'),
        ('Tablets', 'HOME / TABLET'),
        ('Phones', 'HOME / SMARTPHONE'),
        ('Accessories', 'HOME / ACCESSORIES')
    ])
    def test_header_links(self, link_text, expected_breadcrumb):
        self.browser.get('https://gettop.us/')
        self.browser.find_element(By.XPATH, f"//a[text()='{link_text}' and @class='nav-top-link']").click()

        actual_result = self.browser.find_element(By.XPATH, "//nav[contains(@class, 'breadcrumbs')]").text

        assert actual_result == expected_breadcrumb, f'Error! Actual {actual_result} did not match expected {expected_breadcrumb}'
        print(f'{link_text} test passed')

    @pytest.mark.parametrize('category',['laptop','tablet','accessories'])
    def test_add_to_cart(self, category):
        # Click and open first product
        self.browser.get(f'https://gettop.us/product-category/{category}/')
        self.browser.find_element(By.XPATH, "//p[@class='name product-title']").click()
        # Store product name and add to cart
        product_name = self.browser.find_element(By.XPATH, "//h1[contains(@class, 'product-title')]").text
        self.browser.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
        # Verify
        self.browser.get('https://gettop.us/cart/')
        cart_product_name = self.browser.find_element(By.XPATH, "//td[@class='product-name']//a").text
        assert cart_product_name == product_name

    def teardown_method(self):
        self.browser.quit()
