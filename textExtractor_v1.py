
import docxpy
import re

#model class
from dataClass_v1 import instructionDetails

#configurtions
import configurations


file = 'data_manual_clean.docx'
# file = 'original_data.docx'

# extract text
text = docxpy.process(file)

text = text.split("\n")

instructions_number_regex = re.compile('^\d\d?[.]+\d?.?')
instructions_description_regex = re.compile('^\d\d?[.]+\d?.?([ ]*[A-Z|a-z]*|[ ]*)+')


procedure_indices = []
for currentIndex in range(0,len(text)):

    if instructions_description_regex.search(text[currentIndex].strip()):
        
        instruction_number  =  instructions_number_regex.match(text[currentIndex].strip()).group()
        instruction_description = text[currentIndex].strip()

        #checking for value now
        value_required = False 
        value_unit = None
        try:
            value_unit = configurations.units_regex.findall(instruction_description)
            value_required = True
            # print("Value unit is: ",value_unit)
        except:
            pass
 
        data = instructionDetails(instruction_number,instruction_description, value_required, value_unit)
        data.printData()
        procedure_indices.append(currentIndex)
    
print("xxx-xxx-xxx-xxx-xxx-xxx-xxx-xxx")

#lets try to print related data now

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