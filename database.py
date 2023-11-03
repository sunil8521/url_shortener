import sqlalchemy as s


def connector():
    try:
        engine = s.create_engine(
            "mysql+pymysql://admin:siren123@onlinedb.cd88md7c0vfy.eu-north-1.rds.amazonaws.com:3306/url?charset=utf8mb4"
        )
        connection = engine.connect()
        return connection
    except Exception as e:
        raise ConnectionError(
            "Failed to establish a database connection") from e


def fetch():
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


def fetch_shorturl(q,val):
    myConnection = None
    try:
        myConnection = connector()
        myresult = myConnection.execute(s.text(q), [{"val": f"{val}"}]).fetchall()
        return myresult[0][0]
    except Exception as e:
        return None
    finally:
        if myConnection:
            myConnection.close()
            print("connection closed")

def add(shorturl, longurl):
    try:
        myConnection = connector()
        myConnection.execute(s.text("insert into url_shorts(shorturl,longurl) values(:x,:y)"), [
            {"x": f"{shorturl}", "y": f"{longurl}"}])
        myConnection.commit()
        myConnection.close()
    except Exception as e:
        raise Exception("Failed to add data in the database") from e

# result = next((i['shorturl'] for i in url_list if long_url == i['longurl']),None)
