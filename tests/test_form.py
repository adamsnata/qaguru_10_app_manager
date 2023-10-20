from qaguru.application import app
from qaguru.user import User


# * добавить в проект тест на упрощенную регистрацию через форму https://demoqa.com/text-box  и соответствующий PageObject.
#
#   * Реализовать шаблон ApplicationManager для предсоздания всех объектов для пейдж-обджектов.
#
#   * в тесте загрузить форму не через simple_registration_form.open(), а через app.left_panel.open_simple_registration_form(),
# который должен быть шорткатом (методом, вызывающим под капотом другой метод этого же объекта) на app.left_panel.open('Elements', 'Text Box')
#
#     * cоответственно добавить пейджобджект для LeftPanel и создать его объект в виде поля обьекта апликейшен-менеджера


def test_registration_form():
    user = User(
        full_name='тест тестович',
        email='test@test.ts',
        current_address='current address 1',
        permanent_address='permanent address 2',
    )

    app.open()
    app.left_panel.open_simple_registration_form()
    app.simple_registration_form.register_user(user)
    app.simple_registration_form.check_submitted_data(user)

