from flask import Flask, render_template, jsonify, request, redirect, url_for
import string
import random
from database import add, fetch_shorturl
import validators
app = Flask(__name__)


def short_url(length=6):
    all = string.ascii_letters+string.digits
    result = "".join(random.choice(all) for _ in range(length))
    return result


def is_valid_url(url):
    if validators.url(url):
        return url
    else:
        return False


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/url', methods=['POST', 'GET'])
def url():
    error_message=''
    if request.method == "POST":
        long_url = is_valid_url(request.form['mainUrl'])
        if long_url:
            result = fetch_shorturl(
                "SELECT shorturl FROM url_shorts WHERE longurl LIKE :val;", long_url)
            if result is None:
                result = short_url()
                add(result, long_url)
            return render_template('index.html', shortURL=f"{request.url_root}{result}")
        else:
            error_message = "The provided URL is not valid. Please enter a valid URL."
    return render_template('index.html', error=error_message)


@app.route("/<result>")
def show(result):
    check = fetch_shorturl(
        "SELECT longurl FROM url_shorts WHERE shorturl LIKE :val;", result)
    if check is None:
        return render_template('404.html')
    else:
        return redirect(str(check))


if __name__ == "__main__":
    app.run(port=4000,host='0.0.0.0', debug=True)
