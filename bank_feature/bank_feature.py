import json, datetime

with open('/home/course/course_27.05.23/bank_feature/operations.json', 'r', encoding="utf-8") as file:
    operations = json.load(file)


def get_formatted_date(operation):
    date_str = operation["date"]
    date = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date.strftime("%d.%m.%Y")


def get_description(operation):
    return operation["description"]


def get_from_payment_system(operation):
    if get_description(operation) != "Открытие вклада":
        from_split = operation['from'].split(" ")
        payment_system = []
        for item in from_split:
            if item.isalpha:
                payment_system.append(item)
            return " ".join(payment_system)
    else:
        return ""


def get_from_card_number(operation):
    if get_description(operation) != "Открытие вклада":
        from_split = operation['from'].split(" ")
        for item in from_split:
            if item.isdigit():
                num = item[:6] + "" + "*" * 4 + "" + item[-4:]
                return ' '.join([num[i:i+4] for i in range(0, len(num), 4)])

    else:
        return ""


def get_to_payment_system(operation):
    to_split = operation["to"].split(" ")
    payment_system = []
    for item in to_split:
        if item.isalpha:
            payment_system.append(item)
        return " ".join(payment_system)


def get_to_number(operation):
    to_split = operation["to"].split(" ")
    for item in to_split:
        if item.isdigit():
            num = "*" * 2 + item[-4:]
            return num


def get_amount(operation):
    return operation["operationAmount"]["amount"]


def get_currency(operation):
    return operation["operationAmount"]["currency"]["name"]


def get_last_five_operations(operations):
    return operations[-5:]

def get_formatted_last_five_operations(operations):
    formatted_last_five_operations = []
    for operation in operations:
        formatted_last_five_operations.append(
            f"{get_formatted_date(operation)} {get_description(operation)} \n"
            f"{get_from_payment_system(operation)} {get_from_card_number(operation)} -> {get_to_payment_system(operation)} {get_to_number(operation)} \n"
            f"{get_amount(operation)} {get_currency(operation)}")
    return formatted_last_five_operations

for operation in get_formatted_last_five_operations(get_last_five_operations(operations)):
    print("_" * 50 + "\n" + operation + "\n")
