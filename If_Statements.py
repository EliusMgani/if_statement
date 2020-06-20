# if statement
grade = 70
if grade>= 65:
	print('passing grade')
print()

# if else statement
grade = 64
if grade>= 65:
	print('Passing grade')
else:
	print('Failling grade')
print()

# else if statement
if grade>=81:
	print('A grade')
elif grade>=61:
	print('B grade')
elif grade>=41:
	print('C grade')
elif grade>=21:
	print('D grade')
else:
	print('Failling grade')
print()

# nested if statement
a = 11
if a >= 20:
	print('The condition is True')
else:
	if a>=15:
		print('Checking Second Value')
	else:
		print('All Conditions are False')
print()