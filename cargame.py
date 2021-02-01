
bool = True
while True:
	gameinp = input(("> ")).lower()
	if gameinp == "start":
		if bool:
			print("Car Started...")
			bool = False
		else:	
			print("Car Already Started...")
	elif gameinp == "stop":
		if not bool:
			print("Car Stop.")
			bool=True
		else:
			print("Car Already Stop.")
	elif gameinp == "quit":
		break
	elif gameinp == "help":
		print('''
start : For Start Car
stop : For Stop Car
help : Help
quit : Quit Game
		 ''')
	else:
		print("Please Enter Correct Command")