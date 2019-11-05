from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is a Flaak application.'

#app.run('0.0.0.0:8080', debug=True)

if __name__ == '__main__':
    app.run()


    #this is a comment.