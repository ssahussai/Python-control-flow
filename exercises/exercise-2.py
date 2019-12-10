# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

#Psyedocode: 
    # write a code where you will prompt the user to enter a phrase
    # then calculate the length of the phase or word
    # print the msg back to the user saying "What you entered is xx characters long"

words = None
while words != "quit":
    words = input('Please enter a word or phrase:')
    if words != "quit": # w/o while loop exits but print the msg below 
        print(f'What you have entered is {len(words)} characters long')

    





    