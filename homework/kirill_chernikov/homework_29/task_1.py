from playwright.sync_api import Page, expect, BrowserContext


def test_alert(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role(role='link', name='Click').click()
    page.on('dialog', lambda alert: alert.accept())
    text = page.get_by_text('You selected')
    expect(text).to_be_visible()


def test_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    link = page.locator('#new-page-button')
    with context.expect_page() as new_page:
        link.click()

    new_page = new_page.value

    new_text = new_page.locator('#result-text')
    expect(new_text).to_have_text('I am a new page in a new tab')


def test_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('#colorChange')

    expect(button).to_have_css(name='color', value='rgb(220, 53, 69)', timeout=6000)
