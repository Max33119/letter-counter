print("this program displays info about letters/numbers in phrases \n")



def translate(phrase):
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.islower():
                print(letter + " - Lower case vowel")
            elif letter.isupper():
                print(letter + " - Upper case vowel")
        elif letter.lower() == " ":
            print("")
        elif letter in "1234567890":
            print(letter + " - Number")
        else:
            if letter.islower():
                print(letter + " - Lower case consonant")
            elif letter.isupper():
                print(letter + " - Upper case consonant")
        
     
            

translate(input("Enter a word or phrase: "))




input("\nPress enter to end program")
            


