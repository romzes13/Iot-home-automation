import requests

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return 'Index Page Test'

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

@app.route('/temp')
def temp():
  #name=None ensures the code runs even when no name is provided
  #return render_template('user-profile.html', name=name)
  #make a POST request
  dictToSend = {'question':'what is the answer?'}
  res = requests.post('http://192.168.0.134/temp/', json=dictToSend)
  print ('response from server:',res.text)
  dictFromServer = res.json()
  print(dictFromServer)
  print("Dictionary python:")
  for x in dictFromServer:
      print(dictFromServer[x])

  fahrenheit = dictFromServer.get("Fahrenheit")
  humidity = dictFromServer.get("Humidity")
  temp = dictFromServer.get("Temperature")

  print("Fahrenheit=",fahrenheit)
  print("Humidity=",humidity)
  print("Temperature=",temp)

  #return dictFromServer
  return render_template('temperature.html', fahrenheit=fahrenheit, humidity=humidity, temp=temp)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
