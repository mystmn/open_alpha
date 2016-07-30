from flask import Flask, render_template
import helpers, models, controllers, os

app = Flask(__name__)

config = {
    'rootPath': os.path.dirname(os.path.realpath(__file__)),
}


@app.route('/')
def default():
    controllers.account_holder()
    models.account_holder.insert_account_holder("ghost@gmail.com", "mystmn", "6142162858", "pacman")
    return render_template('default.html')


@app.route('/contacts', methods=['GET'])
def contact():
    entries = models.account_holder.select_account_holder()
    return render_template('contacts.html', entries=entries)


@app.context_processor
def inject_dict_for_all_templates():
    return dict(mydict=helpers.menu())


if __name__ == '__main__':
    app.run()
