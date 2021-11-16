# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:20:01 2021

@author: Ayaz
"""

import random 
import string 
import os



def get_random_alpha_string():
    ###generating 10 to 20 letters random strings
    return ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(random.randint(10,20))) 
  
    
def get_random_integers():
    ####generating numbers from 5 to 20 digits integers
    ##can be done using just random.randint function by specifying big range.
    
    return int(''.join(str(i) for i in range(random.randint(5,20))))


def get_random_real_numbers(lower_range=1000,upper_range=100000000):
    ####function to generate real numbers in given range
    
    return random.uniform(lower_range,upper_range)




def get_alpha_numeric_string():
    ####generate alpha numeric strings.
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(random.randint(10,20)))



def check_string_type(inp_str):
    """Checks the type of string, either it is alphanumerics,alphabetical strings,integers or real numbers, """
    try:
        ####Check alphanumeric first as, string,integer and alphastring  are alpha numeric true
        ###checking alpha numeric first.
        if(inp_str.isalnum()):
            if(inp_str.isalpha()):
                return 'Alphabetical'
            ##check digit.
            elif(inp_str.isdigit()):
                return 'Integer'
            ##Otherwise alphanumeric
            else:
                return 'Alphanumeric'
        
        ###if not alpha numberic then either it is decimal
        elif(inp_str.replace('.','',1).isdigit()):
            return 'RealNumber'
        else:
            return 'Unknown'
    except:
        return False
        


def get_list_of_functions():
    ###returns list of functions for writing different strings,numbers,alphatical, alphanumeric string.
    return [get_random_alpha_string,get_alpha_numeric_string,get_random_integers,get_random_real_numbers]
    
    
    
def get_random_strings(n,sep=','):
    """Generates random strings based on given number and sepertor """
    ###getting the list of functions to get alpha numberic, alpha, numbers and integers strings.
    functions=get_list_of_functions()
    ###generating random strings of size n based on the random selection of functions in the list.
    return sep.join(str(random.choice(functions)()) for r in range(n))+','
    
    

    
def get_file_size(fname):
    """Returns file size in Mbs. """
    try:
        ##converting bytest to mbs,
        return os.path.getsize(fname)/1000000
    except:
        return None



def generate_file(file_name):
    """This function generates a file of size 2mb, consisting of  random alphabetical strings,integers and numbers. """
    try:
        file_size=0
        ###overwriting previous file.
        file = open(file_name, "w")
        ##while filesize is less than 2mbs
        while(file_size<2):  
            file.write(get_random_strings(200))
             ##check files size
            file_size=get_file_size(file_name)
        file.close()
        return True
    except:
        print("Unable to write file.")
        return False

 

def get_file_stats(file_name):
    try:
        ##reading file, assuming that file exists in the same directory.
        with open(file_name, 'r') as f:
            data = f.read().replace('\n', '')
        ###removing last ',' from file text
        data=data[:-1]
        ###converting string to its respective data types. i.e.AlphaNumeric, Alphabetical, Integer or real number 
        convert2types=lambda data_string: [check_string_type(d) for d in data_string.split(",")]
        get_type_counts_dict=lambda data_types:{typ: data_types.count(typ) for typ in set(data_types)}
        return get_type_counts_dict(convert2types(data))
        
    except:
        print("Unable to read file.")
        return None
 







