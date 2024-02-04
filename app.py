import os
import bson
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient 
from pymongo.collection import Collection
from pymongo.database import Database

from bson.objectid import ObjectId

# acessing the MangoDB Altas Cluster
# load_dotenv()
# connection_string : str = os.environ.get('CONNECTION_STRING')
connection_string = 'mongodb+srv://junling:Wojiaozjy1999.@flaskmangodb.v8f3vni.mongodb.net/?retryWrites=true&w=majority'
mongo_client:MongoClient = MongoClient(connection_string)

#  add the database name and collection name from Atlas
database:Database = mongo_client.get_database('flask_database')
collection:Collection = database.get_collection('todos')



app: Flask = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        collection.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))
    
    all_todos = collection.find()
    return render_template('index.html', todos=all_todos)


@app.post('/<id>/delete')
def delete(id):
    collection.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

