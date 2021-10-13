class Galleta:
    chocolate = False

    def __init__(self, sabor, olor):
        self.sabor = sabor
        self.olor = olor
        print(f"se creó la {self.sabor} y {self.olor}")

galleta_1 = Galleta("Cai", "Obo")
galleta_2 = Galleta("pei", "uxiono")
galleta_3 = Galleta("pole", "Ray")