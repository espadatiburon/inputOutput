#Name: Harlan Chang
#Assignment: Unit 8

def write_input(filename):
	myFile = open(filename, 'w')
	
	myInput = input("Please enter a number(leave empty when done): ")
	
	while myInput != '':
		myInput = int(myInput)
		myFile.write(str(myInput) + '\n')
		myInput = input("Please enter a number(leave empty when done): ")
	
	myFile.close()
	return 

def read_output(filename):
	min = None #set to none so that the user can input negative variables which isn't possible if set to 0
	max = None #set to none so that the user can input negative variables which isn't possible if set to 0
	avg = 0
	total = 0
	count = 0
	myFile = open(filename, 'r')
	
	for line in myFile:
		amount = line
		print(amount)
		total += int(amount)
		count += 1
		if (min == None) and (max == None): 
		#checks if those varialbes are set otherwise, sets them to the first number in the file
			min = int(amount)
			max = int(amount)
		elif(int(amount) > max):
			max = int(amount)
		elif(int(amount) < min):
			min = int(amount)
	
	avg = float(total/count)
	
	print('The min was: ' + str(min))
	print('The max was : ' + str(max))
	print('The average was : ' + str(avg))
	
	myFile.close()
	return

def main():
	print('Please choose an option:')
	print('1. Save Data')
	print('2. Get Stats')
	print('3. Quit')
	choice = int(input('Choice: '))
	
	while choice != 3:
		if choice == 1:
			name = input('File name: ')
			write_input(name)
		elif choice == 2:
			name = input('File name: ')
			read_output(name)
		else:
			print('That is not a valid option!')
			
		print('\nPlease choose an option:')
		print('1. Save Data')
		print('2. Get Stats')
		print('3. Quit')
		choice = int(input('Choice: '))
		
main()