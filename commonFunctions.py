def getDescriptionById(instructionID, data_storage):
    for each_instruction in data_storage:
        if (each_instruction.id == instructionID):
            return each_instruction.description

