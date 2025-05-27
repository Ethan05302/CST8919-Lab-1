from flask import Flask, redirect, render_template, session, url_for
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.secret_key = 'flask-auth0-demo-key'  


oauth = OAuth(app)
auth0 = oauth.register(
    'auth0',
    client_id=os.getenv('AUTH0_CLIENT_ID'),
    client_secret=os.getenv('AUTH0_CLIENT_SECRET'),
    client_kwargs={
        'scope': 'openid profile email'
    },
    server_metadata_url=f"https://{os.getenv('AUTH0_DOMAIN')}/.well-known/openid-configuration"
)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri=os.getenv("AUTH0_CALLBACK_URL"))


@app.route('/callback')
def callback():
    token = auth0.authorize_access_token()
    session['user'] = token['userinfo']
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    user = session.get('user')
    if not user:
        return redirect('/')
    return render_template('dashboard.html', user=user)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
