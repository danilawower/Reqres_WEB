import ast
import allure
import requests
import json
from locators.reqres_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators

    @allure.step('Нажать на кнопку GET LIST')
    def get_list_users_code(self):
        button = self.element_is_clickable(self.locators.GET_LIST_USERS)
        button.click()
        with allure.step('Получить статус код веб'):
            resp_code = self.element_is_present(self.locators.RESPONSE_CODE)
            status_code = resp_code.text
        with allure.step('Получить статус код api'):
            api_request = requests.get('https://reqres.in/api/users?page=2')
            api_status_code = api_request.status_code
            str_status_code = str(api_status_code)
        return status_code, str_status_code


    @allure.step('Нажать на кнопку GET LIST')
    def get_list_users_body(self):
        button = self.element_is_clickable(self.locators.GET_LIST_USERS)
        button.click()
        with allure.step('Получить тело запроса веб'):
            resp_body = self.element_is_present(self.locators.RESPONSE_BODY)
            body_text = resp_body.text
            json_body_text = ast.literal_eval(body_text)
        with allure.step('Получить тело запроса аpi'):
            api_body = requests.get('https://reqres.in/api/users?page=2')
            json_data = api_body.json()
        return json_body_text, json_data


    def get_single_user_code(self):
        button = self.element_is_clickable(self.locators.GET_SINGLE_USER)
        button.click()
        resp_code = self.element_is_present(self.locators.RESPONSE_CODE)
        status_code = resp_code.text
        api_request = requests.get('https://reqres.in/api/users/2')
        api_status_code = api_request.status_code
        str_status_code = str(api_status_code)
        return status_code, str_status_code


    def get_single_user_body(self):
        button = self.element_is_clickable(self.locators.GET_SINGLE_USER)
        button.click()
        resp_body = self.element_is_present(self.locators.RESPONSE_BODY)
        body_text = resp_body.text
        json_body_text = ast.literal_eval(body_text)
        api_body = requests.get('https://reqres.in/api/users/2')
        json_data = api_body.json()
        return json_body_text, json_data


    def get_single_user_notfound_code(self):
        button = self.element_is_clickable(self.locators.GET_SINGLE_NOT_FOUND)
        button.click()
        resp_code = self.element_is_present(self.locators.RESPONSE_CODE_BAD)
        status_code = resp_code.text
        api_request = requests.get('https://reqres.in/api/users/23')
        api_status_code = api_request.status_code
        str_status_code = str(api_status_code)
        return status_code, str_status_code


    def get_single_user_notfound_body(self):
        button = self.element_is_clickable(self.locators.GET_SINGLE_NOT_FOUND)
        button.click()
        resp_body = self.element_is_present(self.locators.RESPONSE_BODY)
        body_text = resp_body.text
        json_body_text = ast.literal_eval(body_text)
        api_body = requests.get('https://reqres.in/api/users/23')
        json_data = api_body.json()
        return json_body_text, json_data

    # Здесь я попытался взять данные с минимальным включением реквест запросов в коде web тестов. Больше взаимодействую с UI.
    # Далее, все гет работают по подобному принципу. Беру статус код респонса с интерфейса, интерпритирую его,
    # как строковое значение, тоже делаю с api кодом.
    # Тело респонса я беру с веба в текстовом формате, беру json с аpi и конвертирую str формат в dict,
    # позволяя assert'у пройти. Так как значения одинаковые, их мы и сравниваем


    def post_create_code(self):
        button = self.element_is_clickable(self.locators.POST_CREATE)
        button.click()
        resp_code = self.element_is_present(self.locators.RESPONSE_CODE)
        status_code = resp_code.text
        api_request = requests.post('https://reqres.in/api/users')
        api_status_code = api_request.status_code
        str_status_code = str(api_status_code)
        return status_code, str_status_code


    def post_create_body(self):
        button = self.element_is_clickable(self.locators.POST_CREATE)
        button.click()
        resp_body = self.element_is_present(self.locators.RESPONSE_BODY)
        body_text = resp_body.text
        json_body_text = ast.literal_eval(body_text)
        payload = self.post_payload()
        return json_body_text, payload

    #В POST запросе больше углубился в API команды. Создал выгрузку, по которой сверяется контент.
    #По нему сделал assert
    #Далее принцип схожий. Где тело web и json совпадают, там конвертирую и сравниваю значения. Где нет, сравниваю с заранее
    #подготовленным payload.
    #В allure фикстуру все обматывать не стал, указал просто для примера, как я работал с ним
