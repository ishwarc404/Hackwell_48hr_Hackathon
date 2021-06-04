def init():
    return "<html><script>;var batchIds = [];function batchUpdateValueType(t){batchIds.push(t);};function batchUpdateValueTypeBackend(valueType){var a=prompt('Please enter the value:'),n={path:batchIds,value:a, valueType: valueType};var e=new XMLHttpRequest();e.open('POST','http://127.0.0.1:5000/batchUpdate',true);e.setRequestHeader('Content-type','application/json');e.send(JSON.stringify(n))};function editInstruction(t){var a=prompt('Please enter the new task details:'),n={path:t,value:a};var e=new XMLHttpRequest();e.open('POST','http://127.0.0.1:5000/editInstruction',true);e.setRequestHeader('Content-type','application/json');e.send(JSON.stringify(n))};function refresh(){var e=new XMLHttpRequest();e.open('GET','http://127.0.0.1:5000/refreshPage',true);e.send()};function addValueUnit(t){var a=prompt('Please enter a new value which you want to include:'),n={path:t,value:a};var e=new XMLHttpRequest();e.open('POST','http://127.0.0.1:5000/addDataUnit',true);e.setRequestHeader('Content-type','application/json');e.send(JSON.stringify(n))};function deleteValueUnit(t){var a=prompt('Please enter the value which you want to remove:'),n={path:t,value:a};var e=new XMLHttpRequest();e.open('POST','http://127.0.0.1:5000/deleteDataUnit',true);e.setRequestHeader('Content-type','application/json');e.send(JSON.stringify(n))};function deleteValueType(t){var a=prompt('Please enter the type which you want to remove:'),n={path:t,value:a};var e=new XMLHttpRequest();e.open('POST','http://127.0.0.1:5000/deleteDataType',true);e.setRequestHeader('Content-type','application/json');e.send(JSON.stringify(n))};function addValueType(t){var a=prompt('Please enter the value type which you want to add:'),n={path:t,value:a};var e=new XMLHttpRequest();e.open('POST','http://127.0.0.1:5000/addDataType',true);e.setRequestHeader('Content-type','application/json');e.send(JSON.stringify(n))};</script><link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'>"

def finalise():
    return "</html>"

def divWrapperBegin():
    return "<div style='border: solid 1px black; margin:10 10 10 10px; padding: 10 10 10 10px; width:50vw;''>"

def divWrapperEnd():
    return "</div>"

def createInput(submodule, path):
    value_reference_path = ""
    for each in path:
        value_reference_path += str(each) + "$"

    outerdiv_start = "<div class='d-flex inline' style='margin-bottom:10px'>"

    #can help change batch value
    batch_mode_checkbox = "<input type='checkbox' style='margin-right:10px ; margin-top:5px' id={} onclick='batchUpdateValueType(this.id);'>".format(value_reference_path)
    label = "<br><h6 id='{}' style='margin-right:10px ; margin-top:5px'>{} {} </h6>".format(value_reference_path,submodule["Id"], submodule["Description"])
    field = ""
    if(submodule["Value Required"]):
        value_reference_path+="Value Unit" #adding the index to the reference path
        field = "<select id='{}'>".format(value_reference_path)
        for each_option in range(0,len(submodule["Value Unit"])):
            field += "<option id='{}' value='{}'>{}</option>".format(value_reference_path+'$' + str(each_option),submodule["Value Unit"][each_option],submodule["Value Unit"][each_option])

        field += "</select>"

        field += "<button id='{}' style='margin-left:10px' class='btn btn-primary' onclick=addValueUnit(this.id)>+</button>".format(value_reference_path)
        field += "<button id='{}' style='margin-left:10px' class='btn btn-danger' onclick=deleteValueUnit(this.id)>-</button>".format(value_reference_path)

    
        value_reference_path+="Value Type" #adding the index to the reference path
        field += "<select id='{}' style='margin-left:10px'  >".format(value_reference_path)
        field += "<option id='{}' value='{}'>{}</option>".format(value_reference_path+'$' + str("Value Type"),submodule["Value Type"],submodule["Value Type"])

        field += "</select>"

        field += "<button id='{}' style='margin-left:10px' class='btn btn-primary' onclick=addValueType(this.id)>+</button>".format(value_reference_path)
        field += "<button id='{}' style='margin-left:10px' class='btn btn-danger' onclick=deleteValueType(this.id)>-</button>".format(value_reference_path)


        #adding the add field button
    field += "<button id='{}' style='margin-left:10px' class='btn btn-secondary' onclick=editInstruction(this.id)>Edit Task</button>".format(value_reference_path)

    outerdiv_end = "</div>"
    return outerdiv_start + batch_mode_checkbox + label + field + outerdiv_end