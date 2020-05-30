import random 

def get_word():

    word=""
    with open("Wordlist.txt","r") as f:

        while len(word) < 3:
            word=random.choice(f.readlines())            

    return word[:-1].upper() 
    

#print(list(get_word()))
