


from flask import Flask, render_template, request, redirect,  url_for

app = Flask(__name__, template_folder = 'templates')

todos = [{"todo": "Sample Todo", "done": False}]

@app.route('/')
def index():
    return render_template('index_test.html', todos=todos)

if __name__ == '__main__':
    app.run(debug=True)         # why no indentation here? 










