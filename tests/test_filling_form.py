from demoqa_pages.registration_form import RegistrationPage
from selene import browser

def test_registration_form(open_browser_chrome):

    registration_form = RegistrationPage()

    registration_form.fill_first_name('Vika')
    registration_form.fill_last_name('Zhuchkova')
    registration_form.fill_user_email('vika.zh@gmail.com')
    registration_form.fill_gender('Female')
    registration_form.fill_user_number('9881112345')
    registration_form.fill_date_of_birth("1994", "October", "1")
    registration_form.fill_subjects('English')
    registration_form.fill_hobbies('Sports')
    registration_form.fill_picture('testpion.jpeg')
    registration_form.fill_current_address('Test address 789')
    registration_form.fill_state('Uttar Pradesh')
    registration_form.fill_city('Agra')
    registration_form.submit()

    registration_form.check_registered_user('Vika Zhuchkova', 'vika.zh@gmail.com', 'Female', '9881112345', '01 October,1994',
                                    'English', 'Sports', 'testpion.jpeg', 'Test address 789',
                                    'Uttar Pradesh Agra')

