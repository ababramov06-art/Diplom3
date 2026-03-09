from page_objects.feed_page import FeedPage
from page_objects.main_page import MainPage
from conftest import *
import allure
class TestFeedPage:

    @allure.title('Проверка увеличения числа на счетчике общего количества выполненных заказов')
    def test_changes_counter_for_quantity_of_orders_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_header_feed_button()
        orders_count_1 = feed_page.get_quantity_of_orders()
        main_page.click_on_button_constructor()
        main_page.click_on_button_login_in_main()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        main_page.click_on_button_close_confirmation_modal()
        main_page.click_header_feed_button()
        orders_count_2 = feed_page.get_quantity_of_orders()
        assert orders_count_1 < orders_count_2

    @allure.title('Проверка увеличения числа на счетчике ежедневного количества выполненных заказов')
    def test_changes_counter_for_daily_quantity_of_orders_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_header_feed_button()
        orders_count_1 = feed_page.get_daily_quantity_of_orders()
        main_page.click_on_button_constructor()
        main_page.click_on_button_login_in_main()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        main_page.click_on_button_close_confirmation_modal()
        main_page.click_header_feed_button()
        orders_count_2 = feed_page.get_daily_quantity_of_orders()
        assert orders_count_1 < orders_count_2

    @allure.title('Проверка появления нового заказа в разделе "В работе"')
    def test_displaying_new_order_in_progress_feed_success(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_on_button_login_in_main()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        
        new_order_id = main_page.get_number_of_order_in_modal_confirmation()
        main_page.click_on_button_close_confirmation_modal()
        main_page.click_header_feed_button()
        order_in_progress_id = feed_page.get_order_number_in_feed_progress_section()
        assert new_order_id in order_in_progress_id
