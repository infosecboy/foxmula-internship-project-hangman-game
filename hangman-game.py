# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def validate_input(char):
    if (char.isalpha() == False):
         print(" Only  alphabests are appreciated in hangman games")
         return False
        
    if len(char)!=1:
        print(" Please input only a character not a complete word")
        return False
    return True
    


correct = []

import random

word_file = open('hidden-words.txt','r') #give text file of hidden words to guess here 

hidden_words = word_file.readlines()

hidden_word = random.choice(hidden_words)



def game_begins(char):
    
      
    
    if char in list(hidden_word):
        return True
    else:
        return False
            
             
            

user_tries = 0

limit = len(hidden_word)*2

lst = []

flag = 0

right=0

wrong=0
while(user_tries !=limit):
    user_guess = input('enter a character:')
    
    if validate_input(user_guess) == False:
        flag = 2
        break
    print('You entered ' + user_guess+' ')
    if game_begins(user_guess) == True:
        
        
         if  user_guess not in lst:
             print('yup you are in the right direction')
             lst.append(user_guess)
             correct.append(user_guess)      
             right+=1
             
         elif user_guess in lst:
            if lst.count(user_guess) <= list(hidden_word).count(user_guess) - 1:
                print('yup you are in the right direction')
                lst.append(user_guess)
                correct.append(user_guess)   
                right+=1
            else:
                print('Hmmm seems like you are overthinking now')
               
                wrong+=1
    elif game_begins(user_guess) == False:
        print("Sorry pal you are in the wrong direction")
        wrong+=1
    
    user_tries +=1
    print('you have ' + str(limit - user_tries)+ ' tries left')
    if len(correct) == len(list(hidden_word)) - 1:
        flag = 1
        break
    
    
    
if flag == 1:
    print('----------------------------------------------------------------')
    print(' you won congrats pal')
    print('By the way if you are curious the hidden word was '+ hidden_word)
    
    
elif flag == 0:
    print('----------------------------------------------------------------')
    print('Sorry but you have killed hangman you lost')
    print('you had '+str(right)+' guesses correct ')
    print('But you also had '+ str(wrong) + ' guesses wrong  which drown you boat towards success ')
elif flag ==2:
    pass
word_file.close()

    
        
        
          
         
        
    
        
        



