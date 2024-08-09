import mysql.connector
from mysql.connector import errorcode

def create_database():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Skeri@10.15',
        'raise_on_warnings': True
    }

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")

    else:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    create_database()