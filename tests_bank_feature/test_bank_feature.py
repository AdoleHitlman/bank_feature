import json
from bank_feature import bank_feature

with open('/home/course/course_27.05.23/bank_feature/operations.json', 'r', encoding="utf-8") as file:
    operations = json.load(file)

test_operation = operations[0]


def test_get_formatted_date():
    assert bank_feature.get_formatted_date(test_operation) == "26.08.2019"

def test_get_description():
    assert  bank_feature.get_description(test_operation) == "Перевод организации"

def test_get_from_payment_system():
    assert bank_feature.get_from_payment_system(test_operation) == "Maestro"

def test_get_from_card_number():
    assert bank_feature.get_from_card_number(test_operation) == '1596 83** **51 99'

def test_get_to_payment_system():
    assert bank_feature.get_to_payment_system(test_operation) == "Счет"

def test_get_to_number():
    assert bank_feature.get_to_number(test_operation) == "**9589"

def test_get_amount():
    assert bank_feature.get_amount(test_operation) == "31957.58"

def test_get_currency():
    assert bank_feature.get_currency(test_operation) == "руб."

def test_get_last_five_operations():
    assert bank_feature.get_last_five_operations(operations) == [{'id': 27192367, 'state': 'CANCELED', 'date': '2018-12-24T20:16:18.819037', 'operationAmount': {'amount': '991.49', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 71687416928274675290', 'to': 'Счет 87448526688763159781'}, {'id': 921286598, 'state': 'EXECUTED', 'date': '2018-03-09T23:57:37.537412', 'operationAmount': {'amount': '25780.71', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Счет 26406253703545413262', 'to': 'Счет 20735820461482021315'}, {'id': 207126257, 'state': 'EXECUTED', 'date': '2019-07-15T11:47:40.496961', 'operationAmount': {'amount': '92688.46', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 35737585785074382265'}, {'id': 957763565, 'state': 'EXECUTED', 'date': '2019-01-05T00:52:30.108534', 'operationAmount': {'amount': '87941.37', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 46363668439560358409', 'to': 'Счет 18889008294666828266'}, {'id': 667307132, 'state': 'EXECUTED', 'date': '2019-07-13T18:51:29.313309', 'operationAmount': {'amount': '97853.86', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'Maestro 1308795367077170', 'to': 'Счет 96527012349577388612'}]

def test_get_formatted_last_five_operations():
    assert bank_feature.get_formatted_last_five_operations(bank_feature.get_last_five_operations(operations)) == ['24.12.2018 Перевод со счета на счет \nСчет 7168 74** **52 90 -> Счет **9781 \n991.49 руб.', '09.03.2018 Перевод организации \nСчет 2640 62** **32 62 -> Счет **1315 \n25780.71 руб.', '15.07.2019 Открытие вклада \n  -> Счет **2265 \n92688.46 USD', '05.01.2019 Перевод со счета на счет \nСчет 4636 36** **84 09 -> Счет **8266 \n87941.37 руб.', '13.07.2019 Перевод с карты на счет \nMaestro 1308 79** **71 70 -> Счет **8612 \n97853.86 руб.']