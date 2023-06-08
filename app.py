from flask import Flask, request, render_template
import boto3
import dynamodb_handler as db


app = Flask(__name__)

@app.route('/')
def root_route():
 #db.create_table_movie()
 #return "Table created..."
 return render_template("index.html") 
 
@app.route('/movie',methods=['POST'])
def add_movie(): 
 
 data = request.form.to_dict()
 response = db.add_item_to_movie_table(int(data['id']), data['title'], data['director'])
 
 if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Added successfully',
        }

 return {  
        'msg': 'Some error occcured',
        'response': response
    }
 
if __name__ == '__main__':
 app.run(debug=True,port=8080,host='0.0.0.0')
