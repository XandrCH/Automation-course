from smartphone import Smartphone
catalog = []

phone1 = Smartphone('Apple', 'IPhone 13', '+79247778877')
phone2 = Smartphone('Samsung', 'Galaxy S20', '+79246669988')
phone3 = Smartphone('Xiaomi', 'MI 5', '+79245554411')
phone4 = Smartphone('Google', 'Pixel 5', '+79243332255')
phone5 = Smartphone('Apple', 'IPhone 15', '+79245552288')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f'{phone.brand} - {phone.model} {phone.number}')
    