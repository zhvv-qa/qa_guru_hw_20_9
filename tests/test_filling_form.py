from demoqa_pages.data.users import User
from demoqa_pages.pages.registration_form import RegistrationPage


def test_registration_form(open_browser_chrome):

    registration_form = RegistrationPage()

    user = User(
        first_name='Vika',
        last_name='Zhuchkova',
        email='vika.zh@gmail.com',
        gender='Female',
        phone_number='9881112345',
        year='1994',
        month='October',
        day='01',
        subjects='English',
        hobbies='Sports',
        picture='testpion.jpeg',
        address='Test address 789',
        state='Uttar Pradesh',
        city='Agra'
    )

    #Заполнение формы
    registration_form.fill_user_registration_form(user)

    # Проверка данных в таблице
    registration_form.check_registered_user(user)