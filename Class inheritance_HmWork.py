class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return "Лошадиные силы не определены"

class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.price = 1500000  # У Nissan цена выше

    def horse_powers(self):
        return "Nissan обычно имеет около 150-200 лошадиных сил"

class Kia(Car):
    def __init__(self):
        super().__init__()
        self.price = 800000  # У Kia цена ниже

    def horse_powers(self):
        return "Kia обычно имеет около 100-150 лошадиных сил"

nissan = Nissan()
print(f"Цена Nissan: {nissan.price}, лошадиные силы: {nissan.horse_powers()}")

kia = Kia()
print(f"Цена Kia: {kia.price}, лошадиные силы: {kia.horse_powers()}")