import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

cursor = connection.cursor()

def employees_in_company(companyId):
    cursor.execute("SELECT userId, userName FROM user WHERE companyId = %s", (companyId,))
    for x in cursor:
        print(x)

employees_in_company(5)

