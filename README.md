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
 - Step 6: We need to now include some form of NLP so that we can distinguished some of the instructions



