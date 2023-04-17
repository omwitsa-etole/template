"""
A simple flask server for your app
"""

from flask import Flask, render_template, request, redirect, url_for, session, abort, flash,Response

app = Flask(__name__)

#all templates are stored in the templates directory relative to main.py file location
#static files are store in the static directory relative to main.py

"""
Python is strict on spacing i.e has no curly brackets for function definitions, you have to write clean code to avoid errors
"""

@app.route("/")
def home():
	#add your code or render a template using return render_template(template_name,**locals())
	return render_template(templatename,**locals()) #renders the specified template with local variables

	pass

@app.route("/booking",methods=["GET","POST"])
def booking():
	if request.method == "POST":
		#if a post request is made to server
		#have your code here
		pass
	return render_template(templatename) #renders the specified template without local variables

if __name__ == "__main__":
	app.run("0.0.0.0")#run server on all addresses