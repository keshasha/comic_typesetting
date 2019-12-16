import sqlite3
from sqlite3 import Error


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def insertBLOB(empId, name, photo, resumeFile):
    try:
        conn = sqlite3.connect('images.db')
        cursor = conn.cursor()
        print("Connected to SQLite")

        sql_create_images_table = """CREATE TABLE IF NOT EXISTS images (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        image blob,
                                        txt blob
                                        );"""
        create_table(conn, sql_create_images_table)

        sqlite_insert_blob_query = """ INSERT INTO 'images'
                                  ('id', 'name', 'image', 'txt') VALUES (?, ?, ?, ?)"""

        empPhoto = convertToBinaryData(photo)
        resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple = (empId, name, empPhoto, resume)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        conn.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")


if __name__ == '__main__':
    insertBLOB(1, "test1", "0.jpg", "test.txt")
    insertBLOB(2, "test2", "0.jpg", "test.txt")
