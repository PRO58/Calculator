from Calculater import Calculater

def Main():
	options = print("""
		1) Addition
		2) Subtraction
		3) Multiplication
		4) Divsion


		""")

	Options()

def getNumber():
	try:
		getNum1 = float(input("Enter first number: "))
		getNum2 = float(input("Enter second number: "))
		return getNum1, getNum2
	except ValueError:
		print("Please Enter a number.")
		getNumber()
def Options():
	try:
		options = int(input("Enter an option: "))
		Calculation(options)
	except ValueError:
		print("Please enter a number")
		print("---------------------------")
		Main()
	if options > 4:
		print("Invalid input\n\n\n")
		print("-----z----------------------")
		Main()

	if options < 1:
		print("Invalid input\n\n\n")
		print("---------------------------")
		Main()

def Calculation(options):
	num1, num2 = getNumber()
	calculator = Calculater(num1, num2)

	if options == 1:
		print(calculator.Addition())

	elif options == 2:
		print(calculator.Subtraction())
	
	elif options == 3:
		print(calculator.Multiplication())
		
	elif options == 4:
		try:
			print(calculator.Division())
		except ZeroDivisionError:
			print("Cannot divide by zero!")
			getNumber()


if __name__ == "__main__":
	Main()