import mysql.connector

def conn(q):
    global db,object
    db=mysql.connector.connect(
        host="onlinedb.cd88md7c0vfy.eu-north-1.rds.amazonaws.com",
        passwd='siren123',
        user="admin",
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
      host="onlinedb.cd88md7c0vfy.eu-north-1.rds.amazonaws.com",
      user="admin",
      passwd="siren123",
      database="url"
  )
  object = dataBase.cursor()
  sql = f'''INSERT INTO url_shorts(shorturl, longurl)VALUES ('{shorturl}', '{longurl}')'''
  object.execute(sql)
  dataBase.commit()
  dataBase.close()