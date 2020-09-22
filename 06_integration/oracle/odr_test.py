import cx_Oracle

hostname = "hostname"
port = "port"
service_name = "servicename"
username = "username"
password = "password#"

dsn_tns = cx_Oracle.makedsn(hostname, port, service_name=service_name)

connection = cx_Oracle.connect(user=username, password=password, dsn=dsn_tns)

cursor = connection.cursor()
cursor.execute("""
            select * from talbe
            where id = :id
               """,
               id = 671)

for result in cursor:
    print(result)