import configuration
import requests
import data


# Создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_USER,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


response = post_new_user(data.user_body);

print(response.status_code)
print(response.json())


# Функция получения токена
def get_new_user_token():
    user_response = post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    return auth_token


print(response.json())


# Создание набора для конкретного пользователя
def post_new_client_kit(kit_body, auth_token):
    auth_headers = data.headers_token.copy()
    auth_headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_MAIN_KITS,
                         json=kit_body,
                         headers=auth_headers)


auth_token = get_new_user_token()
client_resp = post_new_user(data.user_body.copy())
response = post_new_client_kit(data.kit_body, auth_token)
print(response.status_code)
print(response.json())


# функция меняющая значение "name"
def get_kit_body(name):
    current_name = data.kit_body.copy()
    current_name["name"] = name
    return current_name


# Функция для позитивной проверки
def positive_assert(name, auth_token):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == name


# Функция негативной проверки
def negative_assert_code_400(name, auth_token):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400
