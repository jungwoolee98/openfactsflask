from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/factsheet/')
def factsheet():
	return render_template("search-result-page-MOCKUP.htm")

if __name__=="__main__":
	app.run(debug=True)