This is the code for the web Flask app, OpenFax, that is being hosted on heroku.

It is a website that dynamically generates factsheets for an OpenStax textbook by pulling in information from a postgresql database.

There are some 2000 factsheets available.

Each factsheet is composed of the following: the term, definition, summary, picture, recommended resources, and related terms.

Term - A glossary term pulled from the OpenStax Biology textbook using a parser.

Definition - A definition term pulled from the OpenStax Biology textbook using a parser.

Summary - Initially, idea was to generate summaries for all the terms using the textbook. However, this proved to be very difficult, as some glossary terms had only two sentences in the textbook, making it impossible to generate a good summary. Tried various different NLP packages and libraries such as nltk, spaCy, etc. Eventually, just decided to web scrape data from Simple Wikipedia to generate summaries.

Picture - A picture pulled from the OpenStax Biology textbook.

Recommended resources - Generated some recommended resources through web scraping. Currently only consists of YouTube videos relating to the term.

Related terms - Constructed a weighted graph with nodes as glossary terms, and the edges' weights being the number of times they appeared together within the same sentence or adjacent sentences. For each glossary term, linked to the 3 closest terms.

![image](https://user-images.githubusercontent.com/25090490/30838453-33fd7506-a231-11e7-8d9e-6267e9c9f109.png)

