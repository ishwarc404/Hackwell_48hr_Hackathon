import json
import requests


import changeExecuter
import dataClass_v1
# if(change_requested == "ADD_INSTRUCTION"):
#     print(each_instruction.keys())
#     if(each_instruction["SubModules"]!=None):
#         numberOfExistingInstructions = len(each_instruction["SubModules"])
#         newInstructionId = instructionId + "." + str(numberOfExistingInstructions+1)
#         newData = dataClass_v1.instructionDetailParsing(newInstructionId,final_value)
#         each_instruction["SubModules"].append(newData)
#     else:
#         newInstructionId = instructionId + "." + str(numberOfExistingInstructions+1)
#         newData = dataClass_v1.instructionDetailParsing(newInstructionId,final_value)
#         each_instruction["SubModules"] = [newData]


def convertToJSON(parentPools):

    #Getting any necessary changes, on application restart
    value_changes_requested = changeExecuter.getChanges()


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


                #NEED TO TAKE CARE OF ANY ADD_INSTRUCTION CHANGES HERE
                #change executer
                for each_change in value_changes_requested:
                    # print(each_child)
                    # print(each_change[0])
                    # print("----- \n")
                    if(each_child  == each_change[0]):
                        numberOfExistingInstructions = 0
                        try:
                            numberOfExistingInstructions = len(parentPools[level+1][each_child]["SubModules"])
                        except:
                            parentPools[level+1][each_child]["SubModules"] = []
                        
                        tempvalue = each_change[2:] #this is still a list
                        new_value = ''
                        for each in tempvalue:
                            new_value += each + " "


                        newInstructionId = each_child + "." + str(numberOfExistingInstructions+1) + "."
                        newData = dataClass_v1.instructionDetailParsing(newInstructionId,new_value)
                        newData = newData.__dict__

                        #adding some extra field
                        newData["Id"] = newData.pop("id")
                        newData["Description"] = newData.pop("description")
                        newData["Value Type"] = newData.pop("value_type")
                        newData["Value Unit"] = newData.pop("value_unit")
                        newData["Value Required"] = newData.pop("value_required")
                        newData["Multivalued"] = newData.pop("multivalued")
                        newData["SubModules"] = []
                        # print(newData)
                        parentPools[level+1][each_child]["SubModules"].append(newData)

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

