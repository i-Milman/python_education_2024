import requests, numpy, pandas, matplotlib.pyplot as plt


def get_currency_rates() -> pandas.DataFrame | None:
    """
    Получает актуальный курс валют от ЦБ РФ в виде DataFrame
    """
    def extract_xml_value(xml_block: str, tag: str) -> str:
        """
        Извлекает значение тега из заданного XML-блока.
        """
        start = xml_block.find(f'<{tag}>') + len(f'<{tag}>')
        end = xml_block.find(f'</{tag}>')
        return xml_block[start:end]

    try:
        url = "https://www.cbr-xml-daily.ru/daily_eng.xml"
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('\033[31mОшибка соединения с сервером ЦБ РФ.')
        return None

    if response.status_code == 200:
        # Парсим XML-ответ
        start = response.text.find('<Valute ID="')
        rates = []

        while start != -1:
            end = response.text.find('</Valute>', start)
            valute_block = response.text[start:end + len('</Valute>')]

            # Извлекаем данные о валюте
            currency_numcode = extract_xml_value(valute_block, 'NumCode')
            currency_code = extract_xml_value(valute_block, 'CharCode')
            currency_name = extract_xml_value(valute_block, 'Name')
            nominal = int(extract_xml_value(valute_block, 'Nominal'))
            currency_value = float(extract_xml_value(valute_block, 'Value').replace(',', '.'))

            # Приводим курс к единому виду (за единицу валюты)
            currency_value /= nominal

            rates.append({
                "Numeric Code": currency_numcode,
                "Symbolic Code": currency_code,
                "Currency Name": currency_name,
                "Value (RUB)": currency_value
            })

            start = response.text.find('<Valute ID="', end)

        return pandas.DataFrame(rates)
    else:
        print('\033[31mОшибка при получении курса валют.')
        return None


if __name__ == '__main__':
    # Вызов функции для получения и вывода курса валют
    rates = get_currency_rates()

    if rates is not None:
        # Сохраняю результаты в файл, игнорируея сгенерированные индексы
        rates.to_csv('actual_currency_rates.csv', index=False)

        # Читаю данные из файла
        rates = pandas.read_csv('actual_currency_rates.csv')

        # Вывожу результаты на терминал
        print(rates, end='\n\n')

        # Применяю дополнительно сортировку по ценам, добавлен срез для инверсии, затем выполнен сброс нумерации строк,
        # drop=True убирает внесение старого индекса в качестве столбца
        print(rates.sort_values('Value (RUB)')[::-1].reset_index(drop=True), end='\n\n')

        # Пример использования numpy (создание массива, математическая операция и вывод результата)
        print('Купить каждую валюту в количестве 1 нам будет стоить: ' +
              f'{numpy.sum(rates['Value (RUB)'].to_numpy()):.2f} руб.')

        # Пример использования matplotlib
        # Выбор столбцов для отображения
        x_column = 'Currency Name'
        y_column = 'Value (RUB)'

        # Создание фигуры и осей
        fig, ax = plt.subplots(figsize=(12, 6))

        # Построение графика
        ax.bar(rates[x_column], rates[y_column])

        # Настройка тиков по оси X
        ax.set_xticks(range(len(rates[x_column])))
        ax.set_xticklabels(rates[x_column], rotation=90, )

        # Добавление заголовка, подписей к осям
        ax.set_title('График валют')
        ax.set_xlabel('Валюта')
        ax.set_ylabel('Значение')

        # Отображение графика
        plt.show()
