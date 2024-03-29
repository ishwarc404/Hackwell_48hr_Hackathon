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


    return html


def generateHTML():

    header = "<div  style='margin-bottom:10px; margin-top: 10px;margin-left: 700px;' class='d-flex justify-content-center'><h1>Results</h1> <button style='margin-left:400px;'  class='btn btn-light' onclick='refresh()'>Commit Changes and Refresh</button><a href='/exportJSON' style='margin-left:50px;margin-top:10px;' target='_blank'><button  class='btn btn-light' onclick='export()'>EXPORT JSON</button></a></div>"
    outerWrapper = "<div  class='d-flex inline'><div>"
    with open('result.json') as f:
        data = json.load(f)
    

    batch_mode_checkbox_button1 = "<button id='{}' style='margin-left:10px' class='btn btn-outline-secondary' onclick=batchUpdateValueTypeBackend('value')>Batch Update Value</button>"
    batch_mode_checkbox_button2 = "<button id='{}' style='margin-left:10px' class='btn btn-outline-secondary' onclick=batchUpdateValueTypeBackend('unitadd')>Batch add unit</button>"
    batch_mode_checkbox_button3 = "<button id='{}' style='margin-left:10px' class='btn btn-outline-secondary' onclick=batchUpdateValueTypeBackend('unitdelete')>Batch delete unit</button>"

    html_data = htmlCodeMapper.init()
    for each in data.keys():
        path = [each]
        html_data += htmlCodeMapper.divWrapperBegin()  + recursiveParse(data[each],path) + batch_mode_checkbox_button1 + batch_mode_checkbox_button2 + batch_mode_checkbox_button3 + htmlCodeMapper.divWrapperEnd()




    outerWrapperEnd = " </div><div><iframe  src='./jsonViewer' width='1000' height='6000' frameborder='0'></div></div> </div>"

    with open('./templates/webpage.html', 'w+') as fp:
        fp.write(header + outerWrapper + html_data + outerWrapperEnd)




generateHTML()