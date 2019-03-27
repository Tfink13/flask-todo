from flask import Flask, request, render_template, request, flash



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)




    @app.route('/', methods=["GET", "POST"])
    def index():
        if request.method == 'POST':
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            todo = request.form['todo']
            error = None
            if firstname == None:
                error = 'You must enter a first name'
            elif not lastname:
                error = 'You must enter a last name.'
            elif todo == 'Enter task:' or not todo:
                error = 'You must enter a task for your task manager.'
            if error is None:
                readItems = open("todos.txt", 'a')
                readItems.write(firstname + " " + lastname + ": " + todo + '\n')
                readItems.close()

            flash(error)

        return render_template('base.html')

    @app.route('/list')
    def list():
        if request.method == 'GET':
            readItems = open('todos.txt', 'r')
            tasks = readItems.readline()
            for line in tasks:
                print(line)
            readItems.close()

            while True:
                return render_template('list.html')

        for key, value in request.args.items():
            print(f"{key}: {value}")

        # name = request.args.get('name', 'World')
        # return f"Hello {name}!"



    return app
