from page_objects.feed_page import FeedPage
from page_objects.main_page import MainPage
from page_objects.order_history_page import OrderHistoryPage
from page_objects.account_page import AccountPage
from conftest import *
import allure
from selenium.common.exceptions import TimeoutException

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
       
    # Авторизация
        main_page.click_on_button_login_in_main()
     
    # Сборка заказа
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
    
    # Ожидание появления модального окна с номером заказа и получение ID
        try:
            new_order_id = main_page.get_number_of_order_in_modal_confirmation()
            # Гибкое сравнение номеров заказа (игнорируем ведущий ноль)
            if new_order_id.startswith('0'):
                new_order_id_clean = new_order_id[1:]  # убираем ведущий ноль
            else:
                new_order_id_clean = new_order_id
        except TimeoutException:
            raise AssertionError("Не удалось получить номер заказа из модального окна")
        
    # Закрытие модального окна
        main_page.click_on_button_close_confirmation_modal()

    # Переход на страницу ленты заказов
        main_page.click_header_feed_button()
       
    # Ожидание появления заказа в разделе «В работе»
        try:
            order_in_progress = feed_page.get_order_number_in_feed_progress_section()
        except TimeoutException:
            raise AssertionError("Заказ не появился в разделе «В работе» в течение 20 с")
    
        assert new_order_id_clean == order_in_progress.strip(), \
        f"Номер заказа {new_order_id_clean} не найден в разделе «В работе» (найдено: {order_in_progress})"

    
