
import docxpy
import re

#model class
from dataClass_v1 import procedureDetails

file = 'data_manual_clean.docx'
file = 'original_data.docx'

# extract text
text = docxpy.process(file)

text = text.split("\n")

regexp = re.compile('^\d\d?[.]+\d?.?([ ]*[A-Z|a-z]*|[ ]*)+')


procedure_indices = []
for currentIndex in range(0,len(text)):

    if regexp.search(text[currentIndex].strip()):
        print('Matched: {}'.format(text[currentIndex].strip()))
        procedure_indices.append(currentIndex)
    
print("xxxxxxxx-xxxxxx-xxxxxx-xxxxxx-xxxxx-xxxxx-xxxxx-xxxxxxx")

#lets try to print related data now
for i in range(0,len(procedure_indices)-1,2):
    print('Starting: {}'.format(text[procedure_indices[i]].strip()))
    start_index = procedure_indices[i]+1
    end_index = procedure_indices[i+1]-1

    #need to print everything in this range now
    data = text[start_index:end_index+1]
    # print(data)
    for subdata in data:
        
        if(len(subdata.strip())>0):
            print("Related Data is: ",subdata.strip())
    
    print('Starting: {}'.format(text[procedure_indices[i+1]].strip()))
    print("########################")