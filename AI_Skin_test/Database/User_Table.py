import MySQLdb

class User_Table:

    # connect database skin_dia_users
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "", "skin_dia_users")
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT VERSION()")


    # create a table
    def create_user_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS user_form")
        sql_create_table = """CREATE TABLE user_form (
                 user_id INTEGER AUTO_INCREMENT,
                 email  CHAR(50) NOT NULL,
                 password  CHAR(20) NOT NULL,
                 PRIMARY KEY (user_id))"""

        self.cursor.execute(sql_create_table)
        print self.cursor.fetchone()

    def insert_user(self, user_acc):
        sql_insert = "INSERT INTO user_form(email,password) VALUES (" +"\'"+ str(user_acc['email'])+"\'"+","+"\'"+str(user_acc['password'])+"\'"+")"
        #print sql_insert
        self.cursor.execute(sql_insert)
        self.db.commit()


    def query_user(self, user_email):
        sql_query = "SELECT password FROM user_form WHERE email=" + "\'"+str(user_email)+ "\'"
        #print sql_query
        self.cursor.execute(sql_query)
        result = self.cursor.fetchone()
        return result[0]


    def close_database(self):
        self.db.close()


if __name__ == '__main__':
    mt = User_Table()
    #mt.create_user_table()
    # user = {'email':'c@163.com', 'password':'123'}
    # mt.insert_user(user_acc=user)
    mt.query_user('c@163.com')
    mt.close_database()