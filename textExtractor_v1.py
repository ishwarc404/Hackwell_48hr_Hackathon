
import docxpy
import re
import json

#model class
from dataClass_v1 import instructionDetailParsing

#configurtions
import configurations

#functions
import jsonConverter
import commonFunctions
import changeExecuter


file = 'data_manual_clean.docx'
file = 'original_data.docx'

# extract text
text = docxpy.process(file)

text = text.split("\n")

instructions_number_regex = re.compile('^([1-9]+[1-9]*[.])+')
instructions_description_regex = re.compile('^([1-9]+[1-9]*[.])+([ ]*[A-Z|a-z]*|[ ]*)+')

# text = ['8.22.11. Exhaust bypass line ']
data_storage = []
print("[INFO]: STEP 1-5 STARTING")


procedure_indices = []
for currentIndex in range(0,len(text)):

    if instructions_description_regex.search(text[currentIndex].strip()):
        
        instruction_number  =  instructions_number_regex.match(text[currentIndex].strip()).group()
        instruction_description = text[currentIndex].strip()

        #checking for value now
        value_required = False  #this is set in the dataClassFile
        value_unit = None

        #this checks and finds all occurances of any mention of a unit in the description
        try:
            value_unit = configurations.units_regex.findall(instruction_description)
            value_required = True
        except:
            pass
 
        #we need to strip off the instruction_number from the instruction_description before storing
        instruction_description = instruction_description[len(instruction_number):].lstrip()


        data = instructionDetailParsing(instruction_number,instruction_description, value_required, value_unit)
        
        #refactorData basically cleans it a little more
        data.refactorData()
        data_storage.append(data)
        procedure_indices.append(currentIndex)
    
print("[INFO]: STEP 1-5 REGEX MAPPING AND EXTRACTION COMPLETED")

#Analysis
count_value_found = 0
for each in data_storage:
    if(each.value_required):
        count_value_found+=1
print("Total instructions extracted: ",len(data_storage))
print("Total instructions needing values: ",count_value_found)
print('x-x-x-x-x \n')




print("[INFO]: STEP 6 STARTING")
for each in data_storage:
    if(not each.value_required): #working on only the ones which do not have any value required
        for word in each.description.split(" "):
            if(word.lower() in configurations.keyword_map.keys()):
                each.value_required = True
                each.value_unit.append(each.unitsMap(word.lower(),configurations.keyword_map))
    
    for eachType in each.value_unit:
        if eachType not in configurations.units:
            each.value_type = "string"


print("[INFO]: STEP 6 KEYWORD BASED UNIT EXTRACTION COMPLETED")


#Analysis
#lets try to print related data now
instruction_ids = []
for i in data_storage:
    instruction_ids.append(i.id)

count_value_found = 0
for each in data_storage:
    if(each.value_required):
        count_value_found+=1
print("Total instructions extracted: ",len(data_storage))
print("Total instructions needing values: ",count_value_found)
print('x-x-x-x-x \n')



# for each in data_storage:
#     each.printData()


print("[INFO]: STEP 7 SUBLEVEL EXTRACTION")
#we need to parse instruction_ids and get the data
#Ananlsyis stage

#using a while looop here because we need manual control of the iterative index
iterationIndex  = 0
maxIndex = len(instruction_ids)


#we need to create a tree with the different parents and levels
# we need to know the maximum levels possible
# max_parent_levels_possible = (max_levels - 1 )
#we need to iterate once through the instruction_ids for that
max_level  = 0 
for each in instruction_ids:
    numberOfLevels = each.count(".")
    if(numberOfLevels > max_level):
        max_level = numberOfLevels

parentPoolsRequired = max_level

parentPools = [ {} for i in range(parentPoolsRequired) ] 


def findDotIndex(id):
    return [i for i, ltr in enumerate(id) if ltr == '.']



#TO PREVENT DUPLICATION OF DATA
VISITED_IDS = []

#Getting any necessary changes, on application restart
value_changes_requested = changeExecuter.getChanges()

#first we need to seperate out the parent instruction indices
parentIndices = []
while(iterationIndex < maxIndex):

    if(instruction_ids[iterationIndex] not in VISITED_IDS):
        
        current_instruction_id = instruction_ids[iterationIndex]
        numberOfLevels = current_instruction_id.count(".")
        levelNumbers  = current_instruction_id.split(".")
        levelNumbers.remove('')
        #these level numbers are in string format, need to convert into number
        indexOfDots = findDotIndex(current_instruction_id)



        #change executer
        for each_change in value_changes_requested:
            if(current_instruction_id[0:-1]  == each_change[0]):
                change_requested = each_change[1] #can be ADD DELETE
                tempvalue = each_change[2:] #this is still a list
                new_value = ''
                for each in tempvalue:
                    new_value += each + " "
                data_storage = commonFunctions.updateDataStorage(current_instruction_id, new_value, change_requested , data_storage)
        
        #we need to clear the text file now
        file =  open('changes.txt', 'r+')
        file.truncate(0)
        file.close
                
                

        #if parent
        if(numberOfLevels == 1):
            if(levelNumbers[0] not in parentPools[0].keys()):
                parentPools[0][levelNumbers[0]] = {"SubModules":[]}
                parentPools[0][levelNumbers[0]].update(commonFunctions.getDetailsById(current_instruction_id, data_storage))

        # #means it is a sublevel
        if(numberOfLevels > 1):
            # for eachlevel in numberOfLevels:
            
            parentPoolNumber = numberOfLevels - 2
            indexOfSplitDot = indexOfDots[numberOfLevels - 2]
            parentPoolKey = current_instruction_id[0:indexOfSplitDot]  #split it uptil the  dot # (numberOfLevels - 1)
            childPoolNumber = parentPoolNumber + 1

            try:
                parentPools[parentPoolNumber][parentPoolKey]["SubModules"].append(current_instruction_id[0:-1])
            except:
                pass
                # parentPools[parentPoolNumber][parentPoolKey] = {"SubModules":[]}
                # parentPools[parentPoolNumber][parentPoolKey].update(commonFunctions.getDetailsById("Unknown", data_storage))

            parentPools[childPoolNumber][current_instruction_id[0:-1]] = {"SubModules":[]}
            parentPools[childPoolNumber][current_instruction_id[0:-1]].update(commonFunctions.getDetailsById(current_instruction_id, data_storage))

            VISITED_IDS.append(current_instruction_id)  #TO PREVENT DUPLICATION OF DATA






    iterationIndex +=1

# print("LEVEL 0")
# for i in parentPools[0].keys():
#     if(len(parentPools[0][i])>0):
#         print("{}  = {} ".format(i,parentPools[0][i]))

# print("\n \n")
# print("LEVEL 1")
# for i in parentPools[1].keys():
#     if(len(parentPools[1][i])>0):
#         print("{}  = {} ".format(i,parentPools[1][i]))


# print("\n \n")
# print("LEVEL 2")
# for i in parentPools[2].keys():
#     if(len(parentPools[2][i])>0):
#         print("{}  = {} ".format(i,parentPools[2][i]))

# print("\n \n")
# print("LEVEL 3")
# for i in parentPools[3].keys():
#     if(len(parentPools[3][i])>0):
#         print("{}  = {} ".format(i,parentPools[3][i]))






print("[INFO]: STEP 8 CONVERT INTO JSON")

# #WE ARE STORING THE PARENT POOLS INTO A JSON FILE, SO THAT THE USER CAN MODIFY IT WHILE USING FLASK AND CHANGEEXECUTER.PY
# with open('parentPools.json', 'w') as fp:
#     json.dump({"data":parentPools}, fp)
 
jsonConverter.convertToJSON(parentPools)


print("[INFO]: STEP 8 CONVERT INTO JSON COMPLETED")




       
# #Now that we have the parent indices, we need to find how many sub instructions each parent has
# #this logic will leave out the children for the last index,so we will take care of that later after the loop
# #note 1 is being subtracted from the logic , to not include parent in the count
# numberofChildren = []
# for k in range(0, len(parentIndices)-1):
#     numberofChildren.append(parentIndices[k+1]-parentIndices[k])
#     # print("Parent {} has {} children".format(k+1, parentIndices[k+1]-parentIndices[k]-1))
# #last parent is left out
# indexofLastIntruction = len(instruction_ids)
# indexofLastParent = parentIndices[-1]
# numberofChildren.append(indexofLastIntruction - indexofLastParent -1)
# # print("Last children: ", indexofLastIntruction - indexofLastParent-1)
# # print("Number of parent instructions: ")





























# for i in range(0,len(procedure_indices)-1,2):
#     print('Starting: {}'.format(text[procedure_indices[i]].strip()))
#     start_index = procedure_indices[i]+1
#     end_index = procedure_indices[i+1]-1

#     #need to print everything in this range now
#     data = text[start_index:end_index+1]
#     # print(data)
#     for subdata in data:
        
#         if(len(subdata.strip())>0):
#             print("Related Data is: ",subdata.strip())
    
#     print('Starting: {}'.format(text[procedure_indices[i+1]].strip()))
#     print("########################")

