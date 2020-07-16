import json
import pymysql
import pymysql.cursors
conn = pymysql.Connect(host='localhost', user='root',passwd='', db='beebom')
cursor = conn.cursor()
cursor.execute("SELECT * FROM employee")
result = cursor.fetchall()
print(f"json: {json.dumps(result)}")