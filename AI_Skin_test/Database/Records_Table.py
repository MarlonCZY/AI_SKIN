import MySQLdb

class Record_Table:

    # connect database skin_dia_users
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "", "skin_dia_users")
        self.cursor = self.db.cursor()


    # create a table
    def create_record_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS records")
        sql_create_table = """CREATE TABLE records (
                 record_id INTEGER AUTO_INCREMENT,
                 user_email CHAR(50) NOT NULL ,
                 image_url CHAR(100) NOT NULL ,
                 possibility_1  FLOAT NOT NULL,
                 possibility_2  FLOAT NOT NULL,
                 possibility_3  FLOAT NOT NULL,
                 PRIMARY KEY (record_id))"""

        self.cursor.execute(sql_create_table)
        print self.cursor.fetchone()

    def insert_record(self, record):
        sql_insert = "INSERT INTO records(user_email,image_url,possibility_1,possibility_2,possibility_3 ) VALUES("+"\'"+ str(record['user_email'])+"\'"+","+"\'"+ str(record['image_url'])+"\'"+ ","+ str(record['possibility_1'])+","+ str(record['possibility_2'])+","+ str(record['possibility_3'])+")"
        print sql_insert
        self.cursor.execute(sql_insert)
        self.db.commit()


    def query_record(self, user_email):
        #sql_query = "SELECT user_id FROM records WHERE email=" + "\'"+str(user_email)+ "\'"
        sql_query = "SELECT * FROM records WHERE user_email =" +"'"+ user_email+"'"
        print sql_query
        self.cursor.execute(sql_query)
        result = self.cursor.fetchall()
        print result
        return result

    def query_num_record(self, user_email):
        sql_query_num = "SELECT COUNT(*) FROM records WHERE user_email =" +"'"+ user_email+"'"
        self.cursor.execute(sql_query_num)
        result = self.cursor.fetchone()
        print result
        return result


    def close_database(self):
        self.db.close()


if __name__ == '__main__':
    mt = Record_Table()
    mt.create_record_table()

    record1 = {'image_url':'http://192.168.0.10:8080/static/cz@163.com_0.jpg','user_email':'cz@163.com', 'possibility_1':0.4,'possibility_2':0.2,'possibility_3':0.3}
    record2 = {'image_url':'http://192.168.0.10:8080/static/cz@163.com_1.jpg','user_email':'cz@163.com', 'possibility_1':0.4,'possibility_2':0.2,'possibility_3':0.3}
    record3 = {'image_url':'http://192.168.0.10:8080/static/c@163.com_0.jpg','user_email':'c@163.com', 'possibility_1':0.4,'possibility_2':0.2,'possibility_3':0.3}
    record4 = {'image_url':'http://192.168.0.10:8080/static/c@163.com_1.jpg','user_email':'c@163.com', 'possibility_1':0.4,'possibility_2':0.2,'possibility_3':0.3}
    record5 = {'image_url':'http://192.168.0.10:8080/static/c@163.com_2.jpg','user_email':'c@163.com', 'possibility_1':0.4,'possibility_2':0.2,'possibility_3':0.3}


    mt.insert_record(record=record1)
    mt.insert_record(record=record2)
    mt.insert_record(record=record3)
    mt.insert_record(record=record4)
    mt.insert_record(record=record5)

    mt.query_record('cz@163.com')
    mt.query_num_record('c@163.com')
    mt.close_database()