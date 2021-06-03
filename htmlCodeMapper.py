def init():
    return "<html><form>"

def finalise():
    return "</form></html>"

def createInput(submodule):
    label = "<br><h3>{} {} </h3>".format(submodule["Id"], submodule["Description"])
    field = ""
    if(submodule["Value Required"]):
        field = "<input/>"

    return label + field