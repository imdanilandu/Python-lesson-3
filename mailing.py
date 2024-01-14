class Mailing:

    def __init__(self, track, cost):
        self.cost = cost
        self.track = track

    def say_track(self):
        print('Отправление', self.track, 'из')

    def say_cost(self):
        print('Стоимость', self.cost, 'рублей.')