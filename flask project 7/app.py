import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'


blueprint = make_google_blueprint(client_id='1046827732053-cq06kjjma2lalcfqmil3f24hspjbf0ti.apps.googleusercontent.com',
                                  client_secret='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', 
                                  offline=True, scope=['profile', 'email'])


app.register_blueprint(blueprint, url_prefix='/login')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template(url_for('google.login'))
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']

    return render_template('welcome.html', email=email)


if __name__ == '__main__':
    app.run()