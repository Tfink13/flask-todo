from flask import Flask, request, abort, make_response, render_template, request, session



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)




    @app.route('/', methods=["GET", "POST", "DELETE", "PATCH", "PUT"])
    def index():
        readItems = open("todos.txt", 'r')
        message = readItems.read()
        print(message.split('||'))
        readItems.close()

        return render_template('base.html')
        
    @app.route('/update')
    def hello():

        for key, value in request.args.items():
            print(f"{key}: {value}")

        name = request.args.get('name', 'World')
        return f"Hello {name}!"


    return app
