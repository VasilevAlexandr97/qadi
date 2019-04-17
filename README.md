# QA DartIt

Тестирование сайт http://www.dartit.ru

## Установка зависимостей

```bash
pip install selenium
pip install behave
```

## Запуск тестов

Перейти в папку с тестами, выполнить:

```bash
behave -i ui_test.feature
```

Вывод должен быть примерно таким:

```bash
Feature: Ui test # ui_test.feature:1

  Scenario: Test ui for site DartIt                                        # ui_test.feature:2
    Given website "http://www.dartit.ru/"                                  # ui_test.py:9 4.888s
    Then click link with text "Контакты"                                   # ui_test.py:17 7.567s
    Then click link with text "Екатеринбург"                               # ui_test.py:17 0.404s
    Then page include text in contacts "ул. Малышева, 51, офис 1619"       # ui_test.py:23 0.318s
    Then page include text in footer address "ул. Малышева, 51, офис 1619" # ui_test.py:33 0.058s
    Then click link with text "Продукты"                                   # ui_test.py:17 1.974s
    Then page include text in footer address "ул. Малышева, 51, офис 1619" # ui_test.py:33 0.062s
    Then click link with text "Обучение"                                   # ui_test.py:17 0.707s
    Then page include text in footer address "ул. Малышева, 51, офис 1619" # ui_test.py:33 0.037s
    Then click link with text "О компании"                                 # ui_test.py:17 0.715s
    Then page include text in footer address "ул. Малышева, 51, офис 1619" # ui_test.py:33 0.075s
    Then click link with text "Команда"                                    # ui_test.py:17 4.163s
    Then page include text in footer address "ул. Малышева, 51, офис 1619" # ui_test.py:33 0.054s
    Then click link with text "Партнеры"                                   # ui_test.py:17 0.599s
    Then page include text in footer address "ул. Малышева, 51, офис 1619" # ui_test.py:33 0.051s
    Then click link with text "Студентам"                                  # ui_test.py:17 0.870s
    Then page include text in footer address "ул. Малышева, 51, офис 1619" # ui_test.py:33 0.058s
    Then click link with text "О компании"                                 # ui_test.py:17 0.462s
    Then download file                                                     # ui_test.py:40 5.291s

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
19 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m28.353s
```

#Второе задание

Не очень понял, могу ли я использовать python для него?
