from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return 'Index Page'

@app.route('/hello')
def hello():
  return 'Hello, greetings from different endpoint'

#adding variables
@app.route('/user/<username>')
def show_user(username):
  #returns the username
  return 'Username: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
  #returns the post, the post_id should be an int
  return str(post_id)

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    #check user details from db
    login_user()
  elif request.method == 'GET':
    #serve login page
    serve_login_page()

@app.route('/user1/<name>')
def hello1(name=None):
  #name=None ensures the code runs even when no name is provided
  return render_template('user-profile.html', name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
