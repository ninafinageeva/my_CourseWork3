from src.func import open_json, sorting_by_executed, sorting_by_five_last_string, output_trans

class Tests:
    def test_open_json(self):
        """Проверка необходимых ключей в json"""
        js = {"id", "state", "date", "operationAmount", "amount", "currency", "name", "code", "description", "from", "to"}
        assert js in open_json()

    def sorting_by_executed(self):
        """Если подается ключ 'state' со значением 'CANCELED', тест операцию не засчитывает"""
        sort = [{"state": "EXECUTED"}, {"state": "CANCELED"}]
        assert sorting_by_executed(sort) == [{"state": "EXECUTED"}]

    def sorting_by_five_last_string(self):
        """Проверка на правильную сортировку с верной длиной"""
        string = [{"date": "2019-08-26T10:50:58.294041"}, {"date": "2019-07-03T18:35:29.512364"},
                  {"date": "2018-06-30T02:08:58.425572"}, {"date": "2018-03-23T10:45:06.972075"},
                  {"date": "2019-04-04T23:20:05.206878"}, {"date": "2019-03-23T01:09:46.296404"}]
        assert len(sorting_by_five_last_string(string)) == 5
        assert sorting_by_five_last_string(string) == [{"date": "2019-08-26T10:50:58.294041"},
                                                       {"date": "2019-07-03T18:35:29.512364"},
                                                       {"date": "2019-04-04T23:20:05.206878"},
                                                       {"date": "2019-03-23T01:09:46.296404"},
                                                       {"date": "2018-06-30T02:08:58.425572"}]

    def output_trans(self):
        """Проверка на правильную  реформацию входящих данных"""
        input_ = [{
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        }
        ]
        assert output_trans(input_) == ['13.07.2019 Перевод с карты на счет\n'
                                        'Maestro 1308 79** **** 7170 -> Счет **8612\n'
                                        '97853.86 руб.\n']
