from Words import get_word

def get_letter():
    letter = input("Enter letter: ")
    
    if letter.isalpha() and len(letter)==1:
        letter = letter.upper()
    else:
        print("*"*15 + "Incorrect Input" + "*"*15)
        return None
        
    if letter not in list_letter: 
        list_letter.append(letter)
        return letter
    else:
        print("*"*15 + "Letter already guessed" + "*"*15)
        return None


def find_letters():
    # index_list = [i for i in range(len(word)) if str(word[i])==letter]   ----> slower
    index_list = [i for i,val in enumerate(word) if str(val) == letter]
    for index in index_list:
        guess[index] = letter
            

def display():

    print("\n")
    print(''.join(guess))
    print("Number of wrong guesses left:" + str(num_guess))
    print("Letter guessed: " + ''.join([str(l) + "," for l in list_letter]))
    print("\n")


def result():
    print("\n\n")
    if guess == word:
        print("You Win")
        print(''.join(word) + " successfully guessed")

    else:
        print("You Lose")
        print("The word was: " + ''.join(word))
    

word = list(get_word())
#print(word)
guess = ["_ " for i in word]
num_guess = 7
list_letter = []

while num_guess > 0 and guess != word:
 
    display()
    letter = get_letter()

    if letter != None: 
        if letter in word:
            print("***Letter guessed correctly***")
            find_letters()

        else:
            print("***Letter guessed incorrectly***")
            num_guess-=1
    

result()
