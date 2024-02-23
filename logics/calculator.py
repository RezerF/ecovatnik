from common.constants import Common, Plotnost, WorksPrices, MaterialsToSqrMetr


class Calculators:
    def __init__(self, sqr, width):
        self.sqr = sqr  # метры
        self.width = width  # миллиметры

    @property
    def volume_calculate(self) -> float:
        return round(self.sqr * self.width * Common.METRS_IN_MILLIMETERS, 1)

    @property
    def ves_calculate(self) -> float:
        return round(self.volume_calculate * Plotnost.VERTICAL, 1)

    @property
    def packages_count_calculate(self) -> float:
        return round(self.ves_calculate / Common.VES_UPAKOVKI, 1)

    def ecovata_price_calculate(self, package_price) -> float:
        return round(self.packages_count_calculate * package_price, 1)

    def cost_work_calculate(self, cost_work_per_kg) -> float:
        return round(self.ves_calculate * cost_work_per_kg, 1)

    def izospan_am_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.IZOSPAN_AM, 1)

    def izospan_am_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.IZOSPAN_AM, 1)

    def izospan_am_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.IZOSPAN_AM, 1)

    def setka_arm_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.SETKA_ARM_25x25, 1)

    def brus_50_50_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.BRUS_SS_50x50x3000, 1)

    def brus_20_40_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.BRUS_SS_20x40x3000, 1)

    def samorez_potainoi_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.SAMOREZ_POTAINOI_40x4, 1)

    def samorez_clop_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.SAMOREZ_CLOP, 1)

    def bolt_san_tech_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.BOLT_SAN_TECH_8x100, 1)

    def kronshtein_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.KRONSHTEIN, 1)

    def skobi_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.SKOBI_53_8, 1)

    def skotch_isospan_kl_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.SKOTCH_IZOSPAN_KL, 1)

    def skotch_isospan_lk_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.SKOTCH_IZOSPAN_LK, 1)

    def dubel_calculate(self) -> float:
        return round(self.sqr * MaterialsToSqrMetr.DUBEL_10x80, 1)

    def get_materials_data(self):
        return {
            'izospan_am': self.izospan_am_calculate(),
            'setka_arm': self.setka_arm_calculate(),
            'brus_50x50': self.brus_50_50_calculate(),
            'brus_20x40': self.brus_20_40_calculate(),
            'samorez_potainoi': self.samorez_potainoi_calculate(),
            'samorez_clop': self.samorez_clop_calculate(),
            'bolt_san_tech': self.bolt_san_tech_calculate(),
            'kronshtein': self.bolt_san_tech_calculate(),
            'skobi': self.skobi_calculate(),
            'skotch_isospan_kl': self.skotch_isospan_kl_calculate(),
            'skotch_isospan_lk': self.skotch_isospan_lk_calculate(),
            'dubel': self.dubel_calculate(),
        }

    def obreshetki_montaj_po_derevu_calculate(self) -> float:
        return round(self.sqr * WorksPrices.OBRESHETKI_MONTAJ_PO_DEREVU, 1)

    def obreshetki_montaj_po_kirpichu_calculate(self) -> float:
        return round(self.sqr * WorksPrices.OBRESHETKI_MONTAJ_PO_KIRPICHU, 1)

    def gidro_paroisol_montaj_calculate(self) -> float:
        return round(self.sqr * WorksPrices.GIDRO_PAROISOL_MONTAJ, 1)

    def setka_arm_montaj_calculate(self) -> float:
        return round(self.sqr * WorksPrices.SETKA_ARMIRUU_MONTAJ, 1)

    def kontr_obreshetka_montaj_calculate(self) -> float:
        return round(self.sqr * WorksPrices.KONTR_OBRESHETKA_MONTAJ, 1)

    def get_works_data(self):
        return {
            'obreshetki_montaj_po_derevu': self.obreshetki_montaj_po_derevu_calculate(),
            'obreshetki_montaj_po_kirpichu': self.obreshetki_montaj_po_kirpichu_calculate(),
            'gidro_paroisol_montaj': self.gidro_paroisol_montaj_calculate(),
            "setka_armiruu_montaj": self.setka_arm_montaj_calculate(),
            "kontr_obreshetka_montaj": self.kontr_obreshetka_montaj_calculate()
        }
