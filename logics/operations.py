METRS_IN_MILLIMETERS = 0.001  # метров в миллиметре
HORISONT_PLOTNOST = 35
VES_UPAKOVKI = 15


class Calculators:
    def __init__(self, sqr, width):
        self.sqr = sqr  # метры
        self.width = width  # миллиметры

    @property
    def volume_calculate(self) -> float:
        return self.sqr * self.width * METRS_IN_MILLIMETERS

    @property
    def ves_calculate(self) -> float:
        return self.volume_calculate * HORISONT_PLOTNOST

    @property
    def packages_count_calculate(self) -> float:
        return self.ves_calculate / VES_UPAKOVKI

    @property
    def ecovata_price_calculate(self) -> float:
        return self.packages_count_calculate * VES_UPAKOVKI
