from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = (
    {
        'author': 'Hatsuki',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
     {
        'author': 'Hatsuki',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
)

@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    str = "Hatsuki"
    return render_template('index.html', title='flask test', name=str,
                           posts=posts)

@app.route('/about')
def about():
    return 'About'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)