import json
from datetime import datetime


def open_json() -> list: # Почему функция не чистая
    """Читает файл json"""
    with open('operations.json') as f:
        return json.load(f)


def sorting_by_executed(operation) -> list:
    """Сортировка по выполненным состояниям"""
    exe = []
    for item in operation:
        if item.get("state") == "EXECUTED":
            exe.append(item)
    return exe


def sorting_by_five_last_string(last_string):
    """Сортировка по пяти последним операциям"""
    sort = sorted(last_string, key=lambda x: x["date"], reverse=True) #"%Y-%m-%dT%H:%M:%S.%f")
    last = sort[:5]
    return last

def format_data(data):
    list_format = []
    for item in data:
        format = datetime.strptime(item["date"],"%Y-%m-%dT%H:%M:%S.%f")
        date_form = f'{format: %d.%m.%Y}'
        list_format.append(date_form)
    return list_format


def output_trans(date_from) -> list:
    data_list = []
    for i in date_from:
        date = datetime.fromisoformat(i["date"]).strftime("%d.%m.%Y")
        description = i["description"]
        amount_currency = f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"
        if "from" in i:
            sender = i["from"].split()
            recipient = i["to"].split()
            sender_num = sender.pop()
            recipient_num = recipient.pop()
            if len(sender_num) == 16:
                hide_sender_num = f'{sender_num[:4]} {sender_num[4:6]}** **** {sender_num[-4:]}'
            elif len(sender_num) == 20:
                hide_sender_num = f'** {sender_num[-4:]}'

            if len(recipient_num) == 16:
                hide_recipient_num = f'{recipient_num[:4]} {recipient_num[4:6]}** **** {recipient_num[-4:]}'
            elif len(recipient_num) == 20:
                hide_recipient_num = f'** {recipient_num[-4:]}'
            to_info = f'{" ".join(recipient)} {hide_recipient_num}'
            to_sender = f'{" ".join(sender)} {hide_sender_num}'
            data_list.append(f'{date} {description}\n{to_sender} -> {to_info}\n{amount_currency}\n')
        else:
             to_info = f'**{i["to"][-4:]}'
             data_list.append(f'{date} {description}\nСчет {to_info}\n{amount_currency}\n')
    return data_list