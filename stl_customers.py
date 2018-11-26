import csv
import random
#INSERT INTO seller(name, date_born, gender, dni, points, seller_type_id ) VALUES('Jose Luis Saenz', '4/22/1974', 'M', '12345678', 1013, 1)

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

#>>>>>>>> MAKE CHANGES HERE <<<<<<<<<<<<< 
DATABASE = "dev"
USER = "tatsudy"
PASSWORD = "Data1234"
HOST = "redshift-cluster-1.cn1wpjfeuivh.us-west-2.redshift.amazonaws.com"
PORT = "5439"
SCHEMA = "public"      #default is "public" 

####### connection and session creation ############## 
connection_string = "redshift+psycopg2://%s:%s@%s:%s/%s" % (USER,PASSWORD,HOST,str(PORT),DATABASE)
engine = sa.create_engine(connection_string)
session = sessionmaker()
session.configure(bind=engine)
s = session()
SetPath = "SET search_path TO %s" % SCHEMA
s.execute(SetPath)
###### All Set Session created using provided schema  #######

################ write queries from here ###################### 
query = "SELECT * FROM product;"
rr = s.execute(query)
all_results =  rr.fetchall()
print(all_results)

with open('personas.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        name = row['\ufeffGivenName'] + ' ' + row['Surname']
        date_born = row['Birthday']
        gender = 'F' if 'f' in row['Gender'] else 'M'
        dni = row['NationalID']
        query = "INSERT INTO customer(name, date_born, gender, dni) VALUES('%s', '%s', '%s', '%s')"%\
                (name, date_born, gender, dni)
        rr = s.execute(query)
        s.commit()


