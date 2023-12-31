import sqlalchemy as s
import os
def connector():
    try:
        engine = s.create_engine(os.environ['MY_SQL'])
        connection = engine.connect()
        return connection
    except Exception as e:
        raise ConnectionError(
            "Failed to establish a database connection") from e


def fetch():  # fetch all
    myConnection = None
    try:
        myConnection = connector()
        myresult = myConnection.execute(s.text("SELECT * FROM url_shorts;"))
        column_names = myresult.keys()
        result_list = [dict(zip(column_names, row))
                       for row in myresult.fetchall()]
        return result_list
    except Exception as e:
        raise Exception("Failed to fetch data from the database") from e
    finally:
        if myConnection:
            myConnection.close()
            print("connection closed")
print(fetch())

def fetch_shorturl(q, val):  # fetch single value
    myConnection = None
    try:
        myConnection = connector()
        myresult = myConnection.execute(
            s.text(q), [{"val": f"{val}"}]).fetchall()
        return myresult[0][0]
    except Exception as e:
        return None
    finally:
        if myConnection:
            myConnection.close()
            print("connection closed")


def add(shorturl, longurl):  # for add uel in database
    try:
        myConnection = connector()
        myConnection.execute(s.text("insert into url_shorts(shorturl,longurl) values(:x,:y)"), [
            {"x": f"{shorturl}", "y": f"{longurl}"}])
        myConnection.commit()
        myConnection.close()
    except Exception as e:
        raise Exception("Failed to add data in the database") from e


# fro add conatact info in postgres
def add_contact_details_with_postgres(first_name, last_name, email, number, message):
    engine = s.create_engine(os.environ['MY_SQL'])
    connection = engine.connect()

    params = {
        'f': first_name,
        'l': last_name,
        'e': email,
        'n': number,
        'm': message
    }
    result = connection.execute(s.text(
        "INSERT INTO contact (first_name,last_name,email,number,message) VALUES (:f,:l,:e,:n,:m)"), params)
    connection.commit()
    connection.close()
# result = next((i['shorturl'] for i in url_list if long_url == i['longurl']),None)
