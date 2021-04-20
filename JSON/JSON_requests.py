"""
Implement CRUD on JSON data via node.js server

"""
import json
import requests


key_names = ['id', 'brand', 'model', 'production_year', 'convertible']
key_widths = [10,15,10,20,15]

def show_head():
    """print headers"""
    for (name,width) in zip(key_names, key_widths):
        print(name.ljust(width), end='| ')
    print()

def show_car(car):
    """print details"""
    for (name, width) in zip(key_names, key_widths):
        print(str(car[name]).ljust(width), end='| ')
    print()

def show_empty():
    """print empty lines if no data"""
    for width in key_widths:
        print(' '.ljust(width), end='| ')
    print()

def show(json_obj):
    """feed json data to print methods"""
    show_head()
    if isinstance(json_obj, list):
        for car in json_obj:
            show_car(car)
    if isinstance(json_obj,dict):
        if json_obj:
            show_car(json_obj)
        else:
            show_empty()

class Car:
    """create new car"""
    def __init__(self, id, brand, model, production_year, convertible):
        self.id = id
        self.brand = brand
        self.model = model
        self.production_year = production_year
        self.convertible = convertible

class EncodeJson(json.JSONEncoder):
    """encode class data to JSON"""
    def default(self, car_cls):
        if isinstance(car_cls, Car):
            return car_cls.__dict__
        else:
            return super().default(self, z)

headers_close = {'Connection': 'Close'}
headers_content = {'Content-Type': 'application/json'}

new_car = Car(9, 'Porsche', '911', 1964, False)
print(json.dumps(new_car, cls=encode_json))


try:
    # reply = requests.get('http://127.0.0.1:3000/cars', timeout=1)
    # reply = requests.get('http://127.0.0.1:3000/cars/2', timeout=1)
    # reply = requests.get('http://127.0.0.1:3000/cars?_sort=production_year', timeout=1)
    # reply = requests.get('http://127.0.0.1:3000/cars?_sort=production_year&_order=desc', timeout=1)

    # reply = requests.delete('http://127.0.0.1:3000/cars/2', timeout=1)
    # print(f'delete result = {reply.status_code}')

    # reply = requests.post('http://127.0.0.1:3000/cars', timeout=1, headers=headers_content, data=json.dumps(new_car, cls=EncodeJson))
    # print(f'post result = {reply.status_code}')

    reply = requests.put('http://127.0.0.1:3000/cars/9', timeout=1, headers=headers_content, data=json.dumps(new_car, cls=EncodeJson))
    print(f'put result = {reply.status_code}')

    reply = requests.get('http://127.0.0.1:3000/cars', timeout=1, headers=headers_close)
except requests.exceptions.ConnectionError:
    print('Nobody\'s home, sorry!')
except requests.exceptions.Timeout:
    print('Sorry, Mr. Impatient, you did not get your data.')
except requests.RequestException:
    print('Communication Error')
else:
    # print(reply)
    print(f'connection result {reply.status_code}')
    print(f'Connection = {reply.headers["Connection"]}')
    if reply.status_code == requests.codes.ok: #pylint: disable=E1101
        print('good Connection established')
        # print(reply.headers)
        print(f"content type = {reply.headers['Content-Type']}")
        # print(reply.text)
        # print(reply.json())
        show(reply.json())
    elif reply.status_code == requests.codes.not_found: #pylint: disable=E1101
        print('resource not found')
    else:
        print('Server Error')
