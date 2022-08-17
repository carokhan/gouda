from re import sub
import motion
from pprint import pprint
import subprocess
import os
import pyfiglet

os.environ["GUM_INPUT_CURSOR_FOREGROUND"] = "#FFEA00"
os.environ["GUM_INPUT_PROMPT_FOREGROUND"] = "#87CEEB"
os.environ["GUM_CHOOSE_CURSOR_FOREGROUND"] = "#87CEEB"
os.environ["GUM_CONFIRM_PROMPT_FOREGROUND"] = "#87CEEB"
os.environ["GUM_CONFIRM_SELECTED_FOREGROUND"] = "#FFEA00"
os.environ["GUM_CONFIRM_UNSELECTED_FOREGROUND"] = "#E1C16E"
os.environ["FOREGROUND"] = "39"
os.environ["BORDER_FOREGROUND"] = "39"
os.environ["BORDER_BACKGROUND"] = "17"

gumInstalled = True

try:
    subprocess.run(["gum", "style", "--background=17", "--border=rounded", "--align=center", "--width=53", "--height=1", "--bold", 'Welcome to'])
    gouda = pyfiglet.Figlet(font="starwars")
    gouda = gouda.renderText("GOUDA")
    print("\033[1;33m" + gouda[:-1])
    subprocess.run(["gum", "style", "--background=17", "--border=rounded", "--align=center", "--width=53", "--height=1", "--bold", 'The Gearbox Optimization Utility for Design Automation'])

except FileNotFoundError:
    gumInstalled = False
    print("Welcome to")

if gumInstalled:
    desired = int(subprocess.run(["gum", "input", "--prompt=Enter the desired gear ratio: ", "--placeholder=ie, if you wanted 90:1, type 90 "], stdout=subprocess.PIPE, text=True).stdout.strip().split(" ")[-1])
    subprocess.run(["gum", "style", "Gear ratio of " + str(desired) + ":1 selected!\n"])

    maxsize = int(subprocess.run(["gum", "input", "--prompt=Enter the max gear diameter: ", "--placeholder=(in inches)"], stdout=subprocess.PIPE, text=True).stdout.strip().split(" ")[-1])
    subprocess.run(["gum", "style", "Set maximum gear diameter of: " + str(maxsize) + " inches"])

    subprocess.run(["gum", "style", "\nChoose a motor:"])
    motor = subprocess.run(
        ["gum", "choose", "BAG", "CIM", "Falcon 500", "550", "775", "Neo"],
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    subprocess.run(["gum", "style", motor])

    subprocess.run(["gum", "style", "\nAccount for size in reduction recommendations?"])
    sizeWeight = subprocess.run(
        ["gum", "choose", "Yes", "No"], stdout=subprocess.PIPE, text=True
    ).stdout.strip()
    subprocess.run(["gum", "style", sizeWeight + "\n"])
    
    results = int(subprocess.run(["gum", "input", "--prompt=How many results would you like? "], stdout=subprocess.PIPE, text=True).stdout.strip().split(" ")[-1])
    subprocess.run(["gum", "style", str(results) + " results selected!"])
    
    subprocess.run(["gum", "style", "\nIncrease performance by only using the smallest pinion?"])
    pinionOptimize = subprocess.run(
        ["gum", "choose", "Yes", "No"], stdout=subprocess.PIPE, text=True
    ).stdout.strip()
    subprocess.run(["gum", "style", pinionOptimize])

    confirm = subprocess.run(["gum", "confirm", "Confirm input?"], stdout=subprocess.PIPE, text=True)
    
    if confirm.returncode != 0:
        subprocess.run(["gum", "style", "--foreground=160", "Exiting..."])
        exit(0)

else:
    desired = int(input("Enter desired ratio: "))

    maxsize = float(input("\nMax gear diameter? "))

    motor = input(
        "\n1) BAG\n2) CIM\n3) Falcon 500\n4) 550-class\n5) 775-class\n6) Neo\nEnter a number to choose a motor: "
    )
    match motor:
        case "1":
            motor = "BAG"  # max 2-stage reduction - 84
        case "2":
            motor = "CIM"  # max 2-stage reduction - 56
        case "3":
            motor = "Falcon 500"  # max 2-stage reduction - 63
        case "4":
            motor = "550"  # max 2-stage reduction - 84
        case "5":
            motor = "775"  # max 2-stage reduction - 84
        case "6":
            motor = "Neo"  # max 2-stage reduction - 50.4
        case "_":
            print("Invalid input.")
            exit(0)

    sizeWeight = int(
        input(("\n1) No\n2) Yes\nAccount for size in reduction recommendations? "))
    )

    results = float(input("How many results would you like? "))

    pinionOptimize = input(
        "\n1) Yes\n2) No\nIncrease performance by only using the smallest pinion? "
    )

gears = [gear for gear in motion.gears if gear.diameter - gear.tolerance <= maxsize]
gearTeeth = [gear.teeth for gear in gears]

if int(results) >= 1:
    results = int(results)   

match pinionOptimize:
    case "Yes":
        match motor:
            case "BAG":
                pinions = [
                    motion.Pinion(
                        6,
                        20,
                        0.003,
                        motion.bag,
                        motion.steel,
                        motion.vexprowcp,
                        "217-6339",
                        diameter=8 / 20,
                    )
                ]
            case "CIM":
                pinions = [
                    motion.Pinion(
                        9,
                        20,
                        0.003,
                        motion.cim,
                        motion.steel,
                        motion.vexprowcp,
                        "217-6335",
                        diameter=10 / 20,
                    )
                ]
            case "Falcon 500":
                pinions = [
                    motion.Pinion(
                        8,
                        20,
                        0.003,
                        motion.falcon500,
                        motion.steel,
                        motion.vexprowcp,
                        "217-6915",
                        diameter=10 / 20,
                    )
                ]
            case "550":
                pinions = [
                    motion.Pinion(
                        6,
                        20,
                        0.003,
                        motion.motor550,
                        motion.steel,
                        motion.vexprowcp,
                        "217-6333",
                        diameter=8 / 20,
                    )
                ]
            case "775":
                pinions = [
                    motion.Pinion(
                        6,
                        20,
                        0.003,
                        motion.motor775,
                        motion.steel,
                        motion.vexprowcp,
                        "217-6285",
                        diameter=8 / 20,
                    )
                ]
            case "Neo":
                pinions = [
                    motion.Pinion(
                        10,
                        20,
                        0.003,
                        motion.neo,
                        motion.steel,
                        motion.rev,
                        "REV-21-1998",
                        diameter=0.6,
                    )
                ]
    case "1":
        match motor:
            case "BAG":
                pinions = [
                    motion.Pinion(
                        6,
                        20,
                        0.003,
                        motion.bag,
                        motion.steel,
                        motion.vexprowcp,
                        "217-6339",
                        diameter=8 / 20,
                    )
                ]
            case "CIM":
                pinions = [
                    motion.Pinion(
                        9,
                        20,
                        0.003,
                        motion.cim,
                        motion.steel,
                        motion.vexprowcp,
                        "217-6335",
                        diameter=10 / 20,
                    )
                ]
            case "Falcon 500":
                pinions = [
                    motion.Pinion(
                        8,
                        20,
                        0.003,
                        motion.falcon500,
                        motion.steel,
                        motion.vexprowcp,
                        "217-6915",
                        diameter=10 / 20,
                    )
                ]
            case "550":
                pinions = [
                    motion.Pinion(
                        6,
                        20,
                        0.003,
                        motion.motor550,
                        motion.steel,
                        motion.vexprowcp,
                        "217-6333",
                        diameter=8 / 20,
                    )
                ]
            case "775":
                pinions = [
                    motion.Pinion(
                        6,
                        20,
                        0.003,
                        motion.motor775,
                        motion.steel,
                        motion.vexprowcp,
                        "217-6285",
                        diameter=8 / 20,
                    )
                ]
            case "Neo":
                pinions = [
                    motion.Pinion(
                        10,
                        20,
                        0.003,
                        motion.neo,
                        motion.steel,
                        motion.rev,
                        "REV-21-1998",
                        diameter=0.6,
                    )
                ]
    case "No":
        pinions = [pinion for pinion in motion.pinions if motor == pinion.motor]
    case "2":
        pinions = [pinion for pinion in motion.pinions if motor == pinion.motor]
    case "_":
        if gumInstalled:
            subprocess.run(["gum", "style", "--foreground=160", "Invalid input, exiting..."])
        else:
            print("Invalid input, exiting...")
        exit(0)

pinionTeeth = [pinion.teeth for pinion in pinions]

stages = int(desired / (max(gearTeeth) / min(pinionTeeth)))

stageCount = 1
while stages > max(gearTeeth) / min(gearTeeth):
    stages /= max(gearTeeth) / min(gearTeeth)
    stageCount += 1

if gumInstalled:
    subprocess.run(["gum", "style", "\nStages required: " + str(stageCount + 1)])
else:
    print("\nStages required:", stageCount + 1)

if type(results) == type(1086):
    reductions = list(
        motion.combos(
            gears, desired=desired, pinions=pinions, repeat=stageCount * 2 + 1
        )
    )
else:
    reductions = list(
        motion.combos(
            gears,
            desired=desired,
            pinions=pinions,
            threshold=results,
            repeat=stageCount * 2 + 1,
        )
    )

reductionRatios = {}
for reduction in reductions:
    ratio = motion.calcRatio(reduction)
    try:
        if reduction not in reductionRatios[ratio]:
            reductionRatios[ratio].append(reduction)
    except:
        reductionRatios[ratio] = [reduction]

reductionScore = {}
for reduction in reductions:
    size = motion.calcSize(reduction, motor)
    ratio = motion.calcRatio(reduction)
    similarity = abs(100 - ((abs(ratio - desired)) / ((ratio + desired) / 2)))

    # if sizeWeight == 2:
    #     score = similarity / size
    # else:
    #     score = similarity

    match sizeWeight:
        case "Yes":
            score = similarity / size
        case "No":
            score = similarity

    try:
        if reduction not in reductionScore[score]:
            reductionScore[score]["reductions"].append(reduction)
    except:
        reductionScore[score] = {}
        reductionScore[score]["reductions"] = [[reduction]]
        reductionScore[score]["size"] = size
        reductionScore[score]["ratio"] = ratio
        reductionScore[score]["similarity"] = similarity

highScores = sorted(list(reductionScore.keys()), reverse=True)

if gumInstalled:
    subprocess.run(["gum", "style", "\nResults:"])
else:
    print("\nResults:")

if type(results) == type(1086):
    for i in range(results):
        if gumInstalled:
            subprocess.run(["gum", "style", "--foreground=255", "#"
                + str(i)
                + ", "
                + str(round(highScores[i], 4))
                + ", size: "
                + str(round(reductionScore[highScores[i]]["size"], 4))
                + " cubic inches, ratio: "
                + str(round(reductionScore[highScores[i]]["ratio"], 4))
                + ":1"])
        else:
            print(
                "#"
                + str(i)
                + ", "
                + str(round(highScores[i], 4))
                + ", size: "
                + str(round(reductionScore[highScores[i]]["size"], 4))
                + " cubic inches, ratio: "
                + str(round(reductionScore[highScores[i]]["ratio"], 4))
                + ":1"
            )
else:
    i = 0
    for score in highScores:
        if score < results * 100:
            break
        if gumInstalled:
            subprocess.run(["gum", "style", "--foreground=255", "#"
                + str(i)
                + ", "
                + str(round(score, 4))
                + ", size: "
                + str(round(reductionScore[score]["size"], 4))
                + " cubic inches, ratio: "
                + str(round(reductionScore[score]["ratio"], 4))
                + ":1"])
        else:
            print(
                "#"
                + str(i)
                + ", "
                + str(round(score, 4))
                + ", size: "
                + str(round(reductionScore[score]["size"], 4))
                + " cubic inches, ratio: "
                + str(round(reductionScore[score]["ratio"], 4))
                + ":1"
            )
        i += 1

while True:
    if gumInstalled:
        choice = subprocess.run(["gum", "input", "--prompt=Enter a number for more, or type EXIT: "], stdout=subprocess.PIPE, text=True).stdout.strip().split(" ")[-1]
    else:
        choice = input(
            "\nEnter the number for the reduction you would like more details on, or type EXIT to exit: "
        )
    try:
        for reduction in reductionScore[highScores[int(choice)]]["reductions"]:
            products = [gear.toProduct() for gear in reduction[1::]]
            print("\n")
            pprint([reduction[0]] + products)
            print("\n")
    except:
        if gumInstalled:
            subprocess.run(["gum", "style", "--foreground=160", "Exiting..."])
        else:
            print("Exiting...")
        exit(0)
