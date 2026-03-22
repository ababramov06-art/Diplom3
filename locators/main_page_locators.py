from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной
    BUTTON_LOGIN_IN_MAIN = By.XPATH, './/button[text() = "Войти в аккаунт"]'

     # Кнопка "Конструктор" в шапке сайта
    HEADER_OF_PAGE_CONSTRUCTOR = (By.XPATH, '//p[text() = "Конструктор"]')

    # Заголовок раздела "Конструктор"
    CONSTRUCTOR_TITLE = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1')

        # Кнопка "Лента заказов"
    BUTTON_ORDER_FEED_IN_HEADER = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')

    # Куда перетаскиваются игнредиенты
    PLACE_FOR_INGREDIENTS = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')

   # Кнопка "Оформить заказ"
    BUTTON_MAKE_ORDER = (By.CLASS_NAME, 'button_button__33qZ0')

    # Количество экземпляров ингредиента в заказе (счетчик)
    COUNT_OF_INGREDIENT = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p['
                                     '@class="counter_counter__num__3nue1"][1]')

    # Окно подтверждения создания заказа
    CONFIRMATION_MODAL_OF_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                             '(@class, "Modal_modal__container")]')

    # Номер созданного заказа в окне подтверждения
    NUMBER_OF_ORDER_IN_MODAL_CONFIRMATION = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')

    # Кнопка с крестиком, закрывающая окно подтвержденного заказа
    BUTTON_CLOSE_CONFIRMATION = (By.XPATH, '//button[contains(@class, "close")]')

    # Оверлей. Подарок от наставника.
    #OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    OVERLAY = By.XPATH, './/div[contains(@class, "Modal_modal_overlay__x2ZCr")]'
                        

     # Картинка ингредиента в общем списке
    BURGER_INGREDIENT = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')
    # Ингредиент
    INGREDIENT_1 = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]')

    # Кнопка с крестиком, закрывающая окно "Детали ингредиента"
    BUTTON_CLOSE_MODAL = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "close")]')
    
    # Заголовок окна "Детали ингредиента"
    HEADER_OF_MODAL_DETAILS = (By.XPATH, '//div[@class="Modal_modal__container__Wo2l_"]//h2')
   