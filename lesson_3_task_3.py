from adress import Adress

from mailing import Mailing

mailing = Mailing('12345678901234', 100)
to_adress = Adress('654321', 'Krasnoyarsk', 'Lenina', 1, 2)
from_adress = Adress('123456', 'Moscow', 'Kirenskogo', 2, 1)

mailing.say_track()
to_adress.say_to_adress()
from_adress.say_from_adress()
mailing.say_cost()