def init():
    return "<html><form>"

def finalise():
    return "</form></html>"

def createInput(submodule, path):
    value_reference_path = ""
    for each in path:
        value_reference_path += str(each) + "$"


    label = "<br><h3 id={} >{} {} </h3>".format(value_reference_path,submodule["Id"], submodule["Description"])
    field = ""
    if(submodule["Value Required"]):
        field = "<input/>"

    return label + field