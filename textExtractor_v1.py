
import docxpy
import re

#model class
from dataClass_v1 import instructionDetails

#configurtions
import configurations


file = 'data_manual_clean.docx'
file = 'original_data.docx'

# extract text
text = docxpy.process(file)

text = text.split("\n")

instructions_number_regex = re.compile('^\d\d?[.]+(\d?\d?.?)?')
instructions_description_regex = re.compile('^\d\d?[.]+\d?\d?.?([ ]*[A-Z|a-z]*|[ ]*)+')

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




print("[INFO]: STEP 5 STARTING")
for each in data_storage:
    if(not each.value_required): #working on only the ones which do not have any value required
        for word in each.description.split(" "):
            if(word.lower() in configurations.keyword_map.keys()):
                each.value_required = True
                each.value_unit.append(each.unitsMap(word.lower(),configurations.keyword_map))


print("[INFO]: STEP 5 KEYWORD BASED UNIT EXTRACTION COMPLETED")


#Analysis
#lets try to print related data now
for i in data_storage:
    i.printData()

count_value_found = 0
for each in data_storage:
    if(each.value_required):
        count_value_found+=1
print("Total instructions extracted: ",len(data_storage))
print("Total instructions needing values: ",count_value_found)
print('x-x-x-x-x \n')


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