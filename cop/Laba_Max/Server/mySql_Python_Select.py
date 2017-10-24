#mySql_Python_Select

import mysql.connector
from mysql.connector import errorcode

def sql_select(num_line):
    return_value = list()
    try:
        cnx = mysql.connector.connect(user='root', password='ma',
                                      host='127.0.0.1',
                                      database='test_schema')
        cursor = cnx.cursor()

        query = "SELECT x, y FROM test_schema.Operands Where id = {0};".format(num_line)

        cursor.execute(query)

        for line in cursor:
            return_value.append(line)

        cursor.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
    return return_value

def sql_find_max_id():
    return_value = list()
    try:
        cnx = mysql.connector.connect(user='root', password='ma',
                                      host='127.0.0.1',
                                      database='test_schema')
        cursor = cnx.cursor()

        query = "SELECT id FROM test_schema.Operands Where id = {0};".format(num_line)

        cursor.execute(query)

        for line in cursor:
            return_value.append(line)

        cursor.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
    return return_value

def sql_insert(x, y):
    cnx = mysql.connector.connect(user='root', password='ma',
                                  host='127.0.0.1',
                                  database='test_schema')
    cursor = cnx.cursor()

    query = 'INSERT INTO `test_schema`.`Operands`(`x`, `y`) VALUES ("{0}", "{1}");'.format(x, y)

    cursor.execute(query)

    cnx.commit()
    cursor.close()

    return 1

"""x = sql_select(2)
print(x)
print(x[0][0], x[0][1])
"""


#sql_insert(2,8)