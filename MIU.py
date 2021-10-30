#!/usr/bin/env python3
#welcome
print ("Welcome to the world of the MIU formal system")
print ("You get one free axiom: MI")
state = ["31"]
#allow the user to go through with numbers or letters
print ("would you like to proceed typographically or numerically? (t/n)")
format = input()
#show the rules
print ("\nThe rules are as follows:")
print ("Rule 1: MxI => MxIU")
print ("Rule 2: Mx => Mxx")
print ("Rule 3: MxIIIy => MxUy")
print ("Rule 4: MxUUy => Mxy\n")

if format == "t":
	print ("your starting point is "+str(state[len(state)-1]).replace("3","M").replace("1","I").replace("0","U")+"\n")
else:
	print ("your starting point is "+str(state[len(state)-1])+"\n")

command = ""
while command != "q":
	command = input("what next? Type 'o' to list all availible options: ")
	#list all options
	if command == "o":
		print ("1: MxI => MxIU")
		print ("2: Mx => Mxx")
		print ("3: MxIIIy => MxUy")
		print ("4: MxUUy => Mxy")
		print ("o: show all options")
		print ("p: list possible rules in the current state")
		print ("u: undo last action")
		print ("q: quit the game, print the current Godel number and bottom line\n")
	#list all possible rules from the current state
	elif command == "p":
		print ("possible rules from here:")
		if int(str(state[len(state)-1])[len(str(state[len(state)-1]))-1]) == 1:
			print ("1: MxI => MxIU")
		print ("2: Mx => Mxx")
		if str(state[len(state)-1]).find("111") != -1:
			print ("3: MxIIIy => MxUy")
		if str(state[len(state)-1]).find("00") != -1:
			print ("4: MxUUy => Mxy")
	#undo the last command
	elif command == "u":
		if len(state)-1 > 0:
			state = state[:-1]
		else:
			print ("can't undo")
	#perform rule 1
	elif command == "1":
		if int(str(state[len(state)-1])[len(str(state[len(state)-1]))-1]) == 1:
			state.append(int(state[len(state)-1]) * 10)
		else: print ("can't do that")
	#perform rule 2
	elif command == "2":
		state.append(str(state[len(state)-1]) + str(state[len(state)-1])[1:len(str(state[len(state)-1]))])
	#perform rule 3
	elif command == "3":
		if str(state[len(state)-1]).find("111") == -1:
			print ("can't do that")
		else:
			index=str(state[len(state)-1]).find("111",0,len(str(state[len(state)-1])))
			print ("where in the string would you like to perform this action?")
			while str(state[len(state)-1]).find("111",index,len(str(state[len(state)-1]))) != -1:
				print (str(state[len(state)-1]).find("111",index,len(str(state[len(state)-1]))))
				index=str(state[len(state)-1]).find("111",index,len(str(state[len(state)-1])))+1
			command = input("position:")
			if str(state[len(state)-1]).find("111",int(command),(int(command)+3)) != -1:
				state.append(str(state[len(state)-1])[0:int(command)] + "0" + str(state[len(state)-1])[int(command)+3:len(str(state[len(state)-1]))])
			else:
				print ("can't do that")
	#perform rule 4
	elif command == "4":
		if str(state[len(state)-1]).find("00") == -1:
			print ("can't do that")
		else:
			index=str(state[len(state)-1]).find("00",0,len(str(state[len(state)-1])))
			print ("where in the string would you like to perform this action?")
			while (str(state[len(state)-1]).find("00",index,len(str(state[len(state)-1]))) != -1):
				print (str(state[len(state)-1]).find("00",index,len(str(state[len(state)-1]))))
				index=str(state[len(state)-1]).find("00",index,len(str(state[len(state)-1])))+1
			command = input("position:")
			if str(state[len(state)-1]).find("00",int(command),int(command)+2) != -1:
				state.append(str(state[len(state)-1])[0:int(command)] + str(state[len(state)-1])[int(command)+2:len(str(state[len(state)-1]))])
			else: print ("can't do that")
	else:
		print ("not a valid command\n")
	if format == "t":
		print ("current string: " +str(state[len(state)-1]).replace("3","M").replace("1","I").replace("0","U") + "\n")
	else:
		print ("current string: " + str(state[len(state)-1]) + "\n")
if format == "t":
	print ("Thanks for trying, final string: " +str(state[len(state)-1]).replace("3","M").replace("1","I").replace("0","U") + "\n")
else:
	print ("Thanks for trying, final string: " + str(state[len(state)-1]) + "\n")

