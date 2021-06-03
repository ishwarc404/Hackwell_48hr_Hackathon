from enum import Flag
from posixpath import join
import configurations
import itertools

class instructionDetailParsing :
    def __init__(self, instruction_number, description, value_required, value_unit):
        self.id = instruction_number
        self.description = description
        self.value_required = value_required #True/False
        self.value_unit = value_unit #List of the unti
        self.multivalued = None
        #requires value - true , false
        #type of instruction - boolen, value
        #type of value - single, multiple, range

    
    def refactorData(self):
        # print("Id: {} Description: {}".format(self.id,self.description))

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
                
                unit_allowed = False
                if (joint_unit not in configurations.units):
                    unit_allowed = False
                else:
                    unit_allowed = True
                    self.multivalued  = False #just a single unit found for it

                
                #converting joint_unit into a list
                joint_unit = [joint_unit]


            #if the first check fails
            if(unit_allowed == False):
            #we can do a few more operations, maybe some combination don't fit well together
            #we can get all permutation and combinations of those units toghether
                unit_permutations = list(itertools.permutations(self.value_unit))
                unit_permutations.extend(self.value_unit) #we need to include the originals into the permutation set
                possible_allowed = []
                for each_permutation in unit_permutations:
                    #each permutation is a tuple, we need to join them
                    temporary = ''
                    for k in each_permutation:
                        temporary+= k
                    if (temporary in configurations.units):
                        possible_allowed.append(each_permutation)

                #we can just suggest the user all these possible units
                #let the user pick
                if(len(possible_allowed)>0):
                    unit_allowed = True
                    #joint unit is nothing but a list now
                    joint_unit = possible_allowed
                    self.multivalued = True #multiple units were found which do not work together. 

                else:
                    unit_allowed = False
                    self.value_required = False


            #we accept it only if it is allowed, else we keep 
            if(unit_allowed):
                self.value_unit = joint_unit
                self.value_required = True
                
                new_after_map = []
                for each_allowed in self.value_unit:
                    new_after_map.append(self.unitsMap(each_allowed,configurations.units_map)) #need to map - PCV is measured in %

                self.value_unit = new_after_map
                
                # if(self.value_unit != ''):
                #     print("Value required and it's unit is: {}".format(self.value_unit))

        # print("\n")


    def printData(self):
        # print(" Id: {} \n Description: {} \n Units: {} \n x-x-x-x-x \n \n ".format(self.id,self.description,self.value_unit))
        print("Id: {} \n ".format(self.id))


    #generalised this, as the main function uses this for keyword map
    def unitsMap(self,value_unit,map_dictionary):
        if(value_unit in map_dictionary.keys()):
            return map_dictionary[value_unit]
        else:
            return value_unit


