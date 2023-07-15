from flask import Flask,render_template,jsonify,request,redirect
import string
import random
from database import store ,add
app=Flask(__name__,template_folder='file')

def short_url(length=6):
    all=string.ascii_letters+string.digits
    result="".join(random.choice(all) for _ in range(length))
    return result

@app.route('/',methods=['POST','GET'])
def go():
    global url_list
    url_list=store()
    if request.method =="POST":
        long_url=request.form['mainurl']
        for u in url_list:
            result = next((u['shorturl'] for key, value in u.items() if value == long_url), None)
            if result is not None:
                break
        if result is None:
            result = short_url()
            add(result,long_url)
        return render_template("redirect.html",val=f"{request.url_root}{result}")
    return render_template('main.html')

@app.route("/<result>")
def show(result):
    for u in url_list:
        redi = next((u['longurl'] for key, value in u.items() if value == result), None)
        if redi is not None:
            break
    if redi:
        return redirect(redi)
    else:
        return "Not found",404
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)