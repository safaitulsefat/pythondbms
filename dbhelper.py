import mysql.connector as connctor


class DBHelper:
    def __init__(self):
        self.con = connctor.connect(host='localhost', user='root', password='', database='lab')
        query = 'create table if not exists user(userId int primary key,userName varchar(200),phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("created success")
    #insert
    def insert_user(self, userid, username, userphone):
        query = "insert into user (userId,userName,phone) values({},'{}','{}')".format(userid, username, userphone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")
    def feach__all(self):
        query = ('select * from user')
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("user ID:", row[0])
            print("user Name:", row[1])
            print("user phone:", row[2])
            print()
            print()
    def delete__user(self,userid):
        query = 'delete from user where userId={}'.format(userid)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("deleted")
    def update__user(self, userid, username, userphone):
        query = 'update user set userName= "{}" , phone = "{}" where userId={}'.format(username, userphone, userid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("update success")




