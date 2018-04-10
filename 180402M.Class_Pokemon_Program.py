#Name- 180402M.Class_Pokemon_Program.py

class pokemon(object)
	def __init__(self, name, hp):
		self.hp = hp
		self.name = name
		if self.name == 'Charizard' :
			{
				'ember': random.randint(10,50),
				'flamethrower': random.randint(30,80),
				'splash': random.randint(0,1)
				'roar of time' random.randint(100,100)
			}
		elif self.name == 'Luxray'
			{
				'thunder': random.randint(60,100),
				"zap cannon": random.randint(0,0),
				"Thunder Fang": 65,
				"Crunch": 80
			}

def battle(self, enemy):
	for x in self.type:
		print(x)

		print("%s's turn."%(self.name))


		attack_choice = input('What will Charizard do?')

		chosen_attack = self.name[attack_choice]

		if(self.hp > 1):
			enemy.hp = enemy.hp - chosen_attack
			if(enemy.hp > 1):
				return enemy.battle(self)


	Charizard = pokemon('Charizard', 372)
	Luxray = pokemon('Luxray', 368)


















