
from flask import Flask, render_template, request
from flask_cors import CORS
import json
import changeExecuter
import os


app = Flask(__name__)
CORS(app)

#this takes care of adding any new field
@app.route('/addData',methods=["POST"])
def addData():
    data = request.get_json()
    print(data)
    # data = json.loads(data)
    new_value = data["value"]
    path_to_value = data["path"].split("$")

    # we will store these paths and values onto a new file, and batch process them later
    #we need to figure out the instruction number first
    numbers = [k for k in path_to_value if(k.isdigit())]
    instruction_id = ""
    for i in range(0, len(numbers)):
        if(i==0):
            instruction_id+=numbers[i]
        else:
            instruction_id+="."+str(int(numbers[i])+1) #adding 1 because it is 1.1 not 1.0
    

    with open('changes.txt', 'a+') as fp:
        fp.write(instruction_id +" "+ "ADD" + " " + new_value+ "\n")

    return "200"    


@app.route('/deleteData',methods=["POST"])
def deleteData():
    data = request.get_json()
    print(data)
    # data = json.loads(data)
    new_value = data["value"]
    path_to_value = data["path"].split("$")

    # we will store these paths and values onto a new file, and batch process them later
    #we need to figure out the instruction number first
    numbers = [k for k in path_to_value if(k.isdigit())]
    instruction_id = ""
    for i in range(0, len(numbers)):
        if(i==0):
            instruction_id+=numbers[i]
        else:
            instruction_id+="."+str(int(numbers[i])+1) #adding 1 because it is 1.1 not 1.0
    

    with open('changes.txt', 'a+') as fp:
        fp.write(instruction_id +" "+ "DELETE" + " " + new_value+ "\n")

    return "200"    



@app.route('/editInstruction',methods=["POST"])
def editInstruction():
    data = request.get_json()
    print(data)
    # data = json.loads(data)
    new_value = data["value"]
    path_to_value = data["path"].split("$")

    # we will store these paths and values onto a new file, and batch process them later
    #we need to figure out the instruction number first
    numbers = [k for k in path_to_value if(k.isdigit())]
    instruction_id = ""
    for i in range(0, len(numbers)):
        if(i==0):
            instruction_id+=numbers[i]
        else:
            instruction_id+="."+str(int(numbers[i])+1) #adding 1 because it is 1.1 not 1.0
    

    with open('changes.txt', 'a+') as fp:
        fp.write(instruction_id +" "+ "EDIT_INSTRUCTION" + " " + new_value+ "\n")

    return "200"    




@app.route('/refreshPage',methods=["GET"])
def refreshChanges():
    os.system('python3 textExtractor_v1.py')
    return "200"  


    
if __name__ == '__main__':
    app.run(debug=True)



