from mysql import connector
import datetime

class DbConnect:
    def get_connected(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="arshi",
                password="arshi",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            return None

class GymMemberManager(DbConnect):
    def get(self):
        try:
            self.connect = super().get_connected() # super is used to call parent class and with that its method
            self.cursor = self.connect.cursor()
            query="Select * from member"
            self.cursor.execute(query)
            record=self.cursor.fetchall()
            # print(record)
            return record
        except Exception as e:
            print(e)

    def get_object(self,id=None):
        try:
            self.cursor = self.connect.cursor()
            query = "select * from member where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None

    #to insert data using post()method
    def post(self,**kwargs):
        try:
            self.connect=super().get_connected()
            self.cursor=self.connect.cursor()
            query="""
                  insert into member(name,place,mobile,plan,fee,joined_date)
                  values(%s,%s,%s,%s,%s,%s)
                  """
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("New Members Added Successfully.....")
        except Exception as e:
            print(e)
    #retrieving data with particular id
    def retrieve(self,id=None):
        try:
            self.connect=super().get_connected()
            self.cursor=self.connect.cursor()
            query=""" 
                 select * from member
                 where id=%s
                 """
            values=[id,]
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            print(records)
        except Exception as e:
            print(e)

    # data to be deleted using id
    def delete(self,id=None):
        try:
            self.connect=super().get_connected()
            self.cursor=self.connect.cursor()
            query="""
                 delete from member
                 where id=%s
            """
            values=[id,]
            self.cursor.execute(query,values)
            self.connect.commit()
        except Exception as e:
            print(e)

    #updating and modifying data
    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
                self.connect = super().get_connected()
                self.cursor=self.connect.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+= k +"=%s, "
                    placeholder=placeholder.rstrip(", ")
                    query=f"update member set {placeholder}  where id=%s"
                    values=[v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query,values)
                    self.connect.commit()
                    print("Member updated successfully")
            else:
                print("Member Not Found")
        except Exception as e:
            print(e)





connection_instance=DbConnect()  # object for parent class
print(connection_instance.get_connected()) # to check whether with mysql conected and display it

connect_instance=GymMemberManager()  #object for child class
#to fetch data from table
print("------Member Details----")
connect_instance.get()
#inserting data into table using post
# connect_instance.post(name="Arshit",place="Kakkanad",mobile="8848219118",plan="1 month",fee=2500,joined_date=datetime.date.today())
# connect_instance.post(name="Sameer",place="Kollam",mobile="9744472721",plan="3 month",fee=3500,joined_date=datetime.date.today())
# connect_instance.post(name="Sathpriyan",place="Kannur",mobile="9746154857",plan="6 month",fee=7000,joined_date=datetime.date.today())
# connect_instance.post(name="Deslin",place="Kannur",mobile="986754567",plan="6 month",fee=7000,joined_date=datetime.date.today())
# connect_instance.post(name="Sreelal",place="Kakkanad",mobile="7895467893",plan="1 month",fee=2500,joined_date=datetime.date.today())
# connect_instance.post(name="Albin",place="Kakkanad",mobile="9374567893",plan="3 month",fee=3500,joined_date=datetime.date.today())
print("-------Data Fetched---------")
connect_instance.retrieve(id=1)
#deleting id=6
print("----Data Deleted with id=6------")
connect_instance.delete(id=6)

#updation
connect_instance.put(1,place="Aranmula")