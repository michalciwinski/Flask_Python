#DataBase service with psycopg2 package.
import psycopg2
from configparser import ConfigParser


#ini file read datas to ConnectDB function
def ConfigIniFile(filename='database.ini', section='postgresql'):
    #parse .ini file
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
        print('INI:', db)
    else:
        raise Exception('Section ' + {section} + '  not found in the ' + {filename} + ' file')
    return db


# connect DB
def ConnectDB():
    global conn
    conn = None
    try:
        #rewrite datas to connect
        iniParameters = ConfigIniFile()

        #connect Database
        print('Connecting to the database...')
        conn = psycopg2.connect(**iniParameters)
        # create a cursor
        global cur
        cur = conn.cursor()
        cur.execute("SELECT * FROM tusers")
        print("Rows:", cur.rowcount)

        # display the PostgreSQL database server version
        rows = cur.fetchall()
        print(rows)


    except (Exception, psycopg2.DatabaseError) as error:
        print('Error:', error)



def CloseConnectionDB():
    if conn is not None:
        # close the communication with the PostgreSQL
        cur.close()
        conn.close()
        print('Database connection closed.')


def WriteToTableUsers(firstname, lastname, address, usertype):
    sql = "INSERT INTO tusers (firstname,lastname,address,usertype) VALUES (%s, %s, %s, %s) "
    # execute the INSERT statement
    insertList = ([(firstname), (lastname), (address), (usertype)])
    cur.execute(sql, insertList)
    # get the generated id back
    #vendor_id = cur.fetchone()[0]
    # commit the changes to the database
    conn.commit()