import random
from flask import Flask, request, render_template, jsonify, redirect

app = Flask(__name__)
# When this is True, when you edit this file, the server automatically picks up the changes and refreshes! Wow!
# It will also give you nice error messages if you fuck up
# Turn this to False when your app is done, so hackers can't mess up your cool app!
app.debug = True

# This is a janky and bad way to store data for our app.
# In reality, we would use a nice database like Redis, Postgres, MySQL, MongoDB, whatever...
memory = {'fave': 'placeholder'}


@app.route('/')
def home():
    return render_template('index.html')


# When we call http://127.0.0.1:5000/number/124,
# Flask grabs 124, checks that it is an int, and passes it as an argument to get_number_info(number)
@app.route('/number/<int:number>')
def get_number_info(number):
    # Check it out! We can do fancy computation on the back-end!
    squared = number ** 2
    # Look at number.html to see how `number` and `squared` are used
    return render_template('number.html', number=number, squared=squared)


@app.route('/random')
def get_random():
    return render_template('random.html')


@app.route('/gimme')
def get_random_number():
    number = random.randint(0, 1000)
    square_root = "%.3f" % (number ** 0.5)
    # Takes the Python dictionary and makes it into JSON to return
    return jsonify({"num": random.randint(0, 1000), "sqrt": square_root})


@app.route('/form')
def get_form_page():
    return render_template('form.html', favorite=memory['fave'])


# Don't call directly, takes input from a form
@app.route('/favorite', methods=['POST'])
def take_form_results():
    memory['fave'] = request.form.get('word')
    # Redirects back to the form page
    return redirect('/form')


if __name__ == '__main__':
    # This starts the server. Just run `python server.py` to start the app.
    app.run()
