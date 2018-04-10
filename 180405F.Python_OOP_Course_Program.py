#Name- 180405F.Python_OOP_Course_Program.py
class Car(object):
	def __init__(self, carType, fare):
		self.carType = carType
		self.fare = fare

	def carRentalSystem(self):
		carWanted = input("What kind of car do you want?")
		if(carWanted == "Hatchback"):
			daysNeeded = input("Okay, How many days do you need the car?")
			print("Okay, the price is [%d*%d]"%(daysNeeded, self.fareHatchback))
		elif (carWanted == "Sedan"):
			daysNeeded = input("Okay, How many days do you need the car?")
			print("Okay, the price is [%d*%d]"%(daysNeeded, self.fareSedan))
		else:
			carWanted == "SUV"
			daysNeeded = input("Okay, How many days do you need the car?")
			print("Okay, the price is [%d*%d]"%(daysNeeded, self.fareSUV))

Hatchback = Car('Hatchback', 50)
Sedan = Car('Sedan', 50)
SUV = Car('SUV', 100)
Car.carRentalSystem()