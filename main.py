import motion 

reduction = int(input("Desired reduction? "))
maxsize = float(input("\nMax gear diameter? "))

motorq = {"1": "BAG", "2": "CIM", "3": "Falcon 500", "4": "550", "5": "775", "6": "Neo"}

motor = motorq[input("\n1) BAG\n2) CIM\n3) Falcon 500\n4) 550-class\n5) 775-class\n6) Neo\nEnter a number to choose a motor: ")]

# match motor:
#     case "1":
#         motor = "BAG"
#     case "2":
#         motor = "CIM"
#     case "3":
#         motor = "Falcon 500"
#     case "4":
#         motor = "550"
#     case "5":
#         motor = "775"
#     case "6":
#         motor = "Neo"

gears = [gear for gear in motion.gears if gear.diameter - gear.tolerance <= maxsize]
gearTeeth = [gear.teeth for gear in gears]

pinions = [pinion for pinion in motion.pinions if motor == pinion.motor]
pinionTeeth = [pinion.teeth for pinion in pinions]

stages = int(reduction / (max(gearTeeth) / min(pinionTeeth)))

stageCount = 1
while stages > max(gearTeeth) / min(gearTeeth):
    stages /= max(gearTeeth) / min(gearTeeth)
    stageCount += 1
    
print(stageCount)