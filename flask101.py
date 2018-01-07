from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/template/<user>')
def template(user):
    return render_template('hello.html', name = user)

@app.route('/show_result/<int:score>')
def show_result(score):
    return render_template('result.html', marks = score)

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello {} as guest'.format(guest)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

@app.route('/success/<name>')
def success(name):
    return 'Welcome {}'.format(name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))

@app.route('/hello/<name>')
def hello(name):
    return 'Hello {}'.format(name)

@app.route('/blog/<int:post_id>')
def show_blog(post_id):
    return 'Blog {:d}'.format(post_id)

if __name__ == '__main__':
    app.run(port='80')
