from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import asyncio
import allure
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))

    @allure.step('Найти элемент на странице с ожиданием')
    def find_element_with_wait(self, locator):
        timeout = 30
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located(locator))
            return element
        except asyncio.TimeoutError:
            raise asyncio.TimeoutError(
                f"Элемент {locator} не найден или не стал видимым за {timeout} сек."
            )

    @allure.step('Кликнуть на элемент с повторными попытками')
    def click_on_element(self, locator, max_retries=3):
        timeout = 30
        wait = WebDriverWait(self.driver, timeout)

        for attempt in range(max_retries):
            try:
                element = wait.until(EC.element_to_be_clickable(locator))
                element.click()
                allure.attach(
                    f"Клик выполнен успешно с {attempt + 1}-й попытки",
                    name="Результат клика",
                    attachment_type=allure.attachment_type.TEXT
                )
                return
            except asyncio.TimeoutError:
                if attempt == max_retries - 1:
                    raise asyncio.TimeoutError(
                        f"Не удалось кликнуть на элемент {locator} после {max_retries} попыток"
                    )
                # Логируем попытку
                allure.attach(
                    f"Попытка {attempt + 1} не удалась: элемент перекрыт",
                    name="Статус попытки",
                    attachment_type=allure.attachment_type.TEXT
                )
                   
    @allure.step('Ввести значение в поле ввода')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source_locator, target_locator):
        """
        Перетаскивает элемент из source_locator в target_locator с использованием JavaScript.
        :param source_locator: Локатор элемента, который нужно перетащить.
        :param target_locator: Локатор элемента, куда нужно перетащить.
        """
        self.find_element_with_wait(source_locator)
        self.find_element_with_wait(target_locator)

        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)

    @allure.step('Получить текст на элементе')
    def get_text_on_element(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator).text

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Подождать, пока элемент закроется')
    def wait_for_closing_of_element(self, locator):
        WebDriverWait(self.driver, 30).until_not(EC.visibility_of_element_located(locator))

    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))

    @allure.step('Подождать смену текста на элементе')
    def wait_for_element_to_change_text(self, locator, value):
        return WebDriverWait(self.driver, 30).until_not(EC.text_to_be_present_in_element(locator, value))
    
    @allure.step('Подождать пока элемент не станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, timeout=30).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)
