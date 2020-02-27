from flask import Flask
from database import get_db
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

def db_test():
    client, database = get_db()

    with client.start_session() as session:
    	

@app.route('/reverse/<word>')
def reverse(word):
    ret = word[::-1]
    return ret

if __name__ == '__main__':
    app.run(debug=True)