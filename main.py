from flask import Flask,render_template,jsonify,request,redirect
import string
import random
from database import fetch ,add
app=Flask(__name__,template_folder='file')

def short_url(length=6):
    all=string.ascii_letters+string.digits
    result="".join(random.choice(all) for _ in range(length))
    return result

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/url',methods=['POST','GET'])
def url():
    if request.method =="POST":
        long_url=request.form['mainurl']
        if long_url:
            url_list=fetch()
            result = next((i['shorturl'] for i in url_list if long_url == i['longurl']),None)
            if result is None:
                result = short_url()
                add(result,long_url)
            return render_template("redirect.html",val=f"{request.url_root}{result}",lurl=long_url)
        else:
            return render_template('home.html',error_meassage="URL is required")
    return render_template('home.html')

@app.route("/<result>")
def show(result):
    check_list=fetch()
    checker=next((i['longurl'] for i in check_list if result == i['shorturl']),False)
    if checker:
        return redirect(str(checker))
    else:
        return render_template('404.html')
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
