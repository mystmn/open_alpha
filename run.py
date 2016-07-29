from flask import Flask, render_template, url_for
from models import account_holder

app = Flask(__name__)


@app.route('/')
def default():
    account_holder.insert_account_holder("pcameron52@gmail.com", "mystmn", "6142162858", "pacman")
    return render_template('default.html')


@app.route('/contacts', methods=['GET'])
def contact():
    entries = account_holder.select_account_holder((), 4)
    return render_template('contacts.html', entries=entries)


@app.context_processor
def inject_dict_for_all_templates():
    return dict(mydict=menu())


def menu():
    return {
        'Contact Us': '.contact',
        'Home': '.default',
    }


if __name__ == '__main__':
    app.run()
