from selenium.webdriver.common.by import By


class MainPageLocators:
    RESPONSE_CODE = (By.XPATH, "//span[@class='response-code']")
    RESPONSE_BODY = (By.XPATH, "//pre[@data-key='output-response']")
    GET_LIST_USERS = (By.XPATH, "//li[@data-id='users']")
    GET_SINGLE_USER = (By.XPATH, "//li[@data-id='users-single']")
    GET_SINGLE_NOT_FOUND = (By.XPATH, "//li[@data-id='users-single-not-found']")
    RESPONSE_CODE_BAD = (By.XPATH, "//span[@class='response-code bad']")
    POST_CREATE = (By.XPATH, "//li[@data-id='post']")
