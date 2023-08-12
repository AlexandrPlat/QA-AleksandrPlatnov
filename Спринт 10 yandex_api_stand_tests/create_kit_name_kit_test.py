import sender_stand_request
import data

# получаем токен
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    return auth_token


# Функция, меняющая содержимое тела запроса
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body


# Функция для позитивной проверки
def positive_assert(name):
    # В переменную kit_body сохраняется обновлённое тело запроса:
    kit_body = get_kit_body(name)
    # Передаем auth_token
    auth_token = get_new_user_token()
    # В переменную kit_responce сохраняется результат запроса на создание нового набора:
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверяется, что имя в наборе соответствует тому что задано
    assert kit_response.json()["name"] == name


 # Функция для негативной проверки
def negative_assert_code_400(name):
    # В переменную kit_body сохраняется обновлённое тело запроса:
    kit_body = get_kit_body(name)
    # Передаём auth_token
    auth_token = get_new_user_token()
    # В response сохраняется результат
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    #  Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400


def negative_assert_no_name(kit_body):
    auth_token = get_new_user_token()
    headers = get_headers(auth_token)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, headers)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["massage"] == "Не все необходимые параметры были переданы"



# 1-ый тест. Количество символов в названии набора - 1 символ
def test_create_kit_1_letter_in_kit_name_get_success_response():
    positive_assert("a")


# 2-ой тест. Количество символов в названии набора - 511 символов
def test_create_kit_511_letters_in_kit_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# 3-ий тест. Количество символов - 0 символов
# Здесь ошибка
def test_create_kit_0_letter_in_kit_name_get_error_response():
    negative_assert_code_400("")


# 4-ый тест. Количество символов в названии набора - 512 символов
# Здесь ошибка
def test_create_kit_512_letters_in_kit_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# 5-ый тест. Разрешены английские буквы в названии набора - "QWErty"
def test_create_kit_english_letters_in_kit_name_get_success_response():
    positive_assert("QWErty")


# 6-ой тест. Разрешены русские буквы в названии набора - "Мария"
def test_create_kit_russian_letters_in_kit_name_get_success_response():
    positive_assert("Мария")


# 7-ой тест. Разрешены спецсимволы в названии набора - "№%@","
def test_create_kit_special_symbols_in_kit_name_get_success_response():
    positive_assert('"№%@",')


# 8-ой тест. Разрешены пробелы в названии набора - "Человек и КО"
def test_create_kit_spaces_in_kit_name_get_success_response():
    positive_assert(" Человек и КО ")


# 9-ый тест. Разрешены цифры в названии набора - "123"
def test_create_kit_numbers_in_kit_name_get_success_response():
    positive_assert("123")


# 10-ый тест. Параметр не передан в названии набора
# Здесь ошибка
def test_create_kit_no_name_get_error_response():
   # копирование словаря с телом запроса из data
   current_kit_body = data.kit_body.copy()
   #удаление параметра из запроса
   current_kit_body.pop("name")
   negative_assert_no_name(current_kit_body)

# 11-ый тест. Передан другой тип параметра в названии набора - 123
# Здесь ошибка
def test_create_kit_type_number_in_kit_name_get_error_response():
    negative_assert_code_400(123)