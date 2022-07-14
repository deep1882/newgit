from unicodedata import name
from flask import Flask, render_template, request, redirect
import sqlite3 as sql
import os
from google.cloud import datastore



app = Flask(__name__)

# app.py

# Required imports
import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

os.environ['GOOGLE_APPLICATION_CREDENTIALS']="bq-practice-tatvic-9ad770c552ad.json"
datastore_client = datastore.Client()
# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB


@app.route('/')
def new_student():
   return render_template('/student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         Name = request.form['Name']
         Address = request.form['Address']
         City = request.form['City']
         Pincode = request.form['Pincode']

         
         datastore_client = datastore.Client()

         kind = "deep"
         name = "sampletask1"

         task_key = datastore_client.key(kind, name)
         task = datastore.Entity(key=task_key)
         task["Address"] = Address
         task["City"] = City
         task["Name"] = Name
         task["Pincode"] = Pincode
         print(Address)
         print(City)
         print(Name)
         print(Pincode)

     

         # Saves the entity
         datastore_client.put(task)
         msg = "Record successfully added"
         

         
         


      except:
         
         msg = "error in insert operation"
      
      finally:
 

         return render_template("/student.html",msg = msg)
         con.close()




if __name__ == '__main__':
      app.run(host="0.0.0.0",port=8080)
