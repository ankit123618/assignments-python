import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

cursor = connection.cursor()

# function to show employees according to a company
def employees_in_company(companyId):
    cursor.execute("SELECT userId, userName FROM user WHERE companyId = %s", (companyId,))
    print("EMPLOYEES WORKING IN COMPANY, ID=> ",companyId," ARE:")
    print()
    print("HERE IS THE LIST OF EMPLOYEES WITH THIER ID AND NAMES: ")
    print()
    for x in cursor:
        print(x)

employees_in_company(5)

