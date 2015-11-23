#! /usr/bin/env python

#Genertes an alphanumeric password dictionary

import string, argparse

#Functions
def generate_dict(file_name, lenght, lowercase, uppercase, numbers):
    """ Generates alphanumeric words of n length chars """
    try:
        with open(file_name, w) as dict_file:
            for char_lowercase in lowercase:
                for char
            dict_file.write()
            


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
     
    #Alphanumeric chars 
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    numbers = range(0,10)

    #help message for command
    help_message = ("USAGE:\n" +
                "dict_generator.py uses alphanumeric a-z A-Z 0-9" +
                "dict_genarator.py -n <password_char_length> and wait...\n" ) 

    #Create argparse object
    parser = argparse.ArgumentParser(usage=help_message, description='Creates alphanumeric passwords dict of n length')

    #Fill ArgumentParser with program arguments 
    parser.add_argument('-n', help='Define length of password >8 <21', default=20)

    #Load and parse  arguments from ArgumentParser object
    args = parser.parse_args()

    if (int(args.n) >= 8) and (int(args.n) < 21):
        
        
    else:
        print help_message












    #We need at least the  to be provided or a file with users
    if args.u is not None:
        ldap_obj = open_ldap(args.s)
        check_user(ldap_obj, args.u)
        close_ldap(ldap_obj)

    elif args.f is not None:
        with open(args.f) as f:
            ldap_obj = open_ldap(args.s)
            for line in f:
                try:
                    user = line.rstrip()
                    check_user(ldap_obj, user)
                except:
                    print "ERROR: Please check file content is one user per line with 'name.surname' format"
                    sys.exit(1)
            close_ldap(ldap_obj)
        
    else:
        print help_message
