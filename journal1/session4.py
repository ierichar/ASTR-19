'''
    Session 4
    ASTR-19-01 Spring 2022
    March 31st, 2022
    Ian Richardson

    This program  declares a class describing my favorite animal. 
    It has the data members of the class represent the following 
    physical parameters of the animal: 
        length of the arms (float), 
        length of the legs (float), 
        number of eyes (int), 
        does it have a tail? (bool), 
        is it furry? (bool)
    An initialization function sets the values of the data members when
    an instance of the class is created. A member function of the class
    prints out and describes the data members representing the physical
    characteristics of the animal.
'''

# California Sea Otter
class Animal:
    '''
        Sets the values of the data members when
        an instance of the class is created.
    '''
    def __init__(self):
        self._arm_length = 0.150 #m
        self._leg_length = 150 #cm
        self._eye_count = 2
        self._has_tail = True
        self._is_furry = True
    
    '''
        Prints out and describes the data members representing
        the physical characteristics of the animal.
    '''
    def print(self):
        # Determine if animal has a tail or not for print statement
        if self._has_tail: tail_statement = 'a tail'
        else: tail_statement = 'no tail'
        # Determine if animal has fur or not for print statement
        if self._is_furry: fur_statement = 'have fur'
        else: fur_statement = 'have no fur'

        print('The California Sea Otter has an arm length of', self._arm_length,
            'cm and a leg length of', self._leg_length, 
            'cm. They have', self._eye_count, 'eye(s),', tail_statement +
            ', and', fur_statement + '.')

def main():
    Otter = Animal()
    Otter.print()

if __name__=="__main__":
    main()