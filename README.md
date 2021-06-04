# HONEYWELL HACKATHON 2021 - 48 HOURS
## TITLE: DIGITIZE PAPER BASED BATCH MANUFACTURING RECORDS TO ELECTRONIC FORMAT AUTOMATICALLY


### THOUGHTS AND STEPS


#### v1
 - Let's just delete pages we do not need in the docx file, and work with only those which we need
 - Step 1: Dataset in use => data_manual_clean.doc  Observation : Regex gave good results while extracting the procedures
 - Step 2: Moved onto testing with the original data set Observation : good result while using the numerical way
 - Step 3: Create a class and assemble related data field of the procedures together
 - Step 4: Add a unit mapper in case the representation is different (pcv -> %)
 - Step 5: Provide user with multiple options to select unit where the algorithm is not so sure
 - Step 6: Add a keyword map, and try to figure out the units requirement of the ones which which could not be identifies
 - Step 7: Clean up the index numbering and identify sublevels
 - Step 8: Convert to JSON
 - Step 9: Convert JSON to HTML with reference IDs which will help us map any changes immediately
 - Step 10: Add JSON viewer to HTML
 - Step 11: Added flask application and logic to handle delete/add/edit of instruction values
 - Step 12: Added flask application and logic to handle delete/add/edit of instruction  types
 - Step 13: Minor bug fixes and batch updates
 - Step Uknown: We need to now include some form of NLP so that we can distinguished some of the instructions



### Bugs
- Task Change of 16.3.1 does not work because it's id is 16.0.0 as there are taks missing
