import sender_stand_request


# Тест1 Допустимое количество символов (1)
def test_create_kit_1_letter_in_name_get_succes_response_201():
    sender_stand_request.positive_assert("a", sender_stand_request.auth_token)


# Тест2 Допустимое количество символов (511)
def test_create_kit_511_letter_in_name_get_succes_response_201():
    sender_stand_request.positive_assert("Abcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabbcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC", sender_stand_request.auth_token)


# Тест3 Количество символов меньше допустимого (0)
def test_create_kit_0_letter_in_name_get_succes_response_400():
    sender_stand_request.negative_assert_code_400("", sender_stand_request.auth_token)


# Тест4 Количество символов больше допустимого (512)
def test_create_kit_512_letter_in_name_get_succes_response_400():
    sender_stand_request.negative_assert_code_400("Abcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD", sender_stand_request.auth_token)


# Тест5 Разрешены английские буквы
def test_create_kit_english_letter_in_name_get_succes_response_201():
    sender_stand_request.positive_assert("QWErty", sender_stand_request.auth_token)


# Тест6 Разрешены русские буквы
def test_create_kit_russian_letter_in_name_get_succes_response_201():
    sender_stand_request.positive_assert("Мария", sender_stand_request.auth_token)


# Тест7 Разрешены спецсимволы
def test_create_kit_special_characters_in_name_get_succes_response_201():
    sender_stand_request.positive_assert("%@", sender_stand_request.auth_token)


# Тест8 Разрешены пробелы
def test_create_kit_numbers_in_name_get_succes_response_201():
    sender_stand_request.positive_assert("123", sender_stand_request.auth_token)

# Тест10 Параметр не передан в запросе
def test_parameter_was_not_passed_in_the_request_400():
    sender_stand_request.negative_assert_code_400({}, sender_stand_request.auth_token)

# Тест11 Передан другой тип параметра (число)
def test_different_type_of_parameter_was_passed_400():
        sender_stand_request.negative_assert_code_400(123, sender_stand_request.auth_token)
