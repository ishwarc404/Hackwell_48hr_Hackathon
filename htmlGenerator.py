import json
import htmlCodeMapper





def foo(data):
    if(data["SubModules"] == None):
        return htmlCodeMapper.createInput(data)
    
    html = ""
    for eachModule in data["SubModules"]:
        html += foo(eachModule)
        
    return html


def generateHTML():
    with open('result.json') as f:
        data = json.load(f)
    

    html_data = htmlCodeMapper.init()
    for each in data.keys():
        html_data += foo(data[each])

    with open('webpage.html', 'w+') as fp:
        fp.write(html_data)




generateHTML()