from ast import main
import sys

from collections import Counter

import load_dictionary

dict_file = load_dictionary.load('2of4brif.txt')
# ensure "a"&"I (both lower case) are included"
dict_file.append('a')
dict_file.append('i')
dict_file = sorted(dict_file)

ini_name = input ("Enter a name:")

def find_anagrams(name, word_list):
    """Read name &dictionary file & display all anagrams IN name"""
    name_letter_map = Counter(name)
    anagrams=[]
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
                if Counter (test) == word_letter_map:
                    anagrams.append(word)
    print (*anagrams,sep='\n')
    print ()
    print ("Remaining letters = {}".format(name))
    print ("Number of remainige letters = {}".format(len(name)))
    print ("Number of remainig (real word)anagrams = {}".format(len(anagrams)))


def process_choice(name):
    """ Check user choice for validity, returm choice & leftover letters."""
    while True:
        choice = input('\n Make a choice else Enter to start over or # to end:')
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
            if len(name) - len(left_over_list) == len(candidate):
                break
            else:
                print("Won't work!Make another choice!", file = sys.stderr)
        name = ''.join(left_over_list) #makes display more readble
        return choice, name
def main ():
    """Help user build anagram phrase from their name"""
    name = ''.join(ini_name.lower().split())
    name = name.replace("-",'')
    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace('','')
        if len (temp_phrase) < limit:
            print('Length of anagram phrase = {}'.format(len(temp_phrase)))

            find_anagrams(name, dict_file)
            print ("Current anagram phrase =", end = "")
            print (phrase, file=sys.stderr)

            choice, name = process_choice(name)
            phrase += choice +''

        elif len(temp_phrase) == limit:
            print ("\n*****FINISHED!!!*****\n")
            print("Anagram of name =''",end="")
            print (phrase, file=sys.stderr)
            print()
            try_again = input('\n\nTry again? (Press Enter else"n" to quit)\n')
            if try_again.lower() == "n":
                running = False
                sys.exit()
            else:
                main()

if __name__ == '__main__':
    main()
