from parser_otomoto import parse
from pathlib import Path
import pickle

search_link = 'https://www.otomoto.pl/osobowe/gdansk/-/-/-/-/minivan--kombi/?search%5Bfilter_float_price%3Ato%5D=10000&search%5Bfilter_float_year%3Ato%5D=10000&search%5Bfilter_enum_gearbox%5D%5B0%5D=automatic&search%5Bfilter_enum_gearbox%5D%5B1%5D=cvt&search%5Bfilter_enum_gearbox%5D%5B2%5D=dual-clutch&search%5Bfilter_enum_gearbox%5D%5B3%5D=semi-automatic&search%5Bdist%5D=50&search%5Bcountry%5D='

data_file = Path('data.csv')
if data_file.is_file():
    data = parse(search_link)
    with open('data.csv', 'rb') as file:
        data_file = pickle.load(file)
    if data == data_file:
        print('There are no new cars for sale with your criteria')

    else:
        new_cars = []
        for i in data:
            if i not in data_file:
                new_cars.append(i)
        print(new_cars)
        with open('data.csv', 'wb') as resultFile:
            pickle.dump(data, resultFile)

else:
    data = parse(search_link)
    with open('data.csv', 'wb') as resultFile:
        pickle.dump(data, resultFile)

