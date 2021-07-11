from datetime import date, time, datetime, timedelta


def print_date():
    current_date = date.today()
    print(current_date.strftime('%d/%m/%Y'))
    print(current_date.strftime('%A %B %Y'))


def print_time():
    current_time = time(hour=15, minute=18, second=30)
    print(current_time.strftime('%H:%M:%S'))


def print_datetime():
    current_datetime = datetime.now()
    print(current_datetime.strftime('%d/%m/%Y %H:%M:%S'))
    print(current_datetime.strftime('%c'))
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[current_datetime.weekday()])
    new_datetime = datetime(2018, 6, 20, 15, 30, 20)
    print(new_datetime.strftime('%c'))
    converter_datetime = datetime.strptime('01/01/2019 12:20:22', '%d/%m/%Y %H:%M:%S')
    print(converter_datetime)


def print_timedelta():
    current_datetime = datetime.now()
    new_date = current_datetime - timedelta(days=365, hours=2, minutes=15)
    print(new_date)


if __name__ == '__main__':
    print_date()
    print_time()
    print_datetime()
    print_timedelta()
