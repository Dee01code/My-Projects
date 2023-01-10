import random
import string

WORDLIST_FILENAME = "words.txt"
alph_set = set(string.ascii_lowercase)

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    str_result=""
    for i in secret_word:
        if i in letters_guessed:
            str_result+=i
        else:
            str_result+="_ "
    return str_result        



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    letters_guessed_set = set(letters_guessed)
    available_letters = "".join(list (sorted ( alph_set - letters_guessed_set )))
    return available_letters
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print("You have 3 warnings left.")
    print("- - - - - - - - - - - -")

    guesses_remaining = 6
    warnings_remaining = 3
    vowels = ['a','e','i','o','u']
    letters_guessed=[]
    
    while guesses_remaining > 0 and secret_word != get_guessed_word(secret_word, letters_guessed):
        print("You have",guesses_remaining,"guesses left.")
        print("Available Letters:",get_available_letters(letters_guessed))
        user_input=str.lower(input("Please guess a letter: "))
        if len(user_input)>1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops!  You have taken more than 1 letter. You have {warnings_remaining} warnings left. ")
            else:
                guesses_remaining-=1
                print("Oops!  You have taken more than 1 letter. You have no warnings left.")
        elif user_input not in alph_set:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops!  This is not a valid letter. you have {warnings_remaining} warnings left.")
            else:
                guesses_remaining-=1
                print("Oops!  This is not a valid letter. You have no warnings left.")                
        else:
            if user_input in letters_guessed:
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print(f"Oops!  you've already guessed that letter. you have {warnings_remaining} warnings left.")
                else:
                    guesses_remaining-=1
                    print("Oops!  you've already guessed that letter letter. You have no warnings left.")
            else:
                letters_guessed.append(user_input)
                if user_input in secret_word:
                    print("Good guess:",get_guessed_word(secret_word, letters_guessed))
                elif user_input in vowels:
                    guesses_remaining-=2
                    print("Oops!  That letter is not in my word:",get_guessed_word(secret_word, letters_guessed))
                else:
                    guesses_remaining-=1
                    print("Oops!  That letter is not in my word:",get_guessed_word(secret_word, letters_guessed))
       # print(letters_guessed)                
        print()            
        print("- - - - - - -")
        print()
    if guesses_remaining > 0 and is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        #print("Your total score for  this game is:"
    else:
        print("Sorry, you ran out of guesses. The word was else.")
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word=my_word.replace("_ ","_")
    if len(my_word)==len(other_word):
        for i in range(len(my_word)):
            if my_word[i]!="_" and my_word[i]==other_word[i]:
                pass
            elif my_word[i]!="_" and my_word[i]!=other_word[i]:  
                return False
            else:
                pass
        return True        
            
    else:
        return False
        



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    result=set()
    for i in wordlist:
        if match_with_gaps(my_word, i):
            result.add(i)

    return result


def show_possible_matches2(spm,my_word,lg):
    Hint_words = ""
    my_word = my_word.replace("_ ","_")
    set1 = set(my_word)
    set1.discard('_')
    set2 = set(lg)
    set3 = set2-set1
    set4 = set()
    for i in set3:
        for j in spm:
            if i in j:
                set4.add(j)
    Hint_words += ("  ".join(spm-set4))
    return Hint_words


def print_hangman(guesses_remaining):
    if guesses_remaining==7:
        print("""
         ___________
        |       
        |      
        |     
        |      
        |     
              """)
        return "    Ready to Hang!"
    elif guesses_remaining==6:
        print("""
         ____________
        |      | 
        |      
        |     
        |      
        |     

              """)
        return "    ~6 STEPS AWAY"
    elif guesses_remaining==5:
        print("""
         ____________
        |      | 
        |      O 
        |     
        |      
        |     

              """)
        return "    PROCEEDING TOWARDS DEATH"
    elif guesses_remaining==4:
        print("""
         ____________
        |      | 
        |      O 
        |      |
        |      
        |     

              """)
        return "    STILL YOU CAN SAVE YOURSELF IN 4 ATTEMPTS"
    elif guesses_remaining==3:
        print("""
         ____________
        |      | 
        |      O 
        |      |
        |      |
        |     

              """)
        return "    DON'T MISS YOUR HINT OPTION, CLICK : * "
    elif guesses_remaining==2:
        print("""
         ____________
        |      | 
        |      O 
        |     \\|/
        |      |
        |     

              """)
        return "    ~CLOSE ENOUGH, THINK MORE TAKE YOUR TIME~"
    elif guesses_remaining==1:
        print("""
         ____________
        |      | 
        |      O 
        |     \\|/
        |      |
        |     / 

              """)
        return "    YOU CAN USE HINT '*' OPTION MULTIPLE TIMES"
    else :
        print("""
         ____________
        |      | 
        |      O 
        |     /|\\
        |      |
        |     / \\

              """)
        return "    You are Hanged and Dead!"
            


            

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print()
    print("I'm Dee01Code, i have a dictionary containing 55950 words and you are playing against me. ")
    print()
    print("GAME DESCRIPTION:  As game starts i'll randomly choose a word from my dictionary and your job is to guess that. ")
    print()
    print("""SOME BASIC RULES:

             1. The user starts with TOTAL 8 guesses and 3 warnings.

             2. If you input anything besides an alphabet (symbols, numbers),
                   a. If you have one or more warning left, you'll lose one 
                      warning. 
                   b. If you have no remaining warnings, you'll lose one guess.

             3. If you input a letter that has already been guessed,
                   a. If you have one or more warning left, you'll lose one 
                      warning. 
                   b. If you have no remaining warnings, you'll lose one guess.

             4. If you input a letter that hasn’t been guessed before and
                the letter is in the secret word, the you lose no​ guesses.

             5. Consonants:​ If you input a consonant that hasn’t been
                guessed and the consonant is not in the secret word, the user
                loses one​ guess if it’s a consonant.

             6. Vowels:​ If the vowel hasn’t been guessed and the vowel
                is not in the secret word, the user loses two​ guesses.
                Vowels are a, e, i, o, and u. y does not count as a vowel.

             7. use '*' for HINT.    
                

             """)
    print("""
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

          """)
    print("--Start!--")
    print()
    print("I have choosen a word that is",len(secret_word),"letters long.")
    print("Your 3 warnings left.")
    print("- - - - - - - - - - - -")
    print()
    guesses_remaining = 7
    warnings_remaining = 3
    vowels = ['a','e','i','o','u']
    letters_guessed=[]
    
    while guesses_remaining > 0 and secret_word != get_guessed_word(secret_word, letters_guessed):
        print("You have",guesses_remaining,"guesses left.")
        print("Available Letters:",get_available_letters(letters_guessed))
        user_input=str.lower(input("Please guess a letter: "))
        if len(user_input)>1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops!  You have taken more than 1 letter. You have {warnings_remaining} warnings left. ")
            else:
                guesses_remaining-=1
                print("Oops!  You have taken more than 1 letter. You have no warnings left.")
                print(print_hangman(guesses_remaining))
        elif user_input not in alph_set:
            if user_input == "*":
                print("Possible word matches are: ")
                print(show_possible_matches2(show_possible_matches(get_guessed_word(secret_word, letters_guessed)),get_guessed_word(secret_word, letters_guessed),letters_guessed))
            elif warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops!  This is not a valid letter. you have {warnings_remaining} warnings left.")
            else:
                guesses_remaining-=1
                print("Oops!  This is not a valid letter. You have no warnings left.")
                print(print_hangman(guesses_remaining))
        else:
            if user_input in letters_guessed:
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print(f"Oops!  you've already guessed that letter. you have {warnings_remaining} warnings left.")
                else:
                    guesses_remaining-=1
                    print("Oops!  you've already guessed that letter letter. You have no warnings left.")
                    print(print_hangman(guesses_remaining))
            else:
                letters_guessed.append(user_input)
                if user_input in secret_word:
                    print("Good guess:",get_guessed_word(secret_word, letters_guessed))
                elif user_input in vowels:
                    guesses_remaining-=2
                    print("Oops!  That letter is not in my word:",get_guessed_word(secret_word, letters_guessed))
                    print(print_hangman(guesses_remaining))
                else:
                    guesses_remaining-=1
                    print("Oops!  That letter is not in my word:",get_guessed_word(secret_word, letters_guessed))
                    print(print_hangman(guesses_remaining))
       # print(letters_guessed)                
        print()            
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
        print()
    if guesses_remaining > 0 and is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won! and Found unguilty ")
        print("""
         
                
               O 
              \\|/
               |
              / \\

              """)

        print("Your Score is:",guesses_remaining,"out of 8")
    else:
        print("Sorry, you ran out of guesses. The word was :",secret_word)
    print('''

            Game Over!  

            ''')
    run_exit()    

def run_exit():
    print(" press '1' to play game again. ")
    print(" press '2' to quit the game. "  )
    print()
    a=input("Enter 1 or 2 : ")
    print()
    if a=='1':
        print()
        if __name__ == "__main__":
            secret_word = choose_word(wordlist)
            hangman_with_hints(secret_word)
            
    elif a=='2'  :
        exit()

    else:
        print("invalid input")
        print()
        run_exit()
        

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
