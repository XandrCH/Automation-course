from address import Address
from mailing import Mailing
to_address = Address('123456','Nevelsk', 'Coast St.', '1', '1')
from_address = Address("654321", 'Volgograd', "Repin's St.", "2", '2')
mailing = Mailing(to_address, from_address, 2000.50, 'abc985f')
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}"
      f"{mailing.from_address.build}-{mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}"
      f"{mailing.to_address.street},{mailing.to_address.build}-{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
