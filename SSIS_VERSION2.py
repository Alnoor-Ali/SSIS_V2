import mysql.connector
from prettytable import from_db_cursor

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="ssis_v2"
)

mycursor = db.cursor()

def main_display_menu():
    print("--------------------------------------")
    print(" Welcome to MSU-IIT's Student Information System")
    print("---------------------------------------")
    print("Please choose one:")
    print("1.Student Info\n2.Courses\n3.Exit program")




def display_menu1():
    print("Please what you want to do...\n")
    print("1. Add New Student")
    print("2. Display Students")
    print("3. Search Students")
    print("4. Update Students")
    print("5. Delete Students")
    print("6. Back to main menu")



def display_menu2():
    print("Please choose agaain...\n")
    print("1. Add Courses")
    print("2. View Courses")
    print("3. Search Course")
    print("4. Update Courses")
    print("5. Back to main menu")

def add_student():
    print("Enter student id: ")
    student_id = input()

    while True:
        query = f"SELECT * FROM `student_info` WHERE student_id = '{student_id}'"
        mycursor.execute(query)
        row = mycursor.fetchone()
        if row != None:
            print("Student ID already existed.")
            print("Input again.")
            student_id = input("Enter student id: ")

        else:
            break

    print("Enter student name: ")
    student_name = input()
    print("Enter year level: ")
    year_level = input()
    print("Enter student gender: ")
    gender = input()
    print("Enter student course: ")
    course = input()
    while True:
        query = f"SELECT * FROM `course` WHERE course_code = '{course}'"
        mycursor.execute(query)
        row = mycursor.fetchone()
        if row != None:
           break

        else:
            print("Course Code does not exist.")
            print("Input again.")
            course = input("Enter course code: ")

    mycursor.execute("INSERT INTO `student_info` (student_id, student_name, year_level, gender, course_code) "
                     "VALUES (%s,%s,%s,%s,%s)",
                     (student_id, student_name, year_level, gender, course))

    db.commit()


def display():
    mycursor.execute("SELECT * FROM `student_info`")
    table = from_db_cursor(mycursor)
    print(table)

    input("Press any key to continue")
    display_menu1()


def search_student():
    print("Enter student_id: ")
    student_id = input()
    query = f"SELECT * FROM `student_info` WHERE student_id = '{student_id}'"
    mycursor.execute(query)
    row = mycursor.fetchone()
    if row != None:
        print(row)
    else:
        print("Student ID not Found")

    input("Press any key to continue")


def update_student():
    print("Enter student_id: ")
    student_id = input()
    query = f"SELECT * FROM `student_info` WHERE student_id = '{student_id}'"
    mycursor.execute(query)
    row = mycursor.fetchone()
    if row != None:
        print("What do you want to edit?")
        print(
            "1.Student id\n2.Student Name\n3.Year Level\n4.Gender\n5.Course")
        choice = input("Enter your choice: ")
        if choice == "1":
            new_student_id = input("Enter new student id: ")
            query2 = f"UPDATE student_info SET student_id = '{new_student_id}' WHERE student_id = '{student_id}'"
            mycursor.execute(query2)
            db.commit()
        if choice == "2":
            new_student_name = input("Enter new student name: ")
            query2 = f"UPDATE student_info SET student_name = '{new_student_name}' WHERE student_id = '{student_id}'"
            mycursor.execute(query2)
            db.commit()
        if choice == "3":
            new_student_yl = input("Enter new student year level: ")
            query2 = f"UPDATE student_info SET year_level = '{new_student_yl}' WHERE student_id = '{student_id}'"
            mycursor.execute(query2)
            db.commit()
        if choice == "4":
            new_student_gender = input("Enter new student gender: ")
            query2 = f"UPDATE student_info SET gender = '{new_student_gender}' WHERE student_id = '{student_id}'"
            mycursor.execute(query2)
            db.commit()
        if choice == "5":
            new_student_cc = input("Enter new student course code: ")
            query2 = f"UPDATE student_info SET course_code = '{new_student_cc}' WHERE student_id = '{student_id}'"
            mycursor.execute(query2)
            db.commit()

    else:
        print("Student ID not Found")
        input("Please enter again")
        update_student()

    input("Press any key to continue")


def delete():
    student_id = input("Enter student_id: ")
    query = f"SELECT * FROM `student_info` WHERE student_id = '{student_id}'"
    mycursor.execute(query)
    row = mycursor.fetchone()
    if row != None:
        query2 = f"DELETE FROM student_info WHERE student_id = '{student_id}'"
        mycursor.execute(query2)
        db.commit()
    else:
        print("Student ID not Found")

        input("Press any key to continue")


def update_course():
    course_c = input("Enter course code: ")
    query = f"SELECT * FROM `course` WHERE course_code = '{course_c}'"
    mycursor.execute(query)
    row = mycursor.fetchone()
    if row != None:
        print("What do you want to edit?")
        print(
            "1.Course code\n2.Course Name")
        choice = input("Enter your choice: ")
        if choice == "1":
            new_course_code = input("Enter new course code: ")
            query2 = f"UPDATE course SET course_code = '{new_course_code}' WHERE course_code = '{course_c}'"
            mycursor.execute(query2)
            db.commit()
        if choice == "2":
            new_course_name = input("Enter new Course name: ")
            query2 = f"UPDATE course SET course_name = '{new_course_name}' WHERE course_code = '{course_c}'"
            mycursor.execute(query2)
            db.commit()

    else:
        print("Course code not Found")

        input("Press any key to continue")

def add_courses():
    course_code = input("Enter new course: ")
    while True:
        query = f"SELECT * FROM `course` WHERE course_code = '{course_code}'"
        mycursor.execute(query)
        row = mycursor.fetchone()
        if row != None:
            print("Course code already existed.")
            print("Input again.")
            course_code = input("Enter course code: ")

        else:
            break
    course_name = input("Enter course name: ")

    mycursor.execute("INSERT INTO `course` (course_code, course_name) "
                     "VALUES (%s,%s)",
                     (course_code, course_name))
    db.commit()

def display_course():
    mycursor.execute("SELECT * FROM `course`")
    table = from_db_cursor(mycursor)
    print(table)

    input("Press any key to continue")

def search_course():
    course_code = input("Enter Course code: ")
    while True:
        query = f"SELECT * FROM `course` WHERE course_code = '{course_code}'"
        mycursor.execute(query)
        row = mycursor.fetchone()
        if row is None:
            print("Course code not found.")
            course_code = input("Enter Course code: ")
        else:
            print(row)
            input("Press any key to continue")
            break



while True:
    main_display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        display_menu1()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            display()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete()
        elif choice == "6":
            main_display_menu()

    elif choice == "2":
        display_menu2()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_courses()
        elif choice == "2":
            display_course()
        elif choice == "3":
            search_course()
        elif choice == "4":
            update_course()
        elif choice == "5":
            main_display_menu()

    else:
        break


print("Thank you for using our system!")