

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
highest_student_list = []

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
        
        elif score >= 90:
            return "E"
    else:
        return False
    

def entering_test_data( ):
    '''enters the data for the teacher and test name'''
    global teacher_name, test_name

    teacher_name = input("Please enter the teachers Name: \n").title()
#checks if the teacher name is valid
    while str_validator(teacher_name) == False:
        teacher_name = input("Please enter the teachers Name without numbers \
or special characters: \n").title()
    
    test_name = input('Please enter the test Name:\n')
        
    


def score_entering():
    ''' Enters the score for each student and when finish is typed it will
    stop the program'''

    finish = ''
    
    while finish != "Finish":

        #Verifies the student name
        student_name = input("Please enter the students Name: \n").title()
        while str_validator(student_name) == False:
            student_name = input("Please enter a VALID student Name: \n")
        print()

        #Verifies the student score
        student_score = input("Please enter the students score: \n")
        while number_and_range_validator(student_score, LOWER_GRADE_LIMIT, \
                                          HIGHER_GRADE_LIMIT) == False:
            student_score = input("Please enter a VALID student score: \n")

        student_score = int(student_score)
        print()

        students_and_score[student_name] = student_score

        #aks user if they want to continue
        finish = input("Would you like to carry on? type finish if complete: \n").title()
        while str_validator(finish) == False:
            finish = input("Would you like to carry on? type finish if complete: \n").title()
        print()
            
def average_grade(dictionary):
    ''' gets the average score of the entire class'''

    average = 0
    for key, value in dictionary.items():
        average = average + value

    average = average / len(dictionary)

    return average

def get_highest_students(dictionary):
    ''' gets the names of the top 3 students '''

    top_student_amount = 3
    student_dict = dictionary
    
    while top_student_amount != 0:
        highest_student = max(student_dict, key = student_dict.get)

    # adds the student to the list, a removes it from the local list,allowing
    #second to be the new highest student
        highest_student_list.append(highest_student)
        del student_dict[highest_student]
        top_student_amount = top_student_amount - 1

    return highest_student_list


def get_lowest_student(dictionary):
    '''gets the lowest student in the dictionary '''

    lowest_student = min(dictionary, key = dictionary.get)

    return lowest_student


#----------Main Program----------#

test_data = entering_test_data()
print()
score_entering()
print()

print(f" The teacher name is: {teacher_name}\n The test name is: {test_name}")
#writes the table of the entire classes score, grade and name
for key,value in students_and_score.items():
    print(f"Student: {key} Score: {value} Grade: {grade_converter(value)}")

print()
print(f'The Top 3 students is \n {get_highest_students(students_and_score)}')
print()
print(f"The lowest student is \n {get_lowest_student(students_and_score)}")
print()
print(f"The average score was : {average_grade(students_and_score)}")

