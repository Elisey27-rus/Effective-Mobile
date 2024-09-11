# Проект автоматического тестирования

## Описание

Этот проект включает два автоматических теста:
1. **`test_api.py`** - Тест для работы с GitHub API, который выполняет создание, проверку и удаление репозитория.
2. **`test_ui.py`** - E2E (end-to-end) тест для проверки сценария покупки товара на сайте [saucedemo.com](https://www.saucedemo.com) с использованием Playwright.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone 'https://github.com/Elisey27-rus/Effective-Mobile'
    ```

2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

3. Создайте файл `.env` в корне проекта и добавьте ваши данные:
    ```
    GITHUB_USERNAME=ваше_имя_пользователя
    GITHUB_TOKEN=ваш_токен
    REPO_NAME=имя_тестового_репозитория
    ```

## Запуск тестов

### Запуск теста GitHub API

Используйте команду:
```bash
python test_api.py

### Запуск теста проверки playwright

Используйте команду:
```bash
python test_ui.py