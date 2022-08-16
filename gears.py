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
    # VEXpro or West Coast Products Falcon 500 pinions
    Pinion(8, 20, 0.003, "Falcon 500", "steel", "VEXpro or West Coast Products", "217-6915", diameter=10 / 20),
    Pinion(9, 20, 0.003, "Falcon 500", "steel", "VEXpro or West Coast Products", "217-6916", diameter=10 / 20),
    Pinion(10, 20, 0.003, "Falcon 500", "steel", "VEXpro or West Coast Products", "217-6917", diameter=12 / 20),
    Pinion(11, 20, 0.003, "Falcon 500", "steel", "VEXpro or West Coast Products", "217-6918", diameter=12 / 20),
    Pinion(12, 20, 0.003, "Falcon 500", "steel", "VEXpro or West Coast Products", "217-6919"),
    Pinion(13, 20, 0.003, "Falcon 500", "steel", "VEXpro or West Coast Products", "217-6921", diameter=14 / 20),
    Pinion(14, 20, 0.003, "Falcon 500", "steel", "VEXpro or West Coast Products", "217-6922"),

    # VEXpro or West Coast Products CIM pinions
    Pinion(9, 20, 0.003, "CIM", "steel", "VEXpro or West Coast Products", "217-6335", diameter=10 / 20),
    Pinion(10, 20, 0.003, "CIM", "steel", "VEXpro or West Coast Products", "217-6334", diameter=12 / 20),
    Pinion(11, 20, 0.003, "CIM", "steel", "VEXpro or West Coast Products", "217-3107", diameter=12 / 20),
    Pinion(12, 20, 0.003, "CIM", "steel", "VEXpro or West Coast Products", "217-3099"),
    Pinion(12, 20, 0.003, "CIM", "aluminum", "VEXpro or West Coast Products", "217-2614"),
    Pinion(13, 20, 0.003, "CIM", "steel", "VEXpro or West Coast Products", "217-3416", diameter=14 / 20),
    Pinion(14, 20, 0.003, "CIM", "steel", "VEXpro or West Coast Products", "217-3414"),

    # VEXpro or West Coast Products BAG pinions
    Pinion(6, 20, 0.003, "BAG", "steel", "VEXpro or West Coast Products", "217-6339", diameter=8 / 20),
    Pinion(8, 20, 0.003, "BAG", "steel", "VEXpro or West Coast Products", "217-6368", diameter=10 / 20),

    # VEXpro or West Coast Products 550 pinions
    Pinion(6, 20, 0.003, "550", "steel", "VEXpro or West Coast Products", "217-6333", diameter=8 / 20),
    Pinion(8, 20, 0.003, "550", "steel", "VEXpro or West Coast Products", "217-6367", diameter=10 / 20),

    # VEXpro or West Coast Products 775 pinions
    Pinion(6, 20, 0.003, "775", "steel", "VEXpro or West Coast Products", "217-6285", diameter=8 / 20),
    Pinion(8, 20, 0.003, "775", "steel", "VEXpro or West Coast Products", "217-6362", diameter=10 / 20),

    # REVRobotics Neo pinions
    Pinion(10, 20, 0.003, "Neo", "steel", "REVRobotics", "REV-21-1998", diameter=0.6),
    Pinion(11, 20, 0.003, "Neo", "steel", "REVRobotics", "REV-21-1999", diameter=0.6),
    Pinion(12, 20, 0.003, "Neo", "steel", "REVRobotics", "REV-21-2000"),
    Pinion(13, 20, 0.003, "Neo", "steel", "REVRobotics", "REV-21-2001", diameter=0.7),
    Pinion(14, 20, 0.003, "Neo", "steel", "REVRobotics", "REV-21-2002"),
]




