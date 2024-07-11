from termcolor import cprint
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self._model = model
        self._engine_power = engine_power
        self._color = color

    def get_model(self):
        return f'Модель: {self._model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self._engine_power}'

    def get_color(self):
        return f'Цвет: {self._color}'

    def print_info(self):
        cprint(self.get_model(), 'blue')
        cprint(self.get_horsepower(), 'blue')
        cprint(self.get_color(), 'blue')
        cprint(f'Владелец: {self.owner}', 'blue')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self._color = new_color
        else:
            cprint(f'Нельзя сменить цвет на {new_color}', 'red')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()