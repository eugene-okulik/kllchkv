from playwright.sync_api import Page, expect


def test_find_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com')
    page.get_by_role(role='link', name='Form Authentication').click()
    page.get_by_role(role='textbox', name='username').fill('Kirill')
    page.get_by_role(role='textbox', name='password').fill('test_pwd')
    page.get_by_role(role='button').click()


def test_fill_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')

    page.locator('#firstName').fill('Kirill')
    page.locator('#lastName').fill('Chernikov')
    page.locator('#userEmail').fill('test_email@gmail.com')
    page.locator('[value="Male"]').check()
    page.locator('#userNumber').fill('75023313636')

    page.locator('#dateOfBirthInput').click()
    page.locator('.react-datepicker__year-select').select_option(value='2002')
    page.locator('.react-datepicker__month-select').select_option(value='8')
    page.locator('.react-datepicker__day--017').click()

    page.locator('#subjectsInput').fill('M')
    first_subject = page.locator('#react-select-2-option-0')
    expect(first_subject).to_have_text('Maths')
    first_subject.click()

    page.locator('#hobbies-checkbox-1').check()

    page.get_by_placeholder('Current Address').fill('Testov street, Russia')

    page.locator('#state').click()
    page.locator('#react-select-3-option-0').click()

    page.locator('#react-select-4-input').click()
    city_options = page.locator('[role="option"]').all()
    city_options[2].click()

    page.locator('#submit').click()

    after_submit_header = page.locator('.h4')
    expect(after_submit_header).to_have_text('Thanks for submitting the form')
