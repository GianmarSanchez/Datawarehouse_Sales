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

products = {}
for gg in all_results:
    products[gg[0]] = gg

#(859, 'Corralito Tot Bloc Bugs Quilt', datetime.date(2005, 5, 24), 515.4)

for i in range(1000):
    pro = random.randint(1, 859)
    if pro in products:
        row = products[pro]
    else:
        continue
    price = str(row[3])
    date_id = '1'
    seller_type_id = random.randint(1, 3)
    seller_id = random.randint(1, 2204)
    customer_id = random.randint(1, 8727)
    sale_type_id = random.randint(1, 3)
    
    query = "INSERT INTO sale(price, date_id, seller_type_id, seller_id, customer_id, sale_type_id) VALUES(%s, %s, %s, %s, %s, %s)"%\
                (price, date_id, seller_type_id, seller_id, customer_id, sale_type_id)
    rr = s.execute(query)
    s.commit()
    query_sp = "INSERT INTO sale_product(sale_id, product_id) VALUES(%s, %s)"%\
                (i, row[0])
    rr = s.execute(query_sp)
    s.commit()

