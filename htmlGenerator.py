import json
from sys import path
import htmlCodeMapper


def recursiveParse(data, path):
    if(data["SubModules"] == None):
        return htmlCodeMapper.createInput(data,path)
    
    original_path = path
    html = ""
    path.append("SubModules")
    for eachModuleIndex in range(0,len(data["SubModules"])):
        path.append(eachModuleIndex)
        html += recursiveParse(data["SubModules"][eachModuleIndex],path)
        path.remove(eachModuleIndex)

        
    return html


def generateHTML():
    with open('result.json') as f:
        data = json.load(f)
    

    html_data = htmlCodeMapper.init()
    for each in data.keys():
        path = [each]
        html_data += htmlCodeMapper.divWrapperBegin()  +  recursiveParse(data[each],path) +  htmlCodeMapper.divWrapperEnd()

    with open('webpage.html', 'w+') as fp:
        fp.write(html_data)




generateHTML()