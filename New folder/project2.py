import mysql.connector

# Connect to DB
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Revathi@2004",
    database="revathidb1"
)
cursor = conn.cursor()

# Add a student
def add_student(name, marks):
    sql = "INSERT INTO students (name, marks) VALUES (%s, %s)"
    cursor.execute(sql, (name, marks))
    conn.commit()
    print("Student added successfully!")

# View all students
def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)
    print("data viewed successfully!")


# Delete student by ID
def delete_student_by_name(name):
    cursor.execute("DELETE FROM students WHERE name = %s", (name,))
    conn.commit()
    print("Student deleted by name!")


# Sample usage
add_student("CNR", 85)
view_students()
delete_student_by_name("anu")
view_students()

cursor.close()
conn.close()