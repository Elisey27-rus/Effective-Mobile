import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

USERNAME = os.getenv('GITHUB_USERNAME')
TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')

API_URL = 'https://api.github.com'


def create_repo():
    """Создание нового публичного репозитория на GitHub."""
    url = f'{API_URL}/user/repos'
    headers = {'Authorization': f'token {TOKEN}'}
    data = {'name': REPO_NAME, 'public': True}

    # Отправка запроса на создание репозитория
    response = requests.post(url, json=data, headers=headers)

    # Печать дополнительной информации для отладки
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.json()}")

    assert response.status_code == 201, f"Failed to create repo: {response.status_code}, {response.json()}"
    print(f"Repository '{REPO_NAME}' created successfully.")


def check_repo_exists():
    """Проверка наличия репозитория на GitHub."""
    url = f'{API_URL}/repos/{USERNAME}/{REPO_NAME}'
    headers = {'Authorization': f'token {TOKEN}'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Repository does not exist: {response.json()}"
    print(f"Repository '{REPO_NAME}' exists.")


def delete_repo():
    """Удаление репозитория с GitHub."""
    url = f'{API_URL}/repos/{USERNAME}/{REPO_NAME}'
    headers = {'Authorization': f'token {TOKEN}'}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204, f"Failed to delete repo: {response.json()}"
    print(f"Repository '{REPO_NAME}' deleted successfully.")


def test_github_api():
    """Основная функция для запуска всех тестов GitHub API."""
    create_repo()
    check_repo_exists()
    delete_repo()


if __name__ == "__main__":
    test_github_api()
