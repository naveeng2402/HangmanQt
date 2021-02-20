from os import get_terminal_size
import re, string, random
def game(word):
    word_lst = [i for i in word]
    disp_lst = ['_' for i in range(len(word))]
    
    while word_lst != disp_lst:
        guess = input('Enter Guess: ')
        if guess not in word_lst:
            print('letter not in word')
            continue
        else:
            ind = [i.start() for i in re.finditer(guess, word)]
            for i in ind:
                if disp_lst[i] != '_':
                    continue
                else:
                    disp_lst[i] = guess
                    break
            word_lst.remove(guess)
            print(' '.join(disp_lst).center(get_terminal_size().columns))
            
def fill(word:str):
    lst = [i for i in word.upper()]
    print(f'{lst=}')
    if len(lst)<10: lst.extend(random.choices(string.ascii_uppercase,k=10-len(word)))
    print(f'{lst=}')
    random.shuffle(lst)
    print(f'{lst=}')
fill('naveen')