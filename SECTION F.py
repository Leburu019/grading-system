# SECTION F:

class StudentNotFoundError(Exception):
    """Custom exception raised when a student is not found."""
    pass

class InvalidGradeError(Exception):
    """Custom exception raised for invalid grade input."""
    pass

class Student:
    def __init__(self, name):
        """Initialize a Student object with a name and an empty grades dictionary."""
        self.name = name
        self.grades = {}  # Dictionary to store grades for subjects

    def add_grade(self, subject, grade):
        """Add a grade for a specific subject. If the subject doesn't exist, create an entry."""
        if subject not in self.grades:
            self.grades[subject] = []  # Initialize an empty list for new subjects
        self.grades[subject].append(grade)  # Append the grade to the list of grades for the subject

    def calculate_average(self):
        """Calculate the average grade across all subjects."""
        total_grades = sum(sum(grades) for grades in self.grades.values())  # Sum all grades
        num_grades = sum(len(grades) for grades in self.grades.values())  # Count total number of grades
        return total_grades / num_grades if num_grades > 0 else 0  # Return average or 0 if no grades

    def print_details(self):
        """Print the student's name, average grade, and grades for each subject."""
        print(f"\nStudent: {self.name}")  # Print the student's name
        average_grade = self.calculate_average()  # Calculate the average grade
        print(f"\tAverage Grade: {average_grade:.2f}")  # Print the average grade formatted to two decimal places
        for subject, grades in self.grades.items():
            print(f"\t{subject}: {grades}")  # Print grades for each subject

class Gradebook:
    def __init__(self):
        """Initialize a Gradebook with lists for students and subjects."""
        self.students = []  # List to store Student objects
        self.subjects = []  # List to store subject names

    def add_subject(self, subject_name):
        """Add a new subject to the gradebook if it doesn't already exist."""
        if subject_name not in self.subjects:
            self.subjects.append(subject_name)  # Append the subject name to the list

    def add_student(self, student_name):
        """Add a new student to the gradebook after collecting grades for all subjects."""
        if any(student.name == student_name for student in self.students):
            print(f"Error: Student '{student_name}' already exists.")  # Check for duplicate student names
        else:
            student = Student(student_name)  # Create a new Student object
            for subject in self.subjects:
                grade = self.get_valid_grade(student_name, subject)  # Get a valid grade for each subject
                student.add_grade(subject, grade)  # Add the grade to the student's record
            self.students.append(student)  # Add the student to the list of students
            print(f"Student '{student_name}' added successfully.")

    def remove_student(self, student_name):
        """Remove a student from the gradebook by name."""
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)  # Remove the student if found
                print(f"Student '{student_name}' removed successfully.")
                return
        raise StudentNotFoundError(f"Error: Student '{student_name}' not found.")  # Raise an error if not found

    def get_student(self, student_name):
        """Retrieve a student by name, case-insensitively."""
        for student in self.students:
            if student.name.lower() == student_name.lower():
                return student  # Return the found student
        raise StudentNotFoundError(f"Error: Student '{student_name}' not found.")  # Raise an error if not found

    def get_valid_grade(self, student_name, subject_name):
        """Prompt the user to input a grade, ensuring it's valid."""
        for attempt in range(3):  # Allow 3 attempts to enter a valid grade
            try:
                grade = float(input(f"Enter the grade for {student_name} in {subject_name}: "))  # Get user input
                if 0 <= grade <= 100:
                    return grade  # Return the grade if valid
                else:
                    raise InvalidGradeError("Invalid grade. Please enter a number between 0 and 100.")  # Raise error for out-of-range
            except ValueError:
                print("Invalid input. Please enter a numeric value.")  # Handle non-numeric input
            except InvalidGradeError as e:
                print(e)  # Print custom error message
        print("Maximum attempts reached. No grade added.")  # Notify user if attempts are exhausted
        return None  # Return None if no valid grade was entered

    def calculate_and_display_averages(self):
        """Calculate and display the average grades for all students."""
        for student in self.students:
            student.print_details()  # Print details for each student

    def find_highest_and_lowest_grades(self):
        """Find and print the highest and lowest grades for each subject."""
        highest_grades = {}  # Dictionary to store highest grades
        lowest_grades = {}  # Dictionary to store lowest grades

        for student in self.students:
            for subject, grades in student.grades.items():
                if grades:  # Check if there are grades for the subject
                    highest_grades[subject] = max(highest_grades.get(subject, float('-inf')), max(grades))  # Find highest grade
                    lowest_grades[subject] = min(lowest_grades.get(subject, float('inf')), min(grades))  # Find lowest grade

        print("\nHighest Grades:")  # Print heading for highest grades
        for subject, highest_grade in highest_grades.items():
            print(f"\t{subject}: {highest_grade:.2f}")  # Print highest grade for each subject

        print("\nLowest Grades:")  # Print heading for lowest grades
        for subject, lowest_grade in lowest_grades.items():
            print(f"\t{subject}: {lowest_grade:.2f}")  # Print lowest grade for each subject

    def search_and_update_student(self, student_name):
        """Search for a student and allow the user to update their grades or view their details."""
        try:
            student = self.get_student(student_name)  # Attempt to get the student
            print(f"Student '{student_name}' found.")
            while True:
                try:
                    print("\nWhat would you like to do?")  # Menu for actions
                    print("1. Update a grade")
                    print("2. View grades")
                    print("3. Return to main menu")
                    choice = int(input("Enter your choice: "))  # Get user choice

                    if choice == 1:  # Update a grade
                        subject_name = input("Enter the subject name: ").lower().strip()  # Get subject name
                        new_grade = self.get_valid_grade(student_name, subject_name)  # Get a valid grade
                        if new_grade is not None:  # Check if a valid grade was returned
                            student.add_grade(subject_name, new_grade)  # Add the new grade
                            print(f"Grade for '{student_name}' in {subject_name} updated successfully.")

                    elif choice == 2:  # View grades
                        student.print_details()  # Print student details

                    elif choice == 3:  # Return to menu
                        break

                    else:
                        print("Invalid choice. Please try again.")  # Handle invalid choice
                except ValueError:
                    print("Invalid choice. Please enter a number.")  # Handle non-integer input
        except StudentNotFoundError as e:
            print(e)  # Print error if student not found

    def insertion_sort_students(self, criteria='average'):
        """Sorts the students by their average grades or by name using the insertion sort algorithm."""
        for i in range(1, len(self.students)):  # Start from the second student
            key = self.students[i]  # The student to be compared
            j = i - 1  # Index for the sorted part of the list

            # Compare based on the specified criteria
            if criteria == 'average':
                while j >= 0 and key.calculate_average() > self.students[j].calculate_average():
                    j -= 1
            elif criteria == 'name':
                while j >= 0 and key.name < self.students[j].name:
                    j -= 1

            self.students.insert(j + 1, self.students.pop(i))  # Insert the student in the correct position

        print("\nStudents Sorted by", "Average Grade" if criteria == 'average' else "Name:")  # Print sorting criteria
        for student in self.students:
            student.print_details()  # Print sorted student details

    def search_students(self, name):
        """Search for students by name, case-insensitively, and print the results."""
        found_students = [student for student in self.students if name.lower() in student.name.lower()]  # List comprehension to find students
        if found_students:
            print("\nSearch Results:")  # Print heading for search results
            for student in found_students:
                student.print_details()  # Print details of each found student
        else:
            print(f"No students found with name '{name}'.")  # Print message if no students are found

def get_student_data(num_students, gradebook: Gradebook):
    """Prompt for and collect student and subject data, adding them to the gradebook."""
    num_subjects = int(input("Enter the number of subjects: "))  # Get number of subjects from user
    for j in range(num_subjects):
        while True:
            try:
                subject_name = input(f"Enter the name of subject {j + 1}: ").lower().strip()  # Get subject name
                if not subject_name:
                    raise ValueError("Subject name cannot be empty.")  # Validate input
                gradebook.add_subject(subject_name)  # Add subject to gradebook
                break
            except ValueError as ve:
                print(ve)  # Print error message

    for i in range(num_students):
        while True:
            try:
                student_name = input(f"Enter the name of student {i + 1}: ").lower().strip()  # Get student name
                if not student_name:
                    raise ValueError("Student name cannot be empty.")  # Validate input
                gradebook.add_student(student_name)  # Add student to gradebook
                break
            except ValueError as ve:
                print(ve)  # Print error message

# Main execution
while True:
    try:
        num_students = int(input("Enter the number of students: "))  # Prompt for number of students
        gradebook = Gradebook()  # Create a new Gradebook instance
        get_student_data(num_students, gradebook)  # Collect data for students

        gradebook.calculate_and_display_averages()  # Display average grades
        gradebook.find_highest_and_lowest_grades()  # Find and display highest and lowest grades

        while True:  # Main menu loop
            print("\nChoose an action:")
            print("1. Add a new student")
            print("2. Update a student's grade")
            print("3. Remove a student")
            print("4. View grades for a specific subject")
            print("5. Search for students by name")
            print("6. Sort students")
            print("7. Exit")
            try:
                choice = int(input("Enter your choice: "))  # Get user action choice

                if choice == 1:  # Add a new student
                    student_name = input("Enter the name of the new student: ").lower().strip()  # Get student name
                    gradebook.add_student(student_name)  # Add the student

                elif choice == 2:  # Update a student's grade
                    student_name = input("Enter the name of the student: ").lower().strip()  # Get student name
                    gradebook.search_and_update_student(student_name)  # Search and update grades

                elif choice == 3:  # Remove a student
                    student_name = input("Enter the name of the student to remove: ").lower().strip()  # Get student name
                    try:
                        gradebook.remove_student(student_name)  # Attempt to remove the student
                    except StudentNotFoundError as e:
                        print(e)  # Print error if student not found

                elif choice == 4:  # View grades for a specific subject
                    subject_name = input("Enter the subject name: ").lower().strip()  # Get subject name
                    print(f"\nGrades for '{subject_name}':")  # Print heading for grades
                    for student in gradebook.students:
                        if subject_name in student.grades:
                            print(f"\t{student.name}: {student.grades[subject_name]}")  # Print grades for each student

                elif choice == 5:  # Search for students by name
                    search_name = input("Enter the student's name to search: ").lower().strip()  # Get name to search
                    gradebook.search_students(search_name)  # Search and print results

                elif choice == 6:  # Sort students
                    print("\nSelect sorting criteria:")
                    print("1. Sort by average grade")
                    print("2. Sort by name")
                    sort_choice = int(input("Enter your choice: "))  # Get sort preference

                    if sort_choice == 1:
                        gradebook.insertion_sort_students(criteria='average')  # Sort by average grade
                    elif sort_choice == 2:
                        gradebook.insertion_sort_students(criteria='name')  # Sort by name
                    else:
                        print("Invalid choice.")  # Handle invalid sorting choice

                elif choice == 7:  # Exit the program
                    print("Program ends here, Thank You")  # Exit message
                    exit()  # Exit the program

                else:
                    print("Invalid choice. Please try again.")  # Handle invalid choice
            except ValueError:
                print("Invalid input. Please enter a number between 1-7.")  # Handle non-integer input
            except Exception as e:
                print(f"An unexpected error occurred: {e}")  # Handle unexpected errors

    except ValueError:
        print("Invalid input for number of students or subjects. Please enter valid integers.")  # Handle input errors for number of students
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Handle unexpected errors
