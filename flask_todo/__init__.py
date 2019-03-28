from flask import Flask, request, render_template, request, flash


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # ask zach about this
    app.config.from_mapping(
        SECRET_KEY='dev',
        # ask zach
        DB_NAME='flask_todo',
        DB_USER='csetuser',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
 # each time we are running the command

    from . import db
    db.init_app(app)

    @app.route('/', methods=["GET", "POST"])
    def index():
        if request.method == 'POST':
            # this is where i want to send data to database not txt file


            firstname = request.form['firstname']
            lastname = request.form['lastname']
            todo = request.form['todo']
            error = None
            if not firstname:
                error = 'You must enter a first name'
            elif not lastname:
                error = 'You must enter a last name.'
            elif todo == 'Enter task:' or not todo:
                error = 'You must enter a task for your task manager.'
            else:
                readItems = open("todos.txt", 'a')
                readItems.write(firstname + " " + lastname + ": " + todo + '\n')
                readItems.close()

            flash(error)

        return render_template('base.html')


        # def index():
        #     error = None
        #     if request.method == 'POST':
        #         if request.form['firstname'] == None or request.form['lastname'] == None:
        #                 error = 'You did not properly fill out the todo manager'
        #         else:
        #             readItems = open("todos.txt", 'a')
        #             readItems.write(firstname + " " + lastname + ": " + todo + '\n')
        #             readItems.close()
        #             flash('Your task has been added to the ')
        #             return redirect(url_for('/'))
        #     return render_template('base.html', error=error)


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

    @app.route('/create')
    def create():
        pass
        # this is where i want to mark my list to
        # do somehting to my list



    return app
