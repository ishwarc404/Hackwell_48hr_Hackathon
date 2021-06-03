import json
import requests

def convertToJSON(parentPools):
    numberOfLevels = len(parentPools)
    numberOfGodParents = len(parentPools[0])
    print("Number of levels: " , numberOfLevels)
    print("Number of GodParents: " ,numberOfGodParents)

    #we need to build up the levels
    level = 2 #we start with the last but one level (4 levels indexed as [0,1,2,3])
    while(level > -1):
        # print(parentPools[level].keys())
        keys =  parentPools[level].keys()
        for each_key in keys:

            all_children = parentPools[level][each_key]["SubModules"]
            parentPools[level][each_key]["SubModules"] = [] #at index 2 
            for each_child in all_children:
                parentPools[level][each_key]["SubModules"].append(parentPools[level+1][each_child])
            if(parentPools[level][each_key]["SubModules"] == []):
                parentPools[level][each_key]["SubModules"] = None

        # print(parentPools[level])
        level-=1

    # we need to post this JSON onto the API server as well
    url = 'https://api.jsonbin.io/v3/b/60b8f01d2d9ed65a6a7ede39'
    headers = {
    'Content-Type': 'application/json',
    'X-Master-Key': '$2b$10$sBckZTunpNsmdwc0xPC5z.52q0gtCaWifXquNDipFBGY3d9ZF/pgS'
    }
    data = parentPools[0]

    requests.put(url, json=data, headers=headers)


    with open('result.json', 'w') as fp:
        json.dump(parentPools[0], fp)

