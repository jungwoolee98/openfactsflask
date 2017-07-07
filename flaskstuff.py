from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://@localhost/sample_db'
db = SQLAlchemy(app)

class Example(db.Model):
	__tablename__ = 'example'
	id = db.Column('id', db.Integer, primary_key=True)
	word = db.Column('word', db.Unicode)
	definition = db.Column('definition', db.Unicode)
	summary = db.Column('summary', db.Unicode)
	exercises = db.Column('exercises', db.Unicode)
	resources = db.Column('resources', db.Unicode)

	def __init__(self,id, word, definition, summary, exercises, resources):
		self.id = id
		self.word = word
		self.definition = definition
		self.summary = summary
		self.exercises = exercises
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
		exercises = glossary.exercises,
		resources = glossary.resources)
	else:
		glossary = Example.query.filter_by(word = term.lower()).first_or_404()
		return render_template("search-result-page-MOCKUP.htm",
		term = term.lower(),
		definition = glossary.definition,
		summary = glossary.summary,
		exercises = glossary.exercises,
		resources = glossary.resources)
	return render_template("search-result-page-MOCKUP.htm")

if __name__=="__main__":
	app.run(debug=True)