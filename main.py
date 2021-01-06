from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
import mysql.connector
from sqlfile import db
from os.path import join, dirname, realpath

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER



# Root URL
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route("/record", methods=['POST'])
def record():
    mycursor = db.cursor()
    carid = request.form['carid']
    print('order id :'+carid)
    mycursor.execute("select * from cars where carid="+carid)
    Carrows = []
    for x in mycursor:
        Carrows.append(x)
        print(x)
        print()
    mycursor.close()
    return render_template("results.html", len = len(Carrows),Carrows = Carrows)



# Get the uploaded files
@app.route("/", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)

           parseCSV(file_path)
          # save the file
      return redirect(url_for('index'))

def parseCSV(filepath):
    col_names = ['location', 'price', 'brand', 'model', 'variant', 'year', 'fuel', 'transmission', 'kms', 'owners']
    csvData = pd.read_csv(filepath, names=col_names, header=None)
    mycursor = db.cursor()
    for i, row in csvData.iterrows():
        try:

            mySql_insert_query = """INSERT INTO cars (location,brand,owners) VALUES (%s, %s, %s) """
            if row['location'] and row['brand'] and row['owners']:
                recordTuple = (row['location'],row['brand'],row['owners'])
                mycursor.execute(mySql_insert_query, recordTuple)

            print(i, row['location'],row['brand'],row['owners'])


        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
    mycursor.close()
    db.commit()


if (__name__ == "__main__"):
     app.run(port = 5000)