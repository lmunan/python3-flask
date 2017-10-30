from flask import Flask
app=Flask(__name__)

@app.route('/shiyanlou/<name>')

def hello_world(name):
    return '<h1> Hello, %s!' %name
if __name__=='__main__':
    app.run(debug=True)
