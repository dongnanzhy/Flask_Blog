## import from package __init__ file
from flaskblog import app


if __name__ == '__main__':
    app.run(debug=True)