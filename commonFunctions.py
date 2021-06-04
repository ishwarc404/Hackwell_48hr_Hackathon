def getDescriptionById(instructionID, data_storage):
    for each_instruction in data_storage:
        if (each_instruction.id == instructionID):
            return each_instruction.description

def getDetailsById(instructionID, data_storage):

    # print(instructionID)

    details = {
        "Id" : None,
        "Description" : None,
        "Value Required" : None,
        "Value Unit" : None,
        "Multivalued" : None,
    }

    for each_instruction in data_storage:
        # print(each_instruction.id)
        if (each_instruction.id == instructionID):
            # print(instructionID, "yes")
            details['Id'] = each_instruction.id
            details['Description'] = each_instruction.description
            details['Value Required'] = each_instruction.value_required
            details['Value Unit'] = each_instruction.value_unit
            details['Multivalues'] = each_instruction.multivalued
            details['Value Type'] = each_instruction.value_type

            return details

    return details



def updateDataStorage(instructionId, final_value, change_requested , data_storage):
    try:
        for each_instruction in data_storage:
            if (each_instruction.id == instructionId):
                if(change_requested == "ADD_UNIT"):
                    each_instruction.value_unit.append(final_value[0:-2]) #-2 strips off \n 
                if(change_requested == "DELETE_UNIT"):
                    each_instruction.value_unit.remove(final_value[0:-2]) #-2 strips off \n 

                #ADD is nothing but modified
                if(change_requested == "ADD_TYPE"):
                    each_instruction.value_required = True
                    each_instruction.value_type = final_value[0:-2] #-2 strips off \n 
                if(change_requested == "DELETE_TYPE"):
                    each_instruction.value_required = False
                    each_instruction.value_type = None

                if(change_requested == "EDIT_INSTRUCTION"):
                    each_instruction.description = final_value[0:-2] #-2 strips off \n 


        print("[INFO]: DATA STORE UPDATED")   
    except:
        pass 
    return data_storage