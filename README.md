# GRADING SYSTEM

##FEATURES
-[Add students and subjects]
-[Enter and store grades for each student in different subjects]
-[Calculate and display average grades for all students]
-[Find and display the highest and lowest grades for each subject]
-[Search for students by name (case-insensitive)]
-[Update a student's grade]
-[Remove a student]
-[View all grades for a specific subject]
-[Sort students by average grade or name (using insertion sort)]

##USER INTERFACE (UI)
The application will guide you through various options to manage your gradebook.
The main menu allows you to perform different actions:
-[Add a new student]
-[Update a student's grade]
-[Remove a student]
-[View grades for a specific subject]
-[Search for students by name]
-[Sort students by average grade or name]
-[Exit the program]

##ERROR HANDLING
The code is designed to handle mistakes and problems. If you enter something wrong or something unexpected happens, you'll get a helpful message explaining the issue.

#CODE STRUCTURE
The code is structured into multiple classes and functions to enhance its clarity and ease of management:
###Classes:
Student: Represents a student with a name and a dictionary to store grades for each subject.
Gradebook: Manages the overall gradebook functionality, including adding/removing students and subjects, calculating averages, searching, sorting, etc.
###Functions:
get_student_data: Prompts for and collects student and subject data during program initialization.
