from selene import browser, by, have, be, Element

from qaguru.user import User


class SimpleRegistrationForm:
    def __init__(self):
        self._div_output: Element = browser.element(by.id('output'))

    def register_user(self, user):
        browser.element(by.id('userName')).type(user.full_name)
        browser.element(by.id('userEmail')).type(user.email)
        browser.element(by.id('currentAddress')).type(user.current_address)
        browser.element(by.id('permanentAddress')).type(user.permanent_address)
        browser.element(by.id('submit')).click()

    def check_submitted_data(self, user: User) -> None:
        self._div_output.element(by.id('name')).should(have.text(user.full_name))
        self._div_output.element(by.id('email')).should(have.text(user.email))
        self._div_output.element(by.id('currentAddress')).should(have.text(user.current_address))
        self._div_output.element(by.id('permanentAddress')).should(have.text(user.permanent_address))
