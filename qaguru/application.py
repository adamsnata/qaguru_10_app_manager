from selene import browser

from qaguru.components.left_panel import LeftPanel
from qaguru.components.simple_registration_form import SimpleRegistrationForm


class Application:
    def __init__(self):
        self.left_panel: LeftPanel = LeftPanel()
        self.simple_registration_form: SimpleRegistrationForm = SimpleRegistrationForm()

    def open(self):
        browser.open('/')


app = Application()
