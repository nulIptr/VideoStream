"""
This script runs the VideoStream application using a development server.
"""


from VideoStream import create_app


if __name__ == '__main__':
    #HOST = environ.get('SERVER_HOST', 'localhost')
    #try:
    #    PORT = int(environ.get('SERVER_PORT', '5555'))
    #except ValueError:
    #    PORT = 5555
    app=create_app()
    app.run()

