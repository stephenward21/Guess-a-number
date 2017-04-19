import random
secret_number = random.randint(1,10)
the_number = True
number_of_guesses = 5


while (number_of_guesses > 0) and (the_number == True):
	the_guessed_number = raw_input("Guess a number between 1 and 10.")
	if(int(the_guessed_number) == secret_number):	
		print "Yes! You win!"
		play_again = raw_input("Would you like to play again (Y / N)?")
		if (play_again == "Y"):
			the_number = True
			number_of_guesses = 5
		else: 
			the_number = False
			print "Bye!"

	if (int(the_guessed_number) > secret_number):
		print "Your guess is too high"
		number_of_guesses = number_of_guesses - 1
		print "You have " + str(number_of_guesses)  + " guesses left"

	if (int(the_guessed_number) < secret_number):
		print "Your guess is too low"
		number_of_guesses = number_of_guesses - 1
		print "You have " + str(number_of_guesses)+ " guesses left"

	if (number_of_guesses == 0):
		print "You ran out of guesses!"



	



		




	

