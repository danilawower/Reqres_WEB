from pages.reqres_main_page import MainPage
import allure


@allure.suite('Главная страница')
class TestMainPage:

    @allure.title('GET LIST USERS. Проверка статус кода')
    def test_get_list_code(self, driver):
        main_page = MainPage(driver, 'https://reqres.in/')
        main_page.open()
        web_code, api_code = main_page.get_list_users_code()
        assert web_code == api_code

    @allure.title('GET LIST USERS. Проверка тела ответа')
    def test_get_list_body(self, driver):
        main_page = MainPage(driver, 'https://reqres.in/')
        main_page.open()
        web_body, api_body = main_page.get_list_users_body()
        assert web_body == api_body

    @allure.title('GET SINGLE USER. Проверка статус кода')
    def test_get_single_code(self, driver):
        main_page = MainPage(driver, 'https://reqres.in/')
        main_page.open()
        web_code, api_code = main_page.get_single_user_code()
        assert web_code == api_code

    @allure.title('GET SINGLE USER. Проверка тела ответа')
    def test_get_single_body(self, driver):
        main_page = MainPage(driver, 'https://reqres.in/')
        main_page.open()
        web_body, api_body = main_page.get_single_user_body()
        assert web_body == api_body


    @allure.title('GET SINGLE USER NOT FOUND. Проверка статус кода')
    def test_get_user_notfound_code(self, driver):
        main_page = MainPage(driver, 'https://reqres.in/')
        main_page.open()
        web_code, api_code = main_page.get_single_user_notfound_code()
        assert web_code == api_code


    @allure.title('GET SINGLE USER NOT FOUND. Проверка тела ответа')
    def test_get_user_notfound_body(self, driver):
        main_page = MainPage(driver, 'https://reqres.in/')
        main_page.open()
        web_body, api_body = main_page.get_single_user_notfound_body()
        assert web_body == api_body


    @allure.title('POST CREATE. Проверка статус кода')
    def test_post_create_code(self, driver):
        main_page = MainPage(driver, 'https://reqres.in/')
        main_page.open()
        web_code, api_code = main_page.post_create_code()
        assert web_code == api_code

    @allure.title('POST CREATE. Проверка тела ответа')
    def test_post_create_body(self, driver):
        main_page = MainPage(driver, 'https://reqres.in/')
        main_page.open()
        web_body, payload_body = main_page.post_create_body()
        assert web_body['name'] == payload_body['name']