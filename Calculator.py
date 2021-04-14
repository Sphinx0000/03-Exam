def calc(x,y, ops):

	if ops not in "+-/*%":
		return 'Choose operator: "+, -, *, /, %"!'


	if ops == "+":
		return(str(x) + "" + ops + "" + str(y) + "=" + str(x + y))
	if ops == "-":
		return(str(x) + "" + ops + "" + str(y) + "=" + str(x-y))
	if ops == "*":
		return(str(x) + "" + ops + "" + str(y) + "=" + str(x*y))
	if ops == "/":
		return(str(x) + "" + ops + "" + str(y) + "=" + str(x/y))
	if ops == "%":
		return(str(x) + "" + ops + "" + str(y) + "=" + str(x%y))

while True:


	    x = int(input("Enter First Number: "))
	    y = int(input("Enter Second Number: "))
	    ops = input("Choose between +,-,*,/,% : ")

	    print(calc(x,y,ops))