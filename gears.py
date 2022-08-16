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
        self.clearance = clearance

        if diameter is None:
            self.diameter = (teeth / dp) + clearance
        else:
            self.diameter = diameter + clearance

        self.motor = motor
        self.material = material
        self.vendor = vendor
        self.sku = sku

    def __repr__(self):
        cnstrct = "Pinion(" + self.teeth + ", " + self.dp + ", " + self.clearance + ", " + self.motor + ", " + self.material + ", " + self.vendor + ", " + self.sku
        if self.diameter is not None:
            cnstrct += ", diameter=" + self.diameter
        cnstrct += ")"
        return cnstrct

bag, cim, falcon500, motor550, motor775, neo = "BAG", "CIM", "Falcon 500", "550", "775", "Neo"
aluminum, steel = "aluminum", "steel"
rev, vexpro, vexprowcp =  "REVRobotics", "VEXpro", "VEXpro or West Coast Products",
hex375, hex5, hex5round = '3/8" Hex', '1/2" Hex', '1/2" Hex Rounded'

pinions = [
    # VEXpro or West Coast Products Falcon 500 pinions
    Pinion(8, 20, 0.003, falcon500, steel, vexprowcp, "217-6915", diameter=10 / 20),
    Pinion(9, 20, 0.003, falcon500, steel, vexprowcp, "217-6916", diameter=10 / 20),
    Pinion(10, 20, 0.003, falcon500, steel, vexprowcp, "217-6917", diameter=12 / 20),
    Pinion(11, 20, 0.003, falcon500, steel, vexprowcp, "217-6918", diameter=12 / 20),
    Pinion(12, 20, 0.003, falcon500, steel, vexprowcp, "217-6919"),
    Pinion(13, 20, 0.003, falcon500, steel, vexprowcp, "217-6921", diameter=14 / 20),
    Pinion(14, 20, 0.003, falcon500, steel, vexprowcp, "217-6922"),

    # VEXpro or West Coast Products CIM pinions
    Pinion(9, 20, 0.003, cim, steel, vexprowcp, "217-6335", diameter=10 / 20),
    Pinion(10, 20, 0.003, cim, steel, vexprowcp, "217-6334", diameter=12 / 20),
    Pinion(11, 20, 0.003, cim, steel, vexprowcp, "217-3107", diameter=12 / 20),
    Pinion(12, 20, 0.003, cim, steel, vexprowcp, "217-3099"),
    Pinion(12, 20, 0.003, cim, aluminum, vexprowcp, "217-2614"),
    Pinion(13, 20, 0.003, cim, steel, vexprowcp, "217-3416", diameter=14 / 20),
    Pinion(14, 20, 0.003, cim, steel, vexprowcp, "217-3414"),

    # VEXpro or West Coast Products BAG pinions
    Pinion(6, 20, 0.003, bag, steel, vexprowcp, "217-6339", diameter=8 / 20),
    Pinion(8, 20, 0.003, bag, steel, vexprowcp, "217-6368", diameter=10 / 20),

    # VEXpro or West Coast Products 550 pinions
    Pinion(6, 20, 0.003, motor550, steel, vexprowcp, "217-6333", diameter=8 / 20),
    Pinion(8, 20, 0.003, motor550, steel, vexprowcp, "217-6367", diameter=10 / 20),

    # VEXpro or West Coast Products 775 pinions
    Pinion(6, 20, 0.003, motor775, steel, vexprowcp, "217-6285", diameter=8 / 20),
    Pinion(8, 20, 0.003, motor775, steel, vexprowcp, "217-6362", diameter=10 / 20),

    # REVRobotics Neo pinions
    Pinion(10, 20, 0.003, neo, steel, rev, "REV-21-1998", diameter=0.6),
    Pinion(11, 20, 0.003, neo, steel, rev, "REV-21-1999", diameter=0.6),
    Pinion(12, 20, 0.003, neo, steel, rev, "REV-21-2000"),
    Pinion(13, 20, 0.003, neo, steel, rev, "REV-21-2001", diameter=0.7),
    Pinion(14, 20, 0.003, neo, steel, rev, "REV-21-2002"),
]

gears = [
    # VEXpro 3/8" hex gears
    Gear(14, 20, 0.003, hex375, 0.498, steel, vexpro, "217-3100"),
    Gear(14, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-2699"),
    Gear(16, 20, 0.003, hex375, 0.498, steel, vexpro, "217-5451"),
    Gear(16, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-5450"),
    Gear(18, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-3208"),
    Gear(20, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-2701"),
    Gear(22, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-5452"),
    Gear(24, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-2703"),
    Gear(26, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-5453"),
    Gear(28, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-5454"),
    Gear(30, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-3210"),
    Gear(32, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-5455"),
    Gear(34, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-3211"),
    Gear(36, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-3213"),
    Gear(38, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-5456"),
    Gear(40, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-2707"),
    Gear(42, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-3215"),
    Gear(44, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-5457"),
    Gear(46, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-5458"),
    Gear(50, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-3571"),
    Gear(52, 20, 0.003, hex375, 0.498, aluminum, vexpro, "217-5459"),

    # VEXpro 1/2" hex steel gears
    Gear(18, 20, 0.003, hex5, 0.498, steel, vexpro, "217-5460"),
    Gear(20, 20, 0.003, hex5, 0.498, steel, vexpro, "217-5461"),
    Gear(22, 20, 0.003, hex5, 0.498, steel, vexpro, "217-5463"),
    Gear(24, 20, 0.003, hex5, 0.498, steel, vexpro, "217-5464"),
    Gear(26, 20, 0.003, hex5, 0.498, steel, vexpro, "217-5466"),
    Gear(28, 20, 0.003, hex5, 0.498, steel, vexpro, "217-5468"),
    Gear(30, 20, 0.003, hex5, 0.498, steel, vexpro, "217-5469"),

    # VEXpro 1/2" hex aluminum gears
    Gear(18, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-3209"),
    Gear(20, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-2702"),
    Gear(22, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5462"),
    Gear(24, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-2704"),
    Gear(26, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5465"),
    Gear(28, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5467"),
    Gear(30, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-2705"),
    Gear(32, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5470"),
    Gear(34, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-2706"),
    Gear(36, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-3214"),
    Gear(38, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5471"),
    Gear(40, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-2708"),
    Gear(42, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-3216"),
    Gear(44, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-2710"),
    Gear(46, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5472"),
    Gear(50, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-3572"),
    Gear(52, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5473"),
    Gear(54, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-3573"),
    Gear(56, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5474"),
    Gear(58, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5475"),
    Gear(60, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-3574"),
    Gear(62, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5476"),
    Gear(64, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-3575"),
    Gear(68, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5477"),
    Gear(72, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-3576"),
    Gear(74, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5478"),
    Gear(76, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5479"),
    Gear(78, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5480"),
    Gear(80, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5481"),
    Gear(82, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-5482"),
    Gear(84, 20, 0.003, hex5, 0.498, aluminum, vexpro, "217-3577"),

    # REVRobotics 1/2" hex gears
    
]


