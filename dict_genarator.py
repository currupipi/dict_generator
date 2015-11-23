#! /usr/bin/env python
#Genertes an alphanumeric password dictionary

import sys
import string
import argparse
import itertools
import pdb

#Functions

def calc_dict_length(population, number_elements):
    """ 
    Shows the lenght of a dictionary based on:
    m = different elements that can make a word of the dict (uper/lowers chars and numbers)
    n = lenght of each word of the dict
    """
    return population ** number_elements

#   def generate_dict(file_name, lenght, lowercase, uppercase, numbers):
#   """ Generates alphanumeric words of n length chars """
#   try:
#       with open(file_name, w) as dict_file:
#           for char_lowercase in lowercase:
#               for char
#           dict_file.write()
            
#Main code

if __name__ == "__main__":

    #Vars

    # Console colors
    W = '\033[0m'  # white (normal)
    R = '\033[31m'  # red
    G = '\033[32m'  # green
    O = '\033[33m'  # orange
    B = '\033[34m'  # blue
    P = '\033[35m'  # purple
    C = '\033[36m'  # cyan
    GR = '\033[37m'  # gray

    #help message for command
    help_message = ("USAGE:\n" +
                "dict_generator.py uses alphanumeric chars to create a n lenght dictionary combination of them\n" +
                "dict_genarator.py -n <password_char_length> -l|-u|-c < at least one for: 'l' lowercase, 'u' upercase, 'n' numbers>\n") 

    #Create argparse object
    parser = argparse.ArgumentParser(usage=help_message, description='Creates alphanumeric passwords dict of n length')

    #Fill ArgumentParser with program arguments 
    parser.add_argument('-n', help='Define length of password ideally between 8 and 20', type=int, default=8)
    parser.add_argument('-l', help='l for lowercase [a-z]', default=False, action='store_true')
    parser.add_argument('-u', help='u for upercase [A-Z]', default=False, action='store_true')
    parser.add_argument('-c', help='n for numbers[0-9]', default=False, action='store_true')

    #Load and parse  arguments from ArgumentParser object
    args = parser.parse_args()

    #The population for the permutation calculation
    population = 0

    #Check needed input to run the script
    if args.n is not None:
        pass_length = int(args.n)
    else:
        print help_message
        print R + '[-] ERROR: You need to specify the lenght of the dict word' + W
        print help_message
        sys.exit(1)

    if not args.l and not args.u and not args.c:
        print R + '[-] ERROR: You need to specify l for lowercase [a-z]' + \
        'or u for upercase [A-Z] or c for ciphers between [0-9]' + W
        print help_message
        sys.exit(2)
    
    #Save the arguments from the input
    if args.l:
        lowercase = list(string.ascii_lowercase)
        print G + '[+] INFO: Will use [a-z] chars in the dict' + W
        population = population + len(lowercase)
    
    if args.u:
        uppercase = list(string.ascii_uppercase)
        print G + '[+] INFO: Will use [A-Z] chars in the dict' + W
        population = population + len(uppercase)

    if args.c:
        numbers = range(0,10)
        print G + '[+] INFO: Will use [0-9] numbers in the dict' + W
        population = population + len(numbers)

        pdb.set_trace()

    #Warn about the lenght of the dict
    print O + '[!] WARNING: The dict will have {} passwords! of {} length'.format(calc_dict_length(population ,pass_length), pass_length) + W  

