from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        for k in result:
            print(result.get(k))
        return render_template('result.html', result = result)


@app.route('/hello/<something>')
def hello_name(something):
    list = ['John', 'James', 'Janice']
    return render_template('hello.html', user_name = something, names = list)

@app.route('/user/<name>')
def hello(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest_name = name))

@app.route('/guest/<guest_name>')
def guest(guest_name):
    return 'Hello {} as guest'.format(guest_name)

@app.route('/admin')
def admin():
    return 'Hello admin'

if __name__ == '__main__':
    app.run()
