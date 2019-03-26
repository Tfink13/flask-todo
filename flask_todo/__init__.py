from flask import Flask, request, abort, make_response



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index():

        print('-' * 20)
        print(f"Base URL: {request.base_url}")
        print('-' * 20)

        print('-' * 20)
        print(f"URL Root: {request.url_root}")
        print('-' * 20)

        return 'This is a flask-boilerplate project, not to be used in production.'

    @app.route('/hello')
    def hello():

        for key, value in request.args.items():
            print(f"{key}: {value}")

        name = request.args.get('name', 'World')
        return f"Hello {name}!"


    @app.route('/number/<int:num>')
    def number_route(num):
        return f"Number: {num}"

    @app.route('/method', methods=['GET', 'POST', 'DELETE', 'PATCH', 'PUT'])
    def method_route():
        return f"HTTP Method: {request.method}"

    @app.route('/status')
    def status_route():
        code = request.args.get('c', 200)
        if code == 200:
            return f"{code} OKAY"
        else:
            response = make_response("", code)
        return response


    return app
