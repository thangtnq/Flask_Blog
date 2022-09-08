from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Thang',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'April 20, 2021'
    },

    {
        'author': 'Andy',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 20, 2011'
    }
]

@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html', posts=posts)


@app.route("/about")

def about():
    return render_template('about.html', title = 'About')

if __name__ == '__main__':
    app.run(debug = True)