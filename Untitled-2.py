'''Created by Jonathan Daniel
Date: 24/07/2026
The purpose of this file is to enter students name and raw score 
then convert score to grade and display a neat table
'''

#dictionaries and Constants
LOWER_GRADE_LIMIT = 0
HIGHER_GRADE_LIMIT = 100
TEACHER_NAME = "MS Liang"
TEST_NAME = "Y10 Web design"

Students_and_score = {}

#--------Functions----------#

def str_validator(string):
    ''' checks if the input is a string'''

    if string.isalpha():
        return True
    
    else:
        return False
    
def number_and_range_validator(input, lower_range, higher_range):
    ''' Checks if the input is a number and if it is in the range'''

    #checks if input only as digits
    if input.isdigit():
        input = int(input)
    #checks if input is in range of provide values
        if input >= lower_range and input <= higher_range:

            return True
        else:
            return False
    else:
        return False

    
def grade_converter(score):
    ''' converts the score to a grade'''
    if score >= LOWER_GRADE_LIMIT and score <= HIGHER_GRADE_LIMIT:
        
        if score < 50:
            return 'NA'
        
        elif score >= 50 and score <= 69:
            return 'A'
        
        elif score >= 70 and score <= 89:
            return "M"
        
        elif score > 90:
            return "E"
    else:
        return False
    

def data_entering():
    '''enters the data of the students and their score into the dictionary'''
            