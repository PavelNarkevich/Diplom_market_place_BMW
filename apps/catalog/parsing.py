import requests
from bs4 import BeautifulSoup


class Parsing:

    @staticmethod
    def get_html_code(url):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        }
        scl = requests.get(url, headers=headers)
        req = scl.text

        soup = BeautifulSoup(req, 'lxml')
        return soup

    def get_object(self, url):
        soup = self.get_html_code(url)
        try:
            car = soup.find(class_='standard-table shop').find_all('tr')
        except AttributeError:
            return None
        data = {}

        for elem in car:
            th_teg = elem.find('th').text
            td_teg = elem.find('td').text
            data[th_teg] = td_teg
        data = self.validate(data=data)
        return data

    @staticmethod
    def validate(data):
        copy_data = data.copy()
        for key, value in data.items():
            if key == 'Серия':
                copy_data['body'] = copy_data.pop(key)
                continue
            if key == 'Тип кузова':
                copy_data['body_type'] = copy_data.pop(key)
                continue
            if key == 'Модель':
                new_value = value.split()
                copy_data['model'] = new_value[0]
                copy_data['engine_code'] = new_value[1]
                copy_data.pop(key)
                continue
            if key == 'Трансмиссия':
                if value == 'Автоматическая КПП':
                    copy_data['transmission'] = 'АКПП'
                    copy_data.pop(key)
                    continue

                copy_data['transmission'] = 'КПП'
                copy_data.pop(key)
                continue

            copy_data.pop(key)
        return copy_data

    def get_car(self, vin_code: str):
        url = f'https://drive.by/spare/etk/vin/{vin_code.upper()}/'

        car = self.get_object(url=url)
        return car
