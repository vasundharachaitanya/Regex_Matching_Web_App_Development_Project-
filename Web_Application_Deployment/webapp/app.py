from flask import Flask, request, render_template, redirect, url_for
import re

app = Flask(__name__)

matched_item_list = []

@app.route('/')
def home():
    return render_template("home.html", matched_item_list=matched_item_list)

@app.route("/results", methods=["POST"])
def regex():
    text = request.form.get("text")
    pattern = re.compile(request.form.get("pattern"))
    matched_items = pattern.findall(text)
    matched_item_list.extend(matched_items)
    return redirect(url_for('home'))

@app.route("/validateemail", methods=["POST"])
def validating_email_id():
    email = request.form.get('email')
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    valid_email = bool(re.match(email_pattern, email))
    return render_template("home.html", email=email, valid_email=valid_email, matched_item_list=matched_item_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
