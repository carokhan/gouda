import motion
import itertools
from pprint import pprint


def product(l):
    i = 1
    for e in l:
        i *= e
    return i


# https://docs.python.org/3/library/itertools.html#itertools.product
def combos(*args, desired, pinions, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        for pinion in pinions:
            achieved = calcReduction([pinion] + list(prod))
            similarity = (abs(achieved - desired)) / ((achieved + desired) / 2)
            if similarity < 0.5:
                yield tuple(prod)


def calcReduction(pinionGears):
    driving = pinionGears[::2]
    driven = pinionGears[1::2]
    return product([gear.teeth for gear in driven]) / product(
        [gear.teeth for gear in driving]
    )


desired = int(input("Desired reduction? "))
maxsize = float(input("\nMax gear diameter? "))

motor = input(
    "\n1) BAG\n2) CIM\n3) Falcon 500\n4) 550-class\n5) 775-class\n6) Neo\nEnter a number to choose a motor: "
)
match motor:
    case "1":
        motor = "BAG"  # max reduction - 84
    case "2":
        motor = "CIM"  # max reduction - 56
    case "3":
        motor = "Falcon 500"  # max reduction - 63
    case "4":
        motor = "550"  # max reduction - 84
    case "5":
        motor = "775"  # max reduction - 84
    case "6":
        motor = "Neo"  # max reduction - 50.4

gears = [gear for gear in motion.gears if gear.diameter - gear.tolerance <= maxsize]
gearTeeth = [gear.teeth for gear in gears]

pinionOptimize = input("\n1 - Yes\n2 - No\nIncrease performance by only using the smallest pinion? ")
match pinionOptimize:
    case "1":
        match motor:
            case "BAG":
                pinions = [motion.Pinion(6, 20, 0.003, motion.bag, motion.steel, motion.vexprowcp, "217-6339", diameter=8 / 20)]
            case "CIM":
                pinions = [motion.Pinion(9, 20, 0.003, motion.cim, motion.steel, motion.vexprowcp, "217-6335", diameter=10 / 20)]
            case "Falcon 500":
                pinions = [motion.Pinion(8, 20, 0.003, motion.falcon500, motion.steel, motion.vexprowcp, "217-6915", diameter=10 / 20)]
            case "550":
                pinions = [motion.Pinion(6, 20, 0.003, motion.motor550, motion.steel, motion.vexprowcp, "217-6333", diameter=8 / 20)]
            case "775":
                pinions = [motion.Pinion(6, 20, 0.003, motion.motor775, motion.steel, motion.vexprowcp, "217-6285", diameter=8 / 20)]
            case "Neo":
                pinions = [motion.Pinion(10, 20, 0.003, motion.neo, motion.steel, motion.rev, "REV-21-1998", diameter=0.6)]
    case "2":
        pinions = [pinion for pinion in motion.pinions if motor == pinion.motor]

pinionTeeth = [pinion.teeth for pinion in pinions]

stages = int(desired / (max(gearTeeth) / min(pinionTeeth)))

stageCount = 1
while stages > max(gearTeeth) / min(gearTeeth):
    stages /= max(gearTeeth) / min(gearTeeth)
    stageCount += 1
print("Stages required:", stageCount + 1)

# if len(pinions) > 2:
#     allPossible = list(
#         combos(gears, desired=desired, pinions=pinions, repeat=stageCount * 2 - 1)
#     )
# else:
allPossible = list(
    combos(gears, desired=desired, pinions=pinions, repeat=stageCount * 2 + 1)
)

reductions = [list(reduction) for reduction in allPossible]
configs = [[pinion] + reduction for reduction in reductions for pinion in pinions]

configReductions = {}
for config in configs:
    reduction = calcReduction(config)
    try:
        if config not in configReductions[reduction]:
            configReductions[reduction].append(config)
    except:
        configReductions[reduction] = [config]