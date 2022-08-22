import sqlite3  # importamos la libreria de sqlite


def create(first_name_param, second_name_param, first_last_name_param, second_last_name_param, phone_number_param, email_param, ci_param, age_param, coming_of_age_param):

    conn = sqlite3.connect('info.db', isolation_level=None)

    cursor = conn.cursor()

    query = f'INSERT INTO info(first_name, second_name, first_last_name, second_last_name, phone_number, email, ci, age, coming_of_age) VAlUES("{first_name_param}","{second_name_param}","{first_last_name_param}","{second_last_name_param}","{phone_number_param}","{email_param}",{ci_param},"{age_param}","{coming_of_age_param}")'

    rows = cursor.execute(query)

    cursor.close()

    conn.close()


def read(first_name_param, ci_param):
    conn = sqlite3.connect('info.db')

    cursor = conn.cursor()

    query = f"SELECT * FROM info WHERE first_name='{first_name_param}' AND ci={ci_param}"

    rows = cursor.execute(query)

    data = rows.fetchone()

    cursor.close()
    conn.close()

    if data == None:
        return False
    else:
        print(data)
        return True


def read_all():
    conn = sqlite3.connect('info.db')

    cursor = conn.cursor()

    query = f"SELECT * FROM info"

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


def update(new_first_name_param, new_second_name_param, new_first_last_name_param, new_second_last_name_param, new_phone_number_param, new_email_param, new_ci_param, new_age_param, new_coming_of_age_param, old_first_name_param, old_ci_param):

    conn = sqlite3.connect('info.db', isolation_level=None)

    cursor = conn.cursor()

    query = f"UPDATE info SET first_name='{new_first_name_param}', second_name='{new_second_name_param}', first_last_name='{new_first_last_name_param}', second_last_name='{new_second_last_name_param}',  phone_number='{new_phone_number_param}', email='{new_email_param}', ci={new_ci_param}, age='{new_age_param}', coming_of_age='{new_coming_of_age_param}' WHERE first_name='{old_first_name_param}' AND ci={old_ci_param}"

    rows = cursor.execute(query)

    cursor.close()

    conn.close()


def delete(first_name_param, first_last_name_param, email_param, ci_param):

    conn = sqlite3.connect('info.db', isolation_level=None)

    cursor = conn.cursor()

    query = f'DELETE FROM info WHERE first_name="{first_name_param}" AND first_last_name="{first_last_name_param}" AND email="{email_param}" AND ci={ci_param}'

    rows = cursor.execute(query)

    cursor.close()

    conn.close()
