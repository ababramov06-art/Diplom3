from page_objects.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
import allure

class FeedPage(BasePage):
    @allure.step('Получить текст заголовка раздела заказов')
    def get_text_on_title_of_orders_list(self):
        return self.get_text_on_element(FeedPageLocators.TITLE_OF_ORDERS_FEED)

    @allure.step('Кликнуть по первому (последнему) заказу в ленте')
    def click_on_order_card(self):
        self.wait_visibility_of_element(FeedPageLocators.ORDER_IN_FEED)
        self.click_on_element(FeedPageLocators.ORDER_IN_FEED)

    @allure.step('Получить текст заголовка окна с деталями заказа')
    def get_text_on_title_of_modal_order(self):
        return self.get_text_on_element(FeedPageLocators.TITLE_OF_MODAL_ORDER)

    @allure.step('Получить количество заказов, выполненных за все время')
    def get_quantity_of_orders(self):
        self.find_element_with_wait(FeedPageLocators.QUANTITY_OF_ORDERS)
        return self.get_text_on_element(FeedPageLocators.QUANTITY_OF_ORDERS)

    @allure.step('Получить количество заказов, выполненных за сегодня')
    def get_daily_quantity_of_orders(self):
        self.find_element_with_wait(FeedPageLocators.DAILY_QUANTITY_OF_ORDERS)
        return self.get_text_on_element(FeedPageLocators.DAILY_QUANTITY_OF_ORDERS)

    @allure.step('Проверить наличие номера заказа в списке ленты')
    def check_id_order_in_feed(self, order_id):
        locator = FeedPageLocators.ID_ORDER_CARD_IN_FEED_WITH_SUBSTITUTIONS
        locator_with_order_id = (locator[0], locator[1].format(order_id=order_id))
        self.find_element_with_wait(locator_with_order_id)
        return self.check_displaying_of_element(locator_with_order_id)

    @allure.step('Получить номер последнего заказа в разделе "В работе"')
    def get_order_number_in_feed_progress_section(self):
        return self.get_text_on_element(FeedPageLocators.NUMBER_OF_ORDER_IN_PROGRESS)
