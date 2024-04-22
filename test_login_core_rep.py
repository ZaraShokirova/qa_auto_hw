from selene import browser, have

browser.config.timeout = 2


def open_login_form():
    browser.open('https://testcore-reports.alif.tj/')
    browser.element('[class="pf-c-form-control"]').click()


def test_valid_login():
    open_login_form()

    browser.element('#username').type('zarina.shokirova@alif.tj')
    browser.element('#password').type('Z@r@mir13')
    browser.element('.pf-c-button').click()

    browser.element('.MuiPaper-elevation4 .MuiTypography-root').should(have.exact_text('Core Reports'))


def test_logout():
    ...