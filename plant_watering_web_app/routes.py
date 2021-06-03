from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return "Leo will control his plant watering system from all over the world with this web app!"


@app.route('/control-center.html')
def control_center():
    message = 'Hello World'
    return render_template('control-center.html', message=message)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
