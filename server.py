from flask import Flask, render_template, url_for, request
import csv

from jinja2.lexer import newline_re

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template('index.html')


@app.route("/<string:pathname>")
def show_pathname(pathname):
    return render_template(pathname)


@app.route('/submit_form', methods=['POST', 'GET'])
def form_submitted():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('/thankyou.html')
    else:
        error = 'something went wrong, try again!'


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# def write_to_file(data):
#     with open('database.txt', mode = 'a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{email},{subject},{message}')

# @app.route("/index.html")
# def home_page():
#     return render_template('index.html')
#
#
# @app.route("/works.html")
# def works_page():
#     return render_template('works.html')
#
#
# @app.route("/about.html")
# def about_page():
#     return render_template('about.html')
#
#
# @app.route("/contact.html")
# def contact_page():
#     return render_template('contact.html')
