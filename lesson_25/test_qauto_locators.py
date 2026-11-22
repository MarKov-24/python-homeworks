import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://guest:welcome2qauto@qauto2.forstudy.space/"

XPATH_LOCATORS = {
    "xpath_01_header": "//header[@class='header bg-basic-dark']",
    "xpath_02_logo_href": "//a[@href='/']",
    "xpath_03_about_scroll_attr": "//button[@appscrollto='aboutSection']",
    "xpath_04_contacts_scroll_attr": "//button[@appscrollto='contactsSection']",
    "xpath_05_youtube_iframe": "//iframe[contains(@src, 'youtube.com/embed/')]",
    "xpath_06_info1_img": "//img[contains(@src, 'info_1.jpg')]",
    "xpath_07_about_id": "//div[@id='aboutSection']",
    "xpath_08_contacts_id": "//div[@id='contactsSection']",
    "xpath_09_text_home": "//a[text()='Home']",
    "xpath_10_text_about": "//button[text()='About']",
    "xpath_11_text_contacts": "//button[text()='Contacts']",
    "xpath_12_text_guest_login": "//button[text()='Guest log in']",
    "xpath_13_text_sign_in": "//button[text()='Sign In']",
    "xpath_14_text_sign_up": "//button[text()='Sign up']",
    "xpath_15_text_h1": "//h1[text()='Do more!']",
    "xpath_16_text_fuel_title": "//p[text()='Log fuel expenses']",
    "xpath_17_text_manuals_title": "//p[text()='Instructions and manuals']",
    "xpath_18_text_site_link": "//a[text()='ithillel.ua']",
    "xpath_19_text_email_link": "//a[text()='support@ithillel.ua']",
    "xpath_20_contains_text_footer": "//p[contains(text(), 'Hillel IT school')]",
    "xpath_21_header_nav_home": "//header//nav[@class='header_nav d-flex align-items-center']//a[text()='Home']",
    "xpath_22_header_right_signin": "//div[@class='header_right d-flex align-items-center']//button[text()='Sign In']",
    "xpath_23_hero_signup": "//div[@class='hero-descriptor']//button[text()='Sign up']",
    "xpath_24_contacts_socials": "//div[@id='contactsSection']//div[contains(@class, 'socials')]//a[@href]",
    "xpath_25_footer_last_p": "//footer[@class='footer d-flex align-items-center']//div[contains(@class, '-left')]//p[last()]",
}

CSS_LOCATORS = {
    "css_01_header": "header.header.bg-basic-dark",
    "css_02_logo_href": "a.header_logo[href='/']",
    "css_03_about_scroll_attr": "button[appscrollto='aboutSection']",
    "css_04_contacts_scroll_attr": "button[appscrollto='contactsSection']",
    "css_05_guest_btn": "button.header-link.-guest",
    "css_06_signin_btn": "button.btn.btn-outline-white.header_signin",
    "css_07_hero_h1": "h1.hero-descriptor_title.display-2",
    "css_08_hero_signup_btn": "button.hero-descriptor_btn.btn.btn-primary",
    "css_09_hero_iframe": "iframe.hero-video_frame[src*='youtube.com/embed/']",
    "css_10_about_img_alt": "#aboutSection img[alt='Instructions']",
    "css_11_mailto_link": "#contactsSection a[href^='mailto:']",
    "css_12_blank_socials": "a.socials_link[target='_blank']",
    "css_13_active_nav_link": "header .header_left nav.header_nav a.header-link.-active",
    "css_14_adjacent_signin_btn": "header .header_right button + button",
    "css_15_direct_child_h1": ".hero .hero-descriptor > h1",
    "css_16_about_titles": "#aboutSection .about-block p.about-block_title",
    "css_17_adjacent_descr": "#aboutSection .about-block p.about-block_title + p.about-block_descr",
    "css_18_first_about_title": "#aboutSection .row > div:first-child .about-block_title",
    "css_19_last_about_title": "#aboutSection .row > div:last-child .about-block_title",
    "css_20_first_social": "#contactsSection .contacts_socials a.socials_link:first-child",
    "css_21_last_social": "#contactsSection .contacts_socials a.socials_link:last-child",
    "css_22_second_social": "#contactsSection .contacts_socials a.socials_link:nth-child(2)",
    "css_23_ithillel_link": "#contactsSection a[href='https://ithillel.ua']",
    "css_24_footer_first_p": "footer.footer .footer_item.-left > p:first-child",
    "css_25_footer_logo_svg": "footer.footer .footer_item.-right a.footer_logo > svg",
}


@pytest.fixture(scope="module")
def logged_in_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "app-root"))
    )
    yield driver
    driver.quit()


@pytest.mark.parametrize("name,xpath", XPATH_LOCATORS.items(), ids=XPATH_LOCATORS.keys())
def test_xpath_locators(logged_in_driver, name, xpath):
    elements = logged_in_driver.find_elements(By.XPATH, xpath)
    assert len(elements) > 0, f"XPath '{name}' не знайшов жодного елемента: {xpath}"


@pytest.mark.parametrize("name,css", CSS_LOCATORS.items(), ids=CSS_LOCATORS.keys())
def test_css_locators(logged_in_driver, name, css):
    elements = logged_in_driver.find_elements(By.CSS_SELECTOR, css)
    assert len(elements) > 0, f"CSS '{name}' не знайшов жодного елемента: {css}"