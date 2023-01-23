import cx_Oracle

class Emp1:
    def __init__(self):           
        self.con = None;
        self.cursor = None;
        
    def open(self):
        if(self.con is None):
            self.con = cx_Oracle.connect('sai/kiran@localhost')

    def close(self):
        if self.cursor is True:
            self.cursor.close()
        if self.con is True:
            self.con.close()


    def select(self):
        self.open()
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT * FROM Emp1")
        result = self.cursor.fetchall()
        return result

    
    def insert(self,empno,ename,sal):
        self.open()
        self.cursor = self.con.cursor()
        self.cursor.execute("INSERT INTO emp1 values (:emono,:ename,:sal) ",(empno,ename,sal))
        result = self.con.commit()
        


    def select_max_sal(self):
        self.open()
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT max(sal) from emp1")
        result = self.cursor.fetchall()
        return result   

    def select_min_sal(self):
        self.open()
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT min(sal) from emp1")
        result = self.cursor.fetchall()
        return result

    def select_total_sal(self):
        self.open()
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT sum(sal) from emp1")
        result = self.cursor.fetchall()
        return result

    def delete_record(self,empno):
        try:
            self.open()
            self.cursor = self.con.cursor()
            self.cursor.execute("DELETE from emp1 where empno = " + str(empno))
            self.con.commit()
            
        except cx_Oracle.DatabaseError as error:
            print("The error is", error)
        finally:
            self.close()
        


obj = Emp1()
'''
print(obj.select())
print(obj.select_max_sal())
print(obj.select_min_sal())
print(obj.select_total_sal())
'''

obj.delete_record(1003)
'''
obj.insert(1003,'sai',3000)
'''








    
