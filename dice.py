# This module accepts inputs a string in the form "XdY" where X is a quantity of Y sided dice and returns an integer equal to the sum of the those dice.

import random

def roll(str_input):

    # Verify input is properly formated
    validate_input(str_input)
 
    # Process the dice roll
    list_split_input = str_input.split("d")
    int_output = 0
    int_dice_rolled = 0
    int_number_of_dice = int(list_split_input[0])

    while int_dice_rolled < int_number_of_dice:
        int_output += random.randint(1,int(list_split_input[1]))
        int_dice_rolled += 1 

    return int_output

def validate_input(str_input):
    
    if isinstance(str_input, str):

        # Verify input is in the XdY format.
        str_input = str_input.lower()

        int_d_count = 0
        int_index_position = 0
        int_string_length = len(str_input)

        while int_index_position < int_string_length:
            if str_input[int_index_position].isnumeric() : pass
            elif str_input[int_index_position] == "d" : int_d_count += 1
            else : raise ValueError("Roll function requires a string in an \"XdY\" format.  An invalid character was found.  " + "\"" + str(str_input[int_index_position]) + "\" is the invalid character at index position " + str(int_index_position))
            int_index_position += 1

        if int_d_count != 1 : raise ValueError("Roll function requires a string in an \"XdY\" format.  This requires exactly 1 \"d\".  " + str(int_d_count) + " were found.") 

    else : raise TypeError("Roll function requires a string in an \"XdY\" format. " + "\"" + str(str_input) + "\" is not a string.")
