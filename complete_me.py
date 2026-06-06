import json

def greet(name): 
    '''
    Given a string, return the string "Hello, <the string goes here>! You are amazing :)"
    So given "Pickle" as input, the function should return "Hello, Pickle! You are amazing :)"
    '''
    
   
    return "Hello, "+name+"! You are amazing :)"




def how_hot_is_it(temp):
    '''
    Given an integer as input, return:

    "ICE ICE BABY" if the input is 0 or below.
    "Bring me a blanket" if the input is more than 0 but less than 20.
    "Nice and cozy" if the input is more than or equal to 20 but less than 24.
    "FEELIN' HOT HOT HOT" if the input is 24 or higher.
    '''
    
    if  temp <=0:
        return "ICE ICE BABY"
    if temp >0 and temp <20:
        return "Bring me a blanket"
    if temp >=20 and temp <24:
        return "Nice and cozy"
    if temp >=24:
        return "FEELIN' HOT HOT HOT"


def print_all_numbers_between_one_and_twenty_divisible_by_three():
    '''
    Print to standard output all integers between 1 and 20 that are divisible by 3.
    '''

    # PLEASE IMPLEMENT ME
    
    print("-1")


def do_you_need_a_cookie():
    '''
    Prompt the user for input with the question "Do you need a cookie?".
    If the answer is anything other than "Yes", prompt the user again with the same question.
    If the answer is "Yes", print "Go have a cookie. You deserve it :)" and stop taking user input.
    ''' 
    
    # PLEASE IMPLEMENT ME

    print("No :(")


def find_num_bikes():
    '''
    Given the information in the file 'free_bike_status.json',
    return the number of bikes that are not disabled and whose have 50% or more fuel.
    ''' 
    
    # PLEASE IMPLEMENT ME

    return -1
