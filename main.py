import motion 

reduction = int(input("Desired reduction? "))
maxsize = float(input("\nMax gear diameter? "))
motor = input("\n1) BAG\n2) CIM\n3) Falcon 500\n4) 550-class\n5) 775-class\n6) Neo\nEnter a number to choose a motor: ")

gears = [gear for gear in motion.gears if gear.diameter - gear.tolerance <= maxsize]
gearTeeth = [gear.teeth for gear in gears]

pinions = [pinion for pinion in motion.pinions if motor == pinion.motor]
pinionTeeth = [pinion.teeth for pinion in pinions]

stages = int(reduction / (max(gearTeeth) / min(pinionTeeth)))
print(stages)