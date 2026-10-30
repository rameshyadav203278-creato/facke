from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("http://localhost:8081/")
    page.wait_for_timeout(1000)
    page.locator("//input[@name='user_name']").fill("admin")
    page.wait_for_timeout(1000)
    page.locator("//input[@name='user_password']").fill("expertview")
    page.wait_for_timeout(1000)
    page.locator("#submitButton").click()
    page.wait_for_timeout(1000)
    str=page.url
    expect(page).to_have_url("http://localhost:8081/index.php?action=index&module=Home")
    page.wait_for_timeout(1000)
    str=page.locator("//a[contains(normalize-space(text()),'Home')]").inner_text()
    page.wait_for_timeout(1000)
    print(str)
    sau=page.locator("//b[contains(normalize-space(text()),'Top Trouble Tickets')]")
    page.wait_for_timeout(2000)
    tar=page.locator("//b[contains(normalize-space(text()),'Pending Activities')]")
    page.wait_for_timeout(2000)
    sau.drag_to(tar)
   
    print("Hello")
   
