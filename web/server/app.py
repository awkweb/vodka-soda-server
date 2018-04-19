from flask import Flask, render_template


app = Flask(
    __name__,
    template_folder='templates',
    static_folder='../static',
)


@app.route('/')
def index():
    return render_template('pages/index.html')


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404
