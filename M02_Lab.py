"""Author: Venise Saron
Professor: Ray Storer
Subject: SDEV 220
Last Revised: 1-28-2024
File Name: M02_Lab
Module #: M02 Lab - Case Study: if...else and while
Github URL: https://github.com/ViviCarta/M01-Collaboration.git
Purpose: This app takes student names and GPAs to 
identify whether the student qualifies for either 
the Dean's list or Honor Roll.
"""

# Initialize CONSTANT variables
DEAN_LIST: float = 3.5
HONOR_ROLL: float = 3.25

# Prompt for the student's last name and accepts input.
while True:
    student_last_name = str(input("Please enter the student's last name: "))

    # Error handling
    if student_last_name == 'ZZZ':
        # Outputs a print statement that echoes to the user the inputted name,
        # and an indication that the process is discontinued.
        print(f'{student_last_name} cannot be processed in the system.')
        break
    else:
        # Continues the process by prompting for the student's GPA and accepting input.
        student_grade = float(input("Please enter the student's GPA: "))

        # Error handling
        if student_grade >= DEAN_LIST:
            # Outputs a print statement that the student qualified for the Dean's List.
            print(f"Congratulations! {student_last_name} is in the Dean's List.")
        elif student_grade >= HONOR_ROLL:
            # Outputs a print statement that the student qualified for the Honor Roll.
            print(f"Great job! {student_last_name} is in the Honor Roll.")

        # Additional error handling code for unqualified students.
        else:
            if student_grade < HONOR_ROLL:
                print(f"Unfortunately, {student_last_name} did not qualify for any academic award.")

    # Break statement to exit the application/loop.
    break
