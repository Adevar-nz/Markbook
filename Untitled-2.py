'''Created by Jonathan Daniel
Date: 24/07/2026
The purpose of this file is to enter students name and raw score 
then convert score to grade and display a neat table
'''

#dictionaries, Constants and global variables
LOWER_GRADE_LIMIT = 0
HIGHER_GRADE_LIMIT = 100

teacher_name = ""
test_name = ""
students_and_score = {}

#--------Functions----------#

def str_validator(string):
    ''' checks if the input is a string'''

    if string.replace(" ", "").isalpha():
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
    

def entering_test_data():
    '''enters the data for the teacher and test name'''

    teacher_name = input("Please enter the teachers Name: ").title()

    while str_validator(teacher_name) == False:
        teacher_name = input("Please enter the teachers Name without numbers \
or special characters: ").title()
    
    test_name = input('Please enter the test Name:')

    while str_validator(test_name) == False:
        test_name = input('Please enter the test Name without numbers or \
 special characters:')

    return [teacher_name, test_name]

def score_entering():
    ''' Enters the score for each student and when finish is typed it will
    stop the program'''

    finish = ''
    
    while finish != "Finish":

        #Verifies the student name
        student_name = input("Please enter the students Name: ").title()
        while str_validator(student_name) == False:
            student_name = input("Please enter a VALID student Name: ")
        print()

        #Verifies the student score
        student_score = input("Please enter the students score: ")
        while number_and_range_validator(student_score, LOWER_GRADE_LIMIT, \
                                          HIGHER_GRADE_LIMIT) == False:
            student_score = input("Please enter a VALID student score: ")
        student_score = int(student_score)
        print()

        students_and_score[student_name] = student_score

        finish = input("Would you like to carry on? type finish if no: ").title()
        while str_validator(finish) == False:
            finish = input("Would you like to carry on? type finish if no: ").title()
        print()
            
def average_grade(dictionary):
    ''' gets the average score of the entire class'''

    

def get_highest_students():
    ''' gets the names of the top 3 students '''

