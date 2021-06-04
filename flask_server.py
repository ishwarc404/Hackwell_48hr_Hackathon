
from flask import Flask, render_template, request, Response
from flask_cors import CORS
import json
import changeExecuter
import os


app = Flask(__name__)
CORS(app)

#this takes care of adding any new field
@app.route('/addDataUnit',methods=["POST"])
def addDataUnit():
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
        fp.write(instruction_id +" "+ "ADD_UNIT" + " " + new_value+ "\n")

    return render_template("webpage.html")    


@app.route('/deleteDataUnit',methods=["POST"])
def deleteDataUnit():
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
        fp.write(instruction_id +" "+ "DELETE_UNIT" + " " + new_value+ "\n")

    return render_template("webpage.html")    


#this takes care of adding any new field
@app.route('/addDataType',methods=["POST"])
def addDataType():
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
        fp.write(instruction_id +" "+ "ADD_TYPE" + " " + new_value+ "\n") #ADD IS NOTHING BUT MODIFY

    return render_template("webpage.html")    


@app.route('/deleteDataType',methods=["POST"])
def deleteDataType():
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
        fp.write(instruction_id +" "+ "DELETE_TYPE" + " " + new_value+ "\n")

    return render_template("webpage.html")    


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

    return render_template("webpage.html")    


@app.route('/batchUpdate',methods=["POST"])
def batchUpdate():
    data = request.get_json()
    print(data)
    # data = json.loads(data)
    new_value = data["value"]
    path_to_values = data["path"]
    
    value_type = data["valueType"] #VALUE TYPE OR UNIT
    TYPE_OF_UPDATE = "ADD_TYPE"
    if(value_type == 'unitadd'):
        TYPE_OF_UPDATE = "ADD_UNIT"
    if(value_type == 'unitdelete'):
        TYPE_OF_UPDATE = "DELETE_UNIT"




    single_paths = []
    for each in path_to_values:
        single_paths.append(each.split("$"))


    # we will store these paths and values onto a new file, and batch process them later
    #we need to figure out the instruction number first
    final_paths =  []

    for each in single_paths:
        numbers = [k for k in each if(k.isdigit())]
        instruction_id = ""
        for i in range(0, len(numbers)):
            if(i==0):
                instruction_id+=numbers[i]
            else:
                instruction_id+="."+str(int(numbers[i])+1) #adding 1 because it is 1.1 not 1.0
    

        with open('changes.txt', 'a+') as fp:
            fp.write(instruction_id +" "+ TYPE_OF_UPDATE + " " + new_value+ "\n")

    


@app.route('/refreshPage',methods=["GET"])
def refreshChanges():
    os.system('python3 textExtractor_v1.py')
    return render_template("webpage.html")
    return render_template("webpage.html")  


@app.route("/exportJSON")
def exportJSON():
    with open("result.json") as fp:
        json = fp.read()
    return Response(
        json,
        mimetype="text/json",
        headers={"Content-disposition":
                 "attachment; filename=result.json"})

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        os.system('python3 textExtractor_v1.py')
        return render_template("webpage.html")

    return render_template("webpage.html")


@app.route('/jsonViewer', methods = ['GET', 'POST'])
def jsonViewer():
      return render_template("jsonViewer.html")



@app.route('/', methods = ['GET', 'POST'])
def main():
    return render_template("index.html")


if __name__ == '__main__':
    
    # we need to clear the text file now
    file =  open('changes.txt', 'r+')
    file.truncate(0)
    file.close
    
    app.run(debug=True)



