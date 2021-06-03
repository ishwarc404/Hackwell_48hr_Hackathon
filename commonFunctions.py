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

            return details

    return details

