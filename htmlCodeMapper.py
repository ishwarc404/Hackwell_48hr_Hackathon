def init():
    return "<html><link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'><form>"

def finalise():
    return "</form></html>"

def divWrapperBegin():
    return "<div style='border: solid 1px black; margin:10 10 10 10px; padding: 10 10 10 10px; width:50vw;''>"

def divWrapperEnd():
    return "</div>"

def createInput(submodule, path):
    value_reference_path = ""
    for each in path:
        value_reference_path += str(each) + "$"

    outerdiv_start = "<div class='d-flex inline' style='margin-bottom:10px'>"
    label = "<br><h6 id={}' style='margin-right:10px ; margin-top:2px'>{} {} </h6>".format(value_reference_path,submodule["Id"], submodule["Description"])
    field = ""
    if(submodule["Value Required"]):
        value_reference_path+="Value Unit" #adding the index to the reference path
        field = "<select id='{}'>".format(value_reference_path)
        for each_option in range(0,len(submodule["Value Unit"])):
            field += "<option id='{}' value='{}'>{}</option>".format(value_reference_path+'$' + str(each_option),submodule["Value Unit"][each_option],submodule["Value Unit"][each_option])

        field += "</select>"

        #adding the add field button
        field += "<button id='{}' style='margin-left:10px' class='btn btn-primary'>+</button>".format(value_reference_path)
    outerdiv_end = "</div>"
    return outerdiv_start + label + field + outerdiv_end