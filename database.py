import sqlalchemy as s
import os

def conn(q):
  engine = s.create_engine(os.environ['var'])
  global connection
  connection=engine.connect()
  result = connection.execute(s.text(q))
  return result

def store():
  myresult=conn(q="select * from url_shorts")
  column_names = myresult.keys()
  result_list = [dict(zip(column_names, row)) for row in myresult.fetchall()]
  connection.close()
  return result_list

def add(shorturl,longurl):
  engine = s.create_engine(os.environ['var'])
  connection=engine.connect()
  connection.execute(s.text("insert into url_shorts(shorturl,longurl) values(:x,:y)"),[{"x":f"{shorturl}", "y": f"{longurl}"}])
  connection.commit()
  connection.close()
