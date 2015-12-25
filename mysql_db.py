# -*- coding: utf-8 -*-
#!/projects/contactcars/ven/bin/python2.7
import MySQLdb
import time
import csv
class Db:
    def __init__(self, host, user, passwd, db ,charset):
        self.db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, charset=charset)
        self.db.set_character_set('utf8')
        self.cur = self.db.cursor(MySQLdb.cursors.DictCursor)
        self.cur.execute('SET NAMES utf8;')
        self.cur.execute('SET CHARACTER SET utf8;')
        self.cur.execute('SET character_set_connection=utf8;')
        self.location = False



    def exists(self, href):
        query = 'select * from 26March2015 where _pageUrl="{0}" limit 1; '.format(href)
        self.cur.execute(query)
        for row in self.cur.fetchall() :
            return  True
        return False




    def insert_post(self, data, _source='contactcaes'):
        if self.exists(data['href']):
            print "exist"
            return False
        query = '''INSERT INTO 26March2015
                   ( _widgetName,_source,_resultNumber,_pageUrl,make,model,model_year,price,cc,km,`descr`,addedon)
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        self.cur.execute(query, ('contactcaes',_source,'0',data['href'],data['maker'], data['model'],data['year'],
                                data['price'],data['cc'],data['km'],data['descr'],''))
        self.db.commit()
        return True

    def get_old_data(self,source):
        sql_tpl = 'SELECT * FROM `26March2015`  WHERE `_source`="{0}"  AND `remove_date` is  NULL   ORDER BY `remove_date_check`   limit 100 '
        sql = sql_tpl.format(source)
        print sql
        self.cur.execute(sql)
        for row in self.cur.fetchall() :
            yield row


    def set_as_removed(self,idx):
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        query_tpl = '''UPDATE `26March2015`  SET remove_date ="{remove_date}" WHERE id={idx}'''
        query = query_tpl.format(remove_date=now,idx=idx)
        self.cur.execute(query)
        self.db.commit()

    def set_as_checked(self, idx) :
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        query_tpl = '''UPDATE `26March2015`  SET remove_date_check ="{remove_date_check}" WHERE id={idx}'''
        query = query_tpl.format(remove_date_check=now,idx=idx)
        self.cur.execute(query)
        self.db.commit()


# if __name__ == '__main__':
#     print "hi there!!"
#     db = Db(host='localhost',user='root',passwd='123456',db='Hamouda', charset='utf8')
#     mf = open('carsdata.csv')
#     lines = csv.DictReader(mf)    
#     for data in lines:
#         # data = {}
#         # data['href'] = 'nn'
#         data['descr'] = 'بحالة ودهان المصنع وصيانات في التوكيل'
#         data['cc'] = '00'
#         data['km'] = '00'
#         # data['price'] = '00'
#         # data['year'] = '22'
#         # data['model'] = 'mm'
#         # data['maker'] = 'mk'
#         print data['descr']        
#         break
#         for k,v in data.iteritems():
#             data[k] = data[k].encode('utf-8')

#         db.insert_post(data)

