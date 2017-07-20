from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from string import Template
from flask import Markup
import os
import psycopg2
import urlparse

#urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])
url = url['netloc']

print 'hello', url

"""conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)"""

app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/sample_db'
app.config['SQLALCHEMY_DATABASE_URI'] = url
db = SQLAlchemy(app)

class Example(db.Model):
	__tablename__ = 'example'
	word = db.Column('word', db.Unicode, primary_key=True)
	definition = db.Column('definition', db.Unicode)
	summary = db.Column('summary', db.Unicode)
	picture = db.Column('picture', db.Unicode)
	relatedterms = db.Column('related terms', db.Unicode)
	resources = db.Column('resources', db.Unicode)

	def __init__(self, word, definition, summary, picture, relatedterms, resources):
		self.word = word
		self.definition = definition
		self.summary = summary
		self.picture = picture
		self.relatedterms = relatedterms
		self.resources = resources


@app.route('/')
def home():
	return render_template("search-result-page-MOCKUP.htm")

@app.route('/<term>', methods=['GET', 'POST'])
def factsheet(term):
	if request.method=='POST':
		glossary = Example.query.filter_by(word = request.form['search'].lower()).first_or_404()
		return render_template("search-result-page-MOCKUP.htm",
		term = request.form['search'].lower(),
		definition = glossary.definition,
		summary = glossary.summary,
		picture = Markup(
			'<img src='+glossary.picture+'>'),
		#picture = glossary.picture,
		#relatedterms = glossary.relatedterms,
		relatedterms = Markup(
			'<a href="http://localhost:5000/'+glossary.relatedterms+'">'+glossary.relatedterms+'</a>'),
		#resources = glossary.resources)
		resources = Markup(
			'<iframe width="560" height="315" src='+glossary.resources+' frameborder="0" allowfullscreen></iframe>')
	)
	else:
		glossary = Example.query.filter_by(word = term.lower()).first_or_404()
		return render_template("search-result-page-MOCKUP.htm",
		term = term.lower(),
		definition = glossary.definition,
		summary = glossary.summary,
		#picture = glossary.picture,
		picture = Markup(
			'<img src='+glossary.picture+'>'),
		#relatedterms = glossary.relatedterms,
		relatedterms = Markup(
			'<a href="http://localhost:5000/'+glossary.relatedterms+'">'+glossary.relatedterms+'</a>'),
		resources = Markup(
			'<iframe width="560" height="315" src='+glossary.resources+' frameborder="0" allowfullscreen></iframe>')
	)
	return render_template("search-result-page-MOCKUP.htm")

if __name__=="__main__":
	app.run(debug=True)