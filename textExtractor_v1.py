
import docxpy
import re

#model class
from dataClass_v1 import instructionDetails
from commonModel import instructionLevels

#configurtions
import configurations


#common functions
import commonFunctions


file = 'data_manual_clean.docx'
file = 'original_data.docx'

# extract text
text = docxpy.process(file)

text = text.split("\n")

instructions_number_regex = re.compile('^([1-9]+[1-9]*[.])+')
instructions_description_regex = re.compile('^([1-9]+[1-9]*[.])+([ ]*[A-Z|a-z]*|[ ]*)+')

# text = ['8.39.1. Solution preparation No.']
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


        data = instructionDetails(instruction_number,instruction_description, value_required, value_unit)
        
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

parentPoolsRequired = max_level - 1

parentPools = [ {} for i in range(parentPoolsRequired) ] 


def findDotIndex(id):
    return [i for i, ltr in enumerate(id) if ltr == '.']

#first we need to seperate out the parent instruction indices
parentIndices = []
while(iterationIndex < maxIndex):
    current_instruction_id = instruction_ids[iterationIndex]
    numberOfLevels = current_instruction_id.count(".")
    levelNumbers  = current_instruction_id.split(".")
    levelNumbers.remove('')
    #these level numbers are in string format, need to convert into number
    # levelNumbers = [int(i) for i in levelNumbers]
    indexOfDots = findDotIndex(current_instruction_id)

    #if parent
    if(numberOfLevels == 1):
        if(levelNumbers[0] not in parentPools[0].keys()):
            parentPools[0][levelNumbers[0]] = []

    # #means it is a sublevel
    if(numberOfLevels > 1):
        # for eachlevel in numberOfLevels:
        parentPoolNumber = numberOfLevels - 2
        indexOfSplitDot = indexOfDots[numberOfLevels - 2]
        parentPoolKey = current_instruction_id[0:indexOfSplitDot]  #split it uptil the  dot # (numberOfLevels - 1)
        try:
            parentPools[parentPoolNumber][parentPoolKey].append([current_instruction_id, commonFunctions.getDescriptionById(current_instruction_id, data_storage)])
        except:
            parentPools[parentPoolNumber][parentPoolKey] = []

        


    iterationIndex +=1


# print(parentPools[0])
# print("\n")
# print("\n")
# print(parentPools[1])
# print("\n")
# print("\n")
# print(parentPools[2])


       
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