import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import requests
from config import BASE_URL, ENDPOINTS, generate_item_data, generate_seller_id, DEFAULT_HEADERS

# Загружаем feature файл
scenarios('avito_api.feature')

# Фикстуры
@pytest.fixture
def context():
    return {}

@pytest.fixture
def api_client():
    session = requests.Session()
    session.headers.update(DEFAULT_HEADERS)
    return session

# Background
@given("API сервер доступен")
def api_server_available(context):
    response = requests.get(BASE_URL)
    assert response.status_code in [200, 404, 403]

# Шаги для данных
@given("имеем валидные данные для объявления")
def valid_item_data(context):
    context['item_data'] = generate_item_data()

@given("имеем данные с невалидным sellerId")
def invalid_seller_id_data(context):
    context['item_data'] = generate_item_data()
    context['item_data']['sellerID'] = "abc"

@given("имеем ID объявления")
def have_item_id(context):
    context['item_id'] = "test_id_123"

@given("имеем ID продавца")
def have_seller_id(context):
    context['seller_id'] = generate_seller_id()

# Шаги для действий  
@when("отправляем POST запрос на создание объявления")
def send_post_request(context, api_client):
    url = f"{BASE_URL}{ENDPOINTS['create_item']}"
    response = api_client.post(url, json=context['item_data'])
    context['response'] = response
    print(f"POST {url} -> Status: {response.status_code}")

@when("отправляем GET запрос на получение объявления")
def send_get_item_request(context, api_client):
    url = f"{BASE_URL}{ENDPOINTS['get_item'].format(id=context['item_id'])}"
    response = api_client.get(url)
    context['response'] = response
    print(f"GET {url} -> Status: {response.status_code}")

@when("отправляем GET запрос на получение объявлений продавца")
def send_get_seller_request(context, api_client):
    url = f"{BASE_URL}{ENDPOINTS['get_seller_items'].format(sellerId=context['seller_id'])}"
    response = api_client.get(url)
    context['response'] = response
    print(f"GET {url} -> Status: {response.status_code}")

@when("отправляем GET запрос на получение статистики")
def send_get_stats_request(context, api_client):
    url = f"{BASE_URL}{ENDPOINTS['get_statistics'].format(id=context['item_id'])}"
    response = api_client.get(url)
    context['response'] = response
    print(f"GET {url} -> Status: {response.status_code}")

# Шаги для проверок
@then(parsers.parse('получаем статус код {status_code:d}'))
def check_status_code(status_code, context):
    assert context['response'].status_code == status_code