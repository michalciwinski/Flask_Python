#DataBase service with psycopg2 package.
import psycopg2
from configparser import ConfigParser
import types
class Database:
    cur = None
    conn = None
    #constructor
    def __init__(self, name, func = None):
        self.name = name
        if func is not None:
            self.ConnectDB = types.MethodType(func, self)

    #desctructor - not used
    #def __del__(self, func = None):
    #    #self.CloseConnectionDB()
    #    if func is not None:
    #        self.CloseConnectionDB = types.MethodType(func, self)

    def ConnectDB(self):
        try:
            #rewrite datas to connect
            iniParameters = self.ConfigIniFile()
            #connect Database
            print('Connecting to the database...')
            self.conn = psycopg2.connect(**iniParameters)
            print(self.name + ' connected.')

        except (Exception, psycopg2.DatabaseError) as error:
            print('Error:', error)
            print(self.name + ' not connected.')

    # ini file read datas to ConnectDB function
    def ConfigIniFile(self, filename='database.ini', section='postgresql'):
        # parse .ini file
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
    def readAllDatas(self,table):
        # create a cursor
        self.cur = self.conn.cursor()
        self.cur.execute(table)
        print("Rows:", self.cur.rowcount)

        # display the PostgreSQL database server version
        rows = self.cur.fetchall()
        print(rows)

    def CloseConnectionDB(self):
        if self.conn is not None:
            # close the communication with the PostgreSQL
            self.conn.close()
            self.conn.close()
            print('Database connection closed.')

    def WriteToTableUsers(self,firstname, lastname, address, usertype):
        sql = "INSERT INTO tusers (firstname,lastname,address,usertype) VALUES (%s, %s, %s, %s) "
        # execute the INSERT statement
        insertList = ([(firstname), (lastname), (address), (usertype)])
        self.cur.execute(sql, insertList)
        # get the generated id back
        #vendor_id = self.cur.fetchone()[0]
        # commit the changes to the database
        self.conn.commit()




def initDBLoop():
    # initilize DB
    db1 = Database("first")
    db1.ConnectDB()
    table = "SELECT * FROM tusers"
    db1.readAllDatas(table)
    datas = ['Staszek', 'Malinowski', 'Wojakowa 243', 'User']
    db1.WriteToTableUsers(datas[0], datas[1], datas[2], datas[3])
    db1.readAllDatas(table)
    db1.CloseConnectionDB()


    #DB1.WriteToTableUsers(datas[0], datas[1], datas[2], datas[3])

