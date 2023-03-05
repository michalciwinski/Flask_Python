# This is a backend project for shop website with Postgresql
import DataBaseService as DBS







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #initilize DB
    DBS.ConnectDB()

    print('Write')
    datas = ['Michal', 'Ciwinski', 'Wojakowa 243', 'User']
    DBS.WriteToTableUsers(datas[0], datas[1], datas[2], datas[3])
    print('Wrote')



    print('close...')
    DBS.CloseConnectionDB()




