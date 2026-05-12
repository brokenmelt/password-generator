from flask import Flask,render_template,request
import random
import string
app = Flask(__name__)
@app.route("/",methods = ["GET","POST"]) #homepage (/_)
def home ():
    password =""
    if request.method == "POST":
        length = int(request.form["length"])
        mode = request.form["mode"]
        if mode == "easy":
         characters = string.ascii_letters
         password =""

        elif mode == "moderate" :
           characters = string.ascii_letters+string.digits
           password =""
        else :
           characters = string.ascii_letters+string.digits+"!@#$%"
           password =""
        
        for i in range (length):
          password += random.choice(characters)


    return render_template("index.html",password = password)
app.run(debug=True)