from posixpath import join
import configurations

class instructionDetails :
    def __init__(self, id, description, value_required, value_unit):
        self.id = id
        self.description = description
        self.value_required = value_required #True/False
        self.value_unit = value_unit #List of the unti
        #requires value - true , false
        #type of instruction - boolen, value
        #type of value - single, multiple, range


    def printData(self):
        print("Id: {} Description: {}".format(self.id,self.description))
        if(self.value_required):
            #we need to remove any duplicates from the units list
            self.value_unit = sorted(set(self.value_unit), key = self.value_unit.index)

            #little bit of cleaning is required
            #example - / alone is useless
            if(len(self.value_unit)==1 and self.value_unit[0]=='/'):
                self.value_unit = None
                self.value_required = False


            if(self.value_required):
                #we now need to join it
                joint_unit = ''
                for k in self.value_unit:
                    joint_unit+= k
                
                #we accept it only if it is allowed, else we keep 
                if(joint_unit in configurations.units):
                    self.value_unit = joint_unit
                    if(self.value_unit != ''):
                        print("Value required and it's unit is: {}".format(self.value_unit))

        print("\n")




