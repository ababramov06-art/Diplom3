from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure
import time


class MainPage(BasePage):

    @allure.step('Кликнуть по кнопке "Войти в аккаунт" на главной')
    def click_on_button_login_in_main(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.click_on_element(MainPageLocators.BUTTON_LOGIN_IN_MAIN)
   
    @allure.step('Кликнуть по кнопке "Лента заказов" в хэдере')
    def click_header_feed_button(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.wait_visibility_of_element(MainPageLocators.BUTTON_ORDER_FEED_IN_HEADER)
        self.click_on_element(MainPageLocators.BUTTON_ORDER_FEED_IN_HEADER)

    @allure.step('Переход на страницу конструктора')
    def click_on_button_constructor(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.wait_visibility_of_element(MainPageLocators.HEADER_OF_PAGE_CONSTRUCTOR)
        self.click_on_element(MainPageLocators.HEADER_OF_PAGE_CONSTRUCTOR)

    @allure.step('Получение главного заголовка конструктора')
    def get_text_on_title_of_constructor(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        return self.get_text_on_element(MainPageLocators.CONSTRUCTOR_TITLE)

    
    @allure.step('Проверить отображение окна о создании заказа')
    def check_displaying_of_confirmation_modal_of_order(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.wait_visibility_of_element(MainPageLocators.CONFIRMATION_MODAL_OF_ORDER)
        return self.check_displaying_of_element(MainPageLocators.CONFIRMATION_MODAL_OF_ORDER)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        self.wait_visibility_of_element(MainPageLocators.INGREDIENT_1)
        self.click_on_element(MainPageLocators.INGREDIENT_1)

    @allure.step('Проверить отображение окна "Детали ингредиента"')
    def check_displaying_of_modal_details(self):
        self.wait_visibility_of_element(MainPageLocators.HEADER_OF_MODAL_DETAILS)
        return self.check_displaying_of_element(MainPageLocators.HEADER_OF_MODAL_DETAILS)

    @allure.step('Проверить, что окно "Детали ингредиента" не отображается')
    def check_not_displaying_of_modal_details(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.wait_for_closing_of_element(MainPageLocators.HEADER_OF_MODAL_DETAILS)
        if not self.check_displaying_of_element(MainPageLocators.HEADER_OF_MODAL_DETAILS):
            return True

    @allure.step('Закрыть окно "Детали ингредиента"')
    def close_modal(self):
        self.wait_visibility_of_element(MainPageLocators.BUTTON_CLOSE_MODAL)
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_MODAL)

    @allure.step('Добавить интгридиенты')
    def drag_and_drop_ingredient_to_order(self):
        self.drag_and_drop_element(MainPageLocators.BURGER_INGREDIENT, MainPageLocators.PLACE_FOR_INGREDIENTS)

    @allure.step('Получить количество ингредиентов')
    def get_count_of_ingredients(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        return self.get_text_on_element(MainPageLocators.COUNT_OF_INGREDIENT)

    @allure.step('Кликнуть на кнопку создания заказа')
    def click_on_button_make_order(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.click_on_element(MainPageLocators.BUTTON_MAKE_ORDER)

    @allure.step('Получить номер в окне о создании заказа')
    def get_number_of_order_in_modal_confirmation(self):
        self.wait_for_element_to_change_text(MainPageLocators.NUMBER_OF_ORDER_IN_MODAL_CONFIRMATION, '9999')
        number_of_order = 0
        with allure.step('Получаем номер заказа'):
            number_of_order = self.get_text_on_element(MainPageLocators.NUMBER_OF_ORDER_IN_MODAL_CONFIRMATION)
        return number_of_order

    @allure.step('Кликнуть на кнопку закрытия окна о создании заказа')
    def click_on_button_close_confirmation_modal(self):
        with allure.step('кликаем на кнопку закрытия окна'):
            self.check_element_is_clickable(MainPageLocators.BUTTON_CLOSE_CONFIRMATION)
            self.click_on_element(MainPageLocators.BUTTON_CLOSE_CONFIRMATION)
