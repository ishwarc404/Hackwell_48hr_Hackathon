import json
from sys import path
import htmlCodeMapper


def recursiveParse(data, path):

    if(data["SubModules"] == None):
        return htmlCodeMapper.createInput(data,path)
    
    original_path = path
    html = ""
    
    #to include parents as well,or else if they have children they will not have an html
    label = "<h5 id={}' style='margin-right:10px ;'>{} {} </h5>".format(path,data["Id"], data["Description"])        
    html += label
    path.append("SubModules")
    for eachModuleIndex in range(0,len(data["SubModules"])):
        path.append(eachModuleIndex)
        html += recursiveParse(data["SubModules"][eachModuleIndex],path)
        path.remove(eachModuleIndex)

    outerdiv_start = "<div class='d-flex inline' style='margin-bottom:10px'>"

    addInstructionPath = ""
    for each in path:
        addInstructionPath += str(each) + "$"
    html+= "<button id='{}' style='margin-left:10px' class='btn btn-outline-secondary' onclick=addNewInstruction(this.id)>Add new instruction</button><br><br>".format(addInstructionPath)

    return html


def generateHTML():

    header = "<div  style='margin-bottom:10px; margin-top: 10px;margin-left: 900px;' class='d-flex justify-content-center'><h1>Results</h1> <button style='margin-left:700px;'  class='btn btn-light' onclick='refresh()'>Refresh</button></div>"
    outerWrapper = "<div  class='d-flex inline'><div>"
    with open('result.json') as f:
        data = json.load(f)
    

    batch_mode_checkbox_button1 = "<button id='{}' style='margin-left:10px' class='btn btn-outline-secondary' onclick=batchUpdateValueTypeBackend('value')>Batch Update Value</button>"
    batch_mode_checkbox_button2 = "<button id='{}' style='margin-left:10px' class='btn btn-outline-secondary' onclick=batchUpdateValueTypeBackend('unitadd')>Batch add unit</button>"
    batch_mode_checkbox_button3 = "<button id='{}' style='margin-left:10px' class='btn btn-outline-secondary' onclick=batchUpdateValueTypeBackend('unitdelete')>Batch delete unit</button>"

    html_data = htmlCodeMapper.init()
    for each in data.keys():
        path = [each]
        

        addInstructionPath = ""
        addInstructionPath += str(each) + "$"


        html_data += htmlCodeMapper.divWrapperBegin()  + recursiveParse(data[each],path) + batch_mode_checkbox_button1 + batch_mode_checkbox_button2 + batch_mode_checkbox_button3 +  "<button id='{}' style='margin-left:10px' class='btn btn-outline-secondary' onclick=addNewInstruction(this.id)>Add new instruction</button>".format(addInstructionPath)
        html_data+= htmlCodeMapper.divWrapperEnd()

    outerWrapperEnd = " </div><div><iframe  src='./jsonViewer.html' width='1000' height='11700' frameborder='0'></div></div> </div>"

    with open('webpage.html', 'w+') as fp:
        fp.write(header + outerWrapper + html_data + outerWrapperEnd)




generateHTML()