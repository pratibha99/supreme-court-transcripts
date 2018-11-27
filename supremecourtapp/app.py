#!/usr/bin/env python

import flask
from flask import Response, request, send_file
import json
import sqlite3
import csv
import sys

# Create the application.
app = flask.Flask(__name__)

@app.route('/')
def index():
	"""
	Displays the home page that leads users into different pages
	"""
	#return flask.render_template('index.html')

	year = request.args.get("year", "")
	month = request.args.get("month", "")
	day = request.args.get("day", "")
	title = request.args.get("title", "")
	topic = request.args.get("topic", "")
	name = request.args.get("name", "")

	connection = sqlite3.connect("database.db")
	connection.row_factory = dictionary_factory
	cursor = connection.cursor()

	#Query that gets the records that match the query
	all_records_query = "SELECT cases.title,cases.date,cases.top5,cases.act as acts,\
						speech.name as person,speech.text,speech.score FROM cases INNER \
						JOIN speech on cases.case_id = speech.case_id %s %s;"
	unselected_queries = []
	records_total = []
	where_clause = ""
	where_array = []
	condition_tuple = []
	if name or year or month or day or title or topic:
		where_clause += "where "
		if name:
			where_array.append("speech.name like ? ")
			condition_tuple.append(str(name))
		else:
			unselected_queries.append('Name')
		if title:
			where_array.append("cases.title like ? ")
			condition_tuple.append("%" + title + "%")
		else:
			unselected_queries.append('Title')
		if topic:
			where_array.append("cases.topic = ? ")
			condition_tuple.append(str(topic))
		else:
			unselected_queries.append('Topic')
		if day:
			where_array.append("cases.day = ? ")
			condition_tuple.append(str(day))
		else:
			unselected_queries.append('Day')
		if month:
			where_array.append("cases.month = ? ")
			condition_tuple.append(str(month))
		else:
			unselected_queries.append('Month')
		if year:
			where_array.append("cases.year = ? ")
			condition_tuple.append(str(year))
		else:
			unselected_queries.append('Year')


		where_clause += "and ".join(where_array)
		print(where_clause, file=sys.stderr)
		condition_tuple = tuple(condition_tuple)

		print(condition_tuple, file = sys.stderr)
		limit_statement = "ORDER BY year DESC, month DESC, day DESC LIMIT 5"
		# print(where_clause)
		# print(limit_statement)
		all_records_query = all_records_query % (where_clause, limit_statement)
		print(all_records_query, file = sys.stderr)
		cursor.execute(all_records_query, condition_tuple)
		records = cursor.fetchall()
		connection.close()



	else:
		records = None

	years = [x for x in range(2018, 2000, -1)]
	days = [x for x in range(1, 31, 1)]
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	topics = ["Government action in relation to immigration", "Beneficiaries’ rights to property in an estate", "Trial process for criminal matters", "Damage to persons through injury", "Company financial flows", "Jurisdictional divisions and actions", "Employment entitlements and disputes", "Land contracts and agreements", "Constitutional actors and relationships", "Trade licensing, regulation and IP", "Other"]

	selected_dict = {}
	selected_dict["year"] = int(year) if year else None
	selected_dict["month"] = month if month else None
	selected_dict["day"] = int(day) if day else None
	selected_dict["topic"] = topic if topic else None
	return flask.render_template('index.html',records= records, days = days, years = years,
	months = months, selected_dict = selected_dict, title = title, name = name, topics = topics)

@app.route('/speakers')
def speakers():
	"""
	This is how arguments are passed from the View to this controller
	The get request can look like this:
	/speakers?name=rubio&format=csv
	This tells the controller to get all speeches by rubio in a csv format
	/speakers?name=rubio
	the url above just tells the controller to get speeches by rubio and display them
	/speakers
	The url above simply asks for all speeches to be displayed
	/speakers?format=csv
	Asks for all speeches to be made available in csv format
	"""

	format_ = request.args.get("format", None)
	speaker = request.args.get("name", "")

	connection = sqlite3.connect("mydatabase.sqlite")
	connection.row_factory = dictionary_factory
	cursor = connection.cursor()

	#Query that gets the records that match the query
	all_records_query = "SELECT hearing.hearing_title as title, hearing.date as date, speech.text as text, \
				speaker.surname as name FROM hearing inner join speech on \
				speech.hearing_id = hearing.hearing_id inner join speaker \
				on speaker.speech_id = speech.speech_id %s %s;"

	where_clause = ""
	if speaker:
		where_clause = "where speaker.surname = ? " if speaker else ""

	limit_statement = "limit 20" if format_ != "csv" else ""

	all_records_query = all_records_query % (where_clause, limit_statement)

	if speaker:
		cursor.execute(all_records_query ,(speaker.lower(),))
	else:
		cursor.execute(all_records_query)
	records = cursor.fetchall()

	connection.close()

	#Send the information back to the view
	#if the user specified csv send the data as a file for download else visualize the data on the web page
	if format_ == "csv":
		return download_csv(records, "speeches_%s.csv" % (speaker.lower()))
	else:
		years = [x for x in range(2018, 1995, -1)]
		return flask.render_template('speaker.html', records=records, speaker=speaker, years=years)

########################################################################
# The following are helper functions. They do not have a @app.route decorator
########################################################################
def dictionary_factory(cursor, row):
	"""
	This function converts what we get back from the database to a dictionary
	"""
	d = {}
	for index, col in enumerate(cursor.description):
		d[col[0]] = row[index]
	return d

def download_csv(data, filename):
	"""
	Pass into this function, the data dictionary and the name of the file and it will create the csv file and send it to the view
	"""
	header = data[0].keys() #Data must have at least one record.
	with open('downloads/' + filename, "w+") as f:
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(header)
		for row in data:
			writer.writerow(list(row.values()))

	#Push the file to the view
	return send_file('downloads/' + filename,
				 mimetype='text/csv',
				 attachment_filename=filename,
				 as_attachment=True)


if __name__ == '__main__':
	app.debug=True
	app.run()
