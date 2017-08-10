from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from string import Template
from flask import Markup
import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])
#url = 'postgres://' + url.netloc

#print 'hello', url

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/sample_db'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://tqgafpsayuwpzs:6eb68d4cef7cf0d4fda49977c92b5ca1a5ee826e779352b5aea2237c0c49cfec@ec2-54-243-252-232.compute-1.amazonaws.com:5432/dffvjushfn5ec0"
db = SQLAlchemy(app)

class Example(db.Model):
	__tablename__ = 'example'
	word = db.Column('word', db.Text, primary_key=True)
	definition = db.Column('definition', db.Text)
	summary = db.Column('summary', db.Text)
	picture = db.Column('picture', db.Text)
	relatedterm0 = db.Column('related term 0', db.Text)
	relatedterm1 = db.Column('related term 1', db.Text)
	relatedterm2 = db.Column('related term 2', db.Text)
	resources = db.Column('resources', db.Text)

	def __init__(self, word, definition, summary, picture, relatedterm0, relatedterm1, relatedterm2, resources):
		self.word = word
		self.definition = definition
		self.summary = summary
		self.picture = picture
		self.relatedterm0 = relatedterm0
		self.relatedterm1 = relatedterm1
		self.relatedterm2 = relatedterm2
		self.resources = resources


@app.route('/')
def home():
	return render_template("sample-page.htm")

@app.route('/<term>', methods=['GET', 'POST'])
def factsheet(term):
	if request.method=='POST':
		glossary = Example.query.filter_by(word = request.form['search'].lower()).first_or_404()
		return render_template("sample-page.htm",
		term = request.form['search'].lower(),
		definition = glossary.definition,
		summary = glossary.summary,
		picture = Markup(
			'<img src='+glossary.picture+' width="90%">'),
		#picture = glossary.picture,
		#relatedterms = glossary.relatedterms,
		relatedterm0 = Markup(
			'<a href="http://openfax.herokuapp.com/'+glossary.relatedterm0+'">'+glossary.relatedterm0+'</a>'),
		relatedterm1 = Markup(
			'<a href="http://openfax.herokuapp.com/'+glossary.relatedterm1+'">'+glossary.relatedterm1+'</a>'),
		relatedterm2 = Markup(
			'<a href="http://openfax.herokuapp.com/'+glossary.relatedterm2+'">'+glossary.relatedterm2+'</a>'),
		#resources = glossary.resources)
		resources = Markup(
			'<object width="90%" height="50%" data='+glossary.resources+' </object>')
	)
	else:
		glossary = Example.query.filter_by(word = term.lower()).first_or_404()
		return render_template("sample-page.htm",
		term = term.lower(),
		definition = glossary.definition,
		summary = glossary.summary,
		#picture = glossary.picture,
		picture = Markup(
			'<img src='+glossary.picture+' width="90%">'),
		#relatedterms = glossary.relatedterms,
		relatedterm0 = Markup(
			'<a href="http://openfax.herokuapp.com/'+glossary.relatedterm0+'">'+glossary.relatedterm0+'</a>'),
		relatedterm1 = Markup(
			'<a href="http://openfax.herokuapp.com/'+glossary.relatedterm1+'">'+glossary.relatedterm1+'</a>'),
		relatedterm2 = Markup(
			'<a href="http://openfax.herokuapp.com/'+glossary.relatedterm2+'">'+glossary.relatedterm2+'</a>'),
		resources = Markup(
			'<iframe width="90%" height="35%" src='+glossary.resources+' frameborder="0" allowfullscreen></iframe>')
	)
	return render_template("sample-page.htm")

if __name__=="__main__":
	app.run(debug=True)