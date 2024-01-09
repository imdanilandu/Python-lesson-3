from adress import Adress

from mailing import Mailing

mailing = Mailing()

print('Отправление',  mailing.track, 'из', Adress.index[0] + ',', Adress.city[0] + ',', Adress.street[0] + ',', Adress.house[0], '-', Adress.flat[0], 'в', Adress.index[1] + ',', Adress.city[1] + ',', Adress.street[1] + ',', Adress.house[1], '-', Adress.flat[1], '.', 'Стоимость', mailing.cost, 'рублей.')