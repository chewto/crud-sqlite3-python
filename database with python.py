import sqlite3


def main():

    action = int(input("what you want to do?\n-press 1 to add a new student\n-press 2 to search a student\n-press 3 to look all the regitered students\n-press 4 to update the student information\n-press 5 to delete a student\n:"))

    if action == 1:
        id_student = int(input("enter an id: "))
        name_student = input("enter the student name: ")
        last_name_student = input("enter the student last name: ")

        new_student(id_student, name_student, last_name_student)

    # consultando un alumno

    elif action == 2:

        consult_name = input("enter stundets name: ")

        if search_student(consult_name):
            print("stundet reached")
        else:
            print("theres no any stundent with that name")

    elif action == 3:
        all_students()

    elif action == 4:

        old_name = input(
            "enter the name of the stundent to update the information: ")
        new_id = int(input("enter new id: "))
        new_name = input("enter new name: ")
        new_last_name = input("enter new last name: ")

        update_student(old_name, new_name,
                       new_id, new_last_name)

    elif action == 5:
        delete_name = input(
            "enter the name you want to delete: ")
        delete_student(delete_name)
        print("the student was deleted")

    else:
        print("action is not avaible")


def new_student(id, name, last_name):

    conn = sqlite3.connect('students.db', isolation_level=None)

    cursor = conn.cursor()

    query = f"INSERT INTO students(id, name, last_name) VALUES({id},'{name}','{last_name}')"

    rows = cursor.execute(query)

    cursor.close()
    conn.close()


def delete_student(name):
    conn = sqlite3.connect('students.db', isolation_level=None)

    cursor = conn.cursor()

    query = f" DELETE FROM students WHERE name='{name}'"

    rows = cursor.execute(query)

    cursor.close()
    conn.close()


def update_student(old_name, new_name, id, new_last_name):
    conn = sqlite3.connect('students.db', isolation_level=None)
    cursor = conn.cursor()

    query = f"UPDATE students SET id={id}, name='{new_name}',last_name='{new_last_name}'WHERE name='{old_name}'"

    rows = cursor.execute(query)

    cursor.close()
    conn.close()


def search_student(name):
    conn = sqlite3.connect('students.db')

    cursor = conn.cursor()

    query = f"SELECT * FROM students WHERE name='{name}'"

    rows = cursor.execute(query)

    data = rows.fetchone()

    cursor.close()
    conn.close()

    if data == None:
        return False
    else:
        print(data)
        return True


def all_students():
    conn = sqlite3.connect('students.db')

    cursor = conn.cursor()

    query = f"SELECT * FROM students"

    rows = cursor.execute(query)

    data = rows.fetchall()

    cursor.close()
    conn.close()

    if data == None:
        return False
    else:
        for row in data:
            print(row)
        return True


if __name__ == "__main__":
    main()
