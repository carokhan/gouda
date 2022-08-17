import math


def product(l):
    i = 1
    for e in l:
        i *= e
    return i


# https://docs.python.org/3/library/itertools.html#itertools.product
def combos(*args, desired, pinions, threshold=0.5, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        for pinion in pinions:
            achieved = calcRatio([pinion] + list(prod))
            similarity = (abs(achieved - desired)) / ((achieved + desired) / 2)
            if similarity < threshold:
                yield [pinion] + list(prod)


def calcRatio(pinionGears):
    driving = pinionGears[::2]
    driven = pinionGears[1::2]
    return product([gear.teeth for gear in driven]) / product(
        [gear.teeth for gear in driving]
    )


def calcSize(config, motor):
    total = 0
    for gear in config[1:]:
        total += math.pi * gear.diameter / 2 * gear.height
    match motor:
        case "BAG":
            total += math.pi * 1.590551 / 2 * 3.326772
        case "CIM":
            total += math.pi * 2.52 / 2 * 5.913386
        case "Falcon 500":
            total += math.pi * 2.3622 / 2 * 4.559055
        case "550":
            total += math.pi * 1.377953 / 2 * 2.204724
        case "775":
            total += math.pi * 1.765 / 2 * 3.454567
        case "Neo":
            total += math.pi * 2.322142 / 2 * 3.671260
    return total


class Gear:
    def __init__(self, teeth: int, dp: int, tolerance: float, height: float) -> None:
        self.teeth = teeth
        self.dp = dp
        self.tolerance = tolerance
        self.diameter = (teeth / dp) + tolerance
        self.height = height

    def __eq__(self, compare):
        if (
            self.teeth == compare.teeth
            and self.dp == compare.dp
            and self.tolerance == compare.tolerance
            and self.height == compare.height
        ):
            return True
        else:
            return False

    def __repr__(self):
        return (
            "Gear(teeth="
            + str(self.teeth)
            + ", dp="
            + str(self.dp)
            + ", tolerance="
            + str(self.tolerance)
            + ", height="
            + str(self.height)
            + ")"
        )

    def toProduct(self):
        return [
            product
            for product in products
            if self.teeth == product.teeth
            and self.dp == product.dp
            and self.tolerance == product.tolerance
            and self.diameter == product.diameter
            and self.height == product.height
        ]


# tight fit pinions?
class Pinion:
    def __init__(
        self,
        teeth: int,
        dp: int,
        tolerance: float,
        motor: str,
        material: str,
        vendor: str,
        sku: str,
        diameter=None,
    ) -> None:
        self.teeth = teeth
        self.dp = dp
        self.tolerance = tolerance

        if diameter is None:
            self.diameter = (teeth / dp) + tolerance
        else:
            self.diameter = diameter + tolerance

        self.motor = motor
        self.material = material
        self.vendor = vendor
        self.sku = sku

    def __repr__(self):
        return (
            str(self.teeth)
            + "-Teeth "
            + self.material.capitalize()
            + " "
            + self.motor.capitalize()
            + " Pinion, "
            + str(self.dp)
            + " DP, from "
            + self.vendor
            + " ("
            + self.sku
            + ")"
        )


class Product(Gear):
    def __init__(
        self,
        teeth: int,
        dp: int,
        tolerance: float,
        shaft: str,
        height: float,
        material: str,
        vendor: str,
        sku: str,
    ) -> None:
        self.shaft = shaft
        self.vendor = vendor
        self.material = material
        self.sku = sku
        super().__init__(teeth, dp, tolerance, height)

    def __repr__(self):
        return (
            str(self.teeth)
            + "-Teeth "
            + self.material.capitalize()
            + " Gear, "
            + str(self.dp)
            + " DP, "
            + self.shaft
            + " Bore, from "
            + self.vendor
            + " ("
            + self.sku
            + ")"
        )

    def toGear(self):
        return Gear(self.teeth, self.dp, self.tolerance, self.height)


bag, cim, falcon500, motor550, motor775, neo = (
    "BAG",
    "CIM",
    "Falcon 500",
    "550",
    "775",
    "Neo",
)
aluminum, steel = "aluminum", "steel"
rev, vexpro, vexprowcp, wcp = (
    "REVRobotics",
    "VEXpro",
    "VEXpro or West Coast Products",
    "West Coast Products",
)
hex375, hex5, hex5round, thunder = (
    '3/8" Hex',
    '1/2" Hex',
    '1/2" Hex Rounded',
    '1/2" Thunderhex',
)

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

# thunderhex?
products = [
    # VEXpro or West Coast Products 3/8" hex gears
    Product(14, 20, 0.003, hex375, 0.496, steel, vexprowcp, "217-3100"),
    Product(14, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-2699"),
    Product(16, 20, 0.003, hex375, 0.496, steel, vexprowcp, "217-5451"),
    Product(16, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-5450"),
    Product(18, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-3208"),
    Product(20, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-2701"),
    Product(22, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-5452"),
    Product(24, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-2703"),
    Product(26, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-5453"),
    Product(28, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-5454"),
    Product(30, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-3210"),
    Product(32, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-5455"),
    Product(34, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-3211"),
    Product(36, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-3213"),
    Product(38, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-5456"),
    Product(40, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-2707"),
    Product(42, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-3215"),
    Product(44, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-5457"),
    Product(46, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-5458"),
    Product(50, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-3571"),
    Product(52, 20, 0.003, hex375, 0.498, aluminum, vexprowcp, "217-5459"),
    # VEXpro or West Coast Products 1/2" hex steel gears
    Product(18, 20, 0.003, hex5, 0.498, steel, vexprowcp, "217-5460"),
    Product(20, 20, 0.003, hex5, 0.498, steel, vexprowcp, "217-5461"),
    Product(22, 20, 0.003, hex5, 0.498, steel, vexprowcp, "217-5463"),
    Product(24, 20, 0.003, hex5, 0.498, steel, vexprowcp, "217-5464"),
    Product(26, 20, 0.003, hex5, 0.498, steel, vexprowcp, "217-5466"),
    Product(28, 20, 0.003, hex5, 0.498, steel, vexprowcp, "217-5468"),
    Product(30, 20, 0.003, hex5, 0.498, steel, vexprowcp, "217-5469"),
    # VEXpro or West Coast Products 1/2" hex aluminum gears
    Product(18, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-3209"),
    Product(20, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-2702"),
    Product(22, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5462"),
    Product(24, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-2704"),
    Product(26, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5465"),
    Product(28, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5467"),
    Product(30, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-2705"),
    Product(32, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5470"),
    Product(34, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-2706"),
    Product(36, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-3214"),
    Product(38, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5471"),
    Product(40, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-2708"),
    Product(42, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-3216"),
    Product(44, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-2710"),
    Product(46, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5472"),
    Product(50, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-3572"),
    Product(52, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5473"),
    Product(54, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-3573"),
    Product(56, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5474"),
    Product(58, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5475"),
    Product(60, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-3574"),
    Product(62, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5476"),
    Product(64, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-3575"),
    Product(68, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5477"),
    Product(72, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-3576"),
    Product(74, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5478"),
    Product(76, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5479"),
    Product(78, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5480"),
    Product(80, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5481"),
    Product(82, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-5482"),
    Product(84, 20, 0.003, hex5, 0.498, aluminum, vexprowcp, "217-3577"),
    # REVRobotics 1/2" hex gears
    Product(18, 20, 0.003, hex5, 0.5, steel, rev, "REV-21-1920"),
    Product(20, 20, 0.003, hex5, 0.5, steel, rev, "REV-21-1921"),
    Product(24, 20, 0.003, hex5, 0.5, steel, rev, "REV-21-1923"),
    Product(28, 20, 0.003, hex5, 0.5, steel, rev, "REV-21-1925"),
    Product(30, 20, 0.003, hex5, 0.5, steel, rev, "REV-21-1926"),
    Product(32, 20, 0.003, hex5, 0.5, steel, rev, "REV-21-1927"),
    Product(34, 20, 0.003, hex5, 0.5, steel, rev, "REV-21-1928"),
    Product(36, 20, 0.003, hex5, 0.5, steel, rev, "REV-21-1929"),
    Product(40, 20, 0.003, hex5, 0.5, steel, rev, "REV-21-1931"),
    Product(50, 20, 0.003, hex5, 0.5, steel, rev, "REV-21-1936"),
    Product(52, 20, 0.003, hex5, 0.5, steel, rev, "REV-21-1937"),
    Product(60, 20, 0.003, hex5, 0.5, steel, rev, "REV-21-1941"),
    Product(64, 20, 0.003, hex5, 0.5, steel, rev, "REV-21-1943"),
    Product(68, 20, 0.003, hex5, 0.5, steel, rev, "REV-21-1945"),
    Product(80, 20, 0.003, hex5, 0.5, steel, rev, "REV-21-1951"),
    # REVRobotics 1/2" rounded hex gears
    Product(16, 20, 0.003, hex5round, 0.5, steel, rev, "REV-21-2196"),
    # West Coast Products 3/8" hex gears
    Product(48, 20, 0.003, hex375, 0.498, aluminum, wcp, "WCP-0114"),
    # West Coast Products 1/2" hex gears
    Product(16, 20, 0.003, hex5, 0.498, aluminum, wcp, "WCP-0112"),
    Product(16, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0170"),
    Product(32, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0173"),
    Product(34, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0174"),
    Product(36, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0175"),
    Product(38, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0176"),
    Product(40, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0177"),
    Product(42, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0178"),
    Product(44, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0179"),
    Product(46, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0180"),
    Product(48, 20, 0.003, hex5, 0.498, aluminum, wcp, "WCP-0188"),
    Product(48, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0181"),
    Product(50, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0182"),
    Product(52, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0183"),
    Product(54, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0184"),
    Product(56, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0185"),
    Product(58, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0186"),
    Product(60, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0187"),
    Product(62, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0292"),
    Product(64, 20, 0.003, hex5, 0.498, steel, wcp, "WCP-0293"),
    Product(66, 20, 0.003, hex5, 0.498, aluminum, wcp, "WCP-0171"),
    Product(70, 20, 0.003, hex5, 0.498, aluminum, wcp, "WCP-0172"),
]

sameGears = [product.toGear() for product in products]

gears = []
for gear in sameGears:
    if gear not in gears:
        gears.append(gear)
