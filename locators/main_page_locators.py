from selenium.webdriver.common.by import By


class MainPageLocators:
   # Кнопка "Конструктор" в шапке сайта
    header_of_page_constructor = (By.XPATH, '//p[text() = "Конструктор"]')

    # Заголовок раздела "Конструктор"
    constructor_title = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1')

    # Кнопка "Лента заказов"
    button_order_feed_in_header = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')

    # Куда перетаскиваются игнредиенты
    place_for_ingredients = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')

   # Кнопка "Оформить заказ"
    button_make_order = (By.CLASS_NAME, 'button_button__33qZ0')

    # Количество экземпляров ингредиента в заказе (счетчик)
    count_of_ingredient = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p['
                                     '@class="counter_counter__num__3nue1"][1]')

    # Окно подтверждения создания заказа
    confirmation_modal_of_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                             '(@class, "Modal_modal__container")]')

    # Номер созданного заказа в окне подтверждения
    number_of_order_in_modal_confirmation = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')

    # Кнопка с крестиком, закрывающая окно подтвержденного заказа
    button_close_confirmation = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")'
                                           ']//button[contains(@class, "close")]')

    # Оверлей. Подарок от наставника.
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"

     # Картинка ингредиента в общем списке
    burger_ingredient = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')

    # Ингредиент
    ingredient_1 = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]')

    # Кнопка с крестиком, закрывающая окно "Детали ингредиента"
    button_close_modal = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "close")]')
    
    # Заголовок окна "Детали ингредиента"
    header_of_modal_details = (By.XPATH, '//div[@class="Modal_modal__container__Wo2l_"]//h2')
   