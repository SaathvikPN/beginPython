'''Operator Overloading via special methods'''

'''
Notes:
*Most python operators have an associated "magic" method
(for example, a[x] is the usual way of invoking a.__getitem__(x)).

*Data model guide : https://docs.python.org/3/reference/datamodel.html#special-method-names
'''

class Vector:
    '''Represent vector in Multi-dimensional space'''

    def __init__(self,d):
        ''' create d-dimensional vector intialised to 0'''
        self._coords = [0]*d     #[0,0,0..... d times]

    def __len__(self):
        ''' Return dimension of vector'''
        return len(self._coords)
    def __getitem__(self,i):
        ''' Return ith coordinate'''
        return self._coords[i]
    def __setitem__(self,i,value):
        self._coords[i] = value
    def __add__(self,other):
        ''' Returns sum of 2 vectors(vector objects)'''

        if len(self)!=len(other):    #relies on __len__ method
            raise ValueError('Dimensions must agree')

        result = Vector(len(self))    #start with vector of zeros

        for i in range(len(self)):
            result[i] = self[i] + other[i]
            
        return result

    def __eq__(self,other):
        ''' Return True if vectors have same coordinates'''
        return self._coords == other._coords

    def __ne__(self,other):
        ''' Return True if vectors have different coordinates'''
        return not self == other    #relies on existing __eq__ definition

    def __str__(self):
        ''' Produce string representation of vector'''
        return '<' + str(self._coords)[1:-1] + '>'    #adapt list representation
        
