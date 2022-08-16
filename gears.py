from turtle import clear


class Gear:
    def __init__(self, teeth: int, dp: int, clearance: float, shaftType: str, height: float, material: str, vendor: str, sku: str) -> None:
        self.teeth = teeth
        self.dp = dp
        self.diameter = (teeth / dp) + clearance
        self.shaftType = shaftType
        self.height = height
        self.material = material
        self.vendor = vendor
        self.sku = sku

# tight fit pinions?
class Pinion:
    def __init__(self, teeth: int, dp: int, clearance: float, motor: str, material: str, vendor: str, sku: str, diameter=None) -> None:
        self.teeth = teeth
        self.dp = dp

        if diameter is None:
            self.diameter = (teeth / dp) + clearance
        else:
            self.diameter = diameter + clearance

        self.motor = motor
        self.material = material
        self.vendor = vendor
        self.sku = sku
        

pinions = [
    # VEXpro Falcon 500 pinions
    Pinion(8, 20, 0.003, "Falcon 500", "steel", "VEXpro", "217-6915", diameter=10 / 20),
    Pinion(9, 20, 0.003, "Falcon 500", "steel", "VEXpro", "217-6916", diameter=10 / 20),
    Pinion(10, 20, 0.003, "Falcon 500", "steel", "VEXpro", "217-6917", diameter=12 / 20),
    Pinion(11, 20, 0.003, "Falcon 500", "steel", "VEXpro", "217-6918", diameter=12 / 20),
    Pinion(12, 20, 0.003, "Falcon 500", "steel", "VEXpro", "217-6919"),
    Pinion(13, 20, 0.003, "Falcon 500", "steel", "VEXpro", "217-6921", diameter=14 / 20),
    Pinion(14, 20, 0.003, "Falcon 500", "steel", "VEXpro", "217-6922"),

    # VEXpro CIM pinions
    Pinion(9, 20, 0.003, "CIM", "steel", "VEXpro", "217-6335", diameter=10 / 20),
    Pinion(10, 20, 0.003, "CIM", "steel", "VEXpro", "217-6334", diameter=12 / 20),
    Pinion(11, 20, 0.003, "CIM", "steel", "VEXpro", "217-3107", diameter=12 / 20),
    Pinion(12, 20, 0.003, "CIM", "steel", "VEXpro", "217-3099"),
    Pinion(12, 20, 0.003, "CIM", "aluminum", "VEXpro", "217-2614"),
    Pinion(13, 20, 0.003, "CIM", "steel", "VEXpro", "217-3416", diameter=14 / 20),
    Pinion(14, 20, 0.003, "CIM", "steel", "VEXpro", "217-3414"),

    # VEXpro BAG pinions
    Pinion(6, 20, 0.003, "BAG", "steel", "VEXpro", "217-6339", diameter=8 / 20),
    Pinion(8, 20, 0.003, "BAG", "steel", "VEXpro", "217-6368", diameter=10 / 20),
]




