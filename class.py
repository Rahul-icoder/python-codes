class India:
	population = 0
	def __init__(self,name,age):
		India.population += 1
		self.name = name;
		self.age = age
	@classmethod
	def get_population(india_class):
		return india_class.population


rahul = India('rahul',21)
rahul.population = 3 # not write way static variable 
total = rahul.get_population()
print(total)
vicky = India('vicky',19)
total = rahul.get_population()
print(total)