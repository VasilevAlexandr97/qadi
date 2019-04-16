Feature: Ui test
Scenario: Test ui for site DartIt


Given website "http://www.dartit.ru/"
Then click link with text "Контакты"
Then click link with text "Екатеринбург"
Then page include text in contacts "ул. Малышева, 51, офис 1619"
Then page include text in footer address "ул. Малышева, 51, офис 1619"
Then click link with text "Продукты"
Then page include text in footer address "ул. Малышева, 51, офис 1619"
Then click link with text "Обучение"
Then page include text in footer address "ул. Малышева, 51, офис 1619"
Then click link with text "О компании"
Then page include text in footer address "ул. Малышева, 51, офис 1619"
Then click link with text "Команда"
Then page include text in footer address "ул. Малышева, 51, офис 1619"
Then click link with text "Партнеры"
Then page include text in footer address "ул. Малышева, 51, офис 1619"
Then click link with text "Студентам"
Then page include text in footer address "ул. Малышева, 51, офис 1619"
Then click link with text "О компании"
Then download file