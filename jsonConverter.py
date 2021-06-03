import json

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
            current_description = parentPools[level][each_key]["Description"]
            all_children = parentPools[level][each_key]["SubModules"]
            parentPools[level][each_key]["SubModules"] = [] #at index 2 
            for each_child in all_children:
                parentPools[level][each_key]["SubModules"].append(parentPools[level+1][each_child])
            if(parentPools[level][each_key]["SubModules"] == []):
                parentPools[level][each_key]["SubModules"] = None

        # print(parentPools[level])
        level-=1

    with open('result.json', 'w+') as fp:
        json.dump(parentPools[0], fp)