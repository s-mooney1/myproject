print("welcome to guess the number")
number = 10
guess =int(raw_input("Enter a guess"));

if guess == number:

	print "guess is correct"

elif guess < number:

	print "guess is too low"

elif guess > number:

	print "guess is too high"

else: 
	print "wrong"



