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

    header = "<div  style='margin-bottom:10px; margin-top: 10px;margin-left: 900px;' class='d-flex justify-content-center'><h1>Results</h1> <button style='margin-left:700px;'  class='btn btn-light' onclick='refresh()'>Refresh</button></div>"
    outerWrapper = "<div  class='d-flex inline'><div>"
    with open('result.json') as f:
        data = json.load(f)
    

    html_data = htmlCodeMapper.init()
    for each in data.keys():
        path = [each]
        # label = "<br><h5 id={}' style='margin-right:10px ;'>{} {} </h5>".format(path,data[each]["Id"], data[each]["Description"])        
        html_data += htmlCodeMapper.divWrapperBegin()  + recursiveParse(data[each],path) +  htmlCodeMapper.divWrapperEnd()


    outerWrapperEnd = " </div><div><iframe  src='./jsonViewer.html' width='1000' height='6000' frameborder='0'></div></div> </div>"

    with open('webpage.html', 'w+') as fp:
        fp.write(header + outerWrapper + html_data + outerWrapperEnd)




generateHTML()