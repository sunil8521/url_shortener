import mysql.connector
import os
def conn(q):
    global db,object
    db=mysql.connector.connect(
        host=os.environ['host_key'],
        passwd=os.environ['pass_key'],
        user=os.environ['admin_key'],
        database='url'
    )
    object=db.cursor()
    object.execute(q)
    all=object.fetchall()
    return all

def store():
  myresult=conn(q="select * from url_shorts")
  jobs_dict = []
  for row in myresult:
    job_dict = {}
    for index, value in enumerate(row):
      column_name = object.column_names[index]
      job_dict[column_name] = value
    jobs_dict.append(job_dict)
  db.close()
  return jobs_dict

def add(shorturl,longurl):
  dataBase = mysql.connector.connect(
      host=os.environ['host_key'],
      user=os.environ['admin_key'],
      passwd=os.environ['pass_key'],
      database="url"
  )
  object = dataBase.cursor()
  sql = f'''INSERT INTO url_shorts(shorturl, longurl)VALUES ('{shorturl}', '{longurl}')'''
  object.execute(sql)
  dataBase.commit()
  dataBase.close()