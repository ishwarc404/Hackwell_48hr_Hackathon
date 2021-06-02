
import docxpy
import re


file = 'data_manual_clean.docx'
file = 'original_data.docx'

# extract text
text = docxpy.process(file)

text = text.split("\n")

regexp = re.compile('^\d\d?[.]+\d?.?([ ]*[A-Z|a-z]*|[ ]*)+')

for each in text:
    checked = each.strip()
    if regexp.search(each.strip()):
        print('Matched: {}'.format(each.strip()))