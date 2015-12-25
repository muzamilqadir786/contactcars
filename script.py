# -*- coding: utf-8 -*-
#!/usr/local/bin/python2.7
from mysql_db import *
DATABASE_SETTINGS = dict(
    host='HHamouda.mysql.pythonanywhere-services.com',
    # port = 3306,
    user='HHamouda',
    passwd='mysql',
    db='test', 
    charset='utf8'
)
    



if __name__ == '__main__':    
    print DATABASE_SETTINGS
    try:
        db = Db(**DATABASE_SETTINGS)
        print db
        mf = open('carsdata.csv')
        lines = csv.DictReader(mf)    
        for data in lines:                        
            data['cc'] = '00'
            data['km'] = '00'            
            print data['descr']                                
            db.insert_post(data)
        except MySQLdb.Error,e:
        print "exception"
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    
