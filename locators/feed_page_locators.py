from selenium.webdriver.common.by import By


class FeedPageLocators:
    
    # Заголовок ленты заказов
    TITLE_OF_ORDERS_FEED = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')

    # Карточка заказа в ленте
    ORDER_IN_FEED = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')

    # Заголовок всплывающего окна с деталями заказа
    TITLE_OF_MODAL_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                      '"Modal_orderBox")]//h2')

    # Счетчик заказов "Выполнено за все время"
    QUANTITY_OF_ORDERS = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')

    # Счетчик заказов "Выполнено за сегодня"
    DAILY_QUANTITY_OF_ORDERS = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')

    # Номер заказа в разделе "В работе"
    NUMBER_OF_ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, '
                                             '"OrderFeed_orderListReady")]/li[contains(@class, '
                                             '"text_type_digits-default")]')

    # Номер заказа в ленте — заготовка, в которую нужно подставить id искомого заказа
    ID_ORDER_CARD_IN_FEED_WITH_SUBSTITUTIONS = (By.XPATH, './/*[text()="{order_id}"]')
