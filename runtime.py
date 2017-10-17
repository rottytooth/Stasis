# Stasis runtime module

import math

class InterpreterError(Exception):
    pass

def conv_to_float(item):
    def from_int(a):
        return float(a)
    def from_char(a): # test for len of 1
        if (len(a) > 1):
            raise InterpreterError("Cannot convert string of length > 1 to char")
        return float(ord(a))
    def no_conv(a):
        return a

    options_in = {
        str : from_char,
        int : from_int,
        float: no_conv
    }
    return options_in[type(item)](item) 

def conv_from_float(item_value, item_type):
    def to_int(a):
        return int(round(a))
    def to_char(a):
        int_a = to_int(a)
        if 0 < int_a < 0x110000:
            return chr(int_a)
        else:
            return '' # out of range -- return empty string
    def no_conv(a):
        return a

    options_out = {
        str : to_char,
        int : to_int,
        float: no_conv
    }
    return options_out[item_type](item_value) 

def get_var(name):
    return VariableStore.get(name)


def set_var(name, value, typ = None):
    VariableStore.set(name, value, typ)


class VariableStore(object):
    __vars = {} #: :type: dict of (str, Variable)

    @staticmethod
    def reset():
        _vars = {}

    @staticmethod
    def set(name, value, typ):
        if (typ == None): 
            typ = type(value)
        if typ == str and isinstance(value, list): # might be an array of floats or a string
            new_var = String(len(value))
            new_var.value = value
        else:
            new_var = Variable(typ)
            new_var.value = value

        VariableStore.__vars[name] = new_var
        VariableStore._update_all()

    @staticmethod
    def get(name):
        if type(VariableStore.__vars[name]) is String:
            retset = []
            retset[:] = [conv_from_float(x, str) for x in VariableStore.__vars[name]._value]
            return ''.join(retset)
        else:
            return VariableStore.__vars[name].value

    def _total_length():
        length = 0.0

        for key, value in VariableStore.__vars.items():
            if type(value) is String:
                length += value.length
            else:
                length += 1.0
        return length

# delete_var?

    @staticmethod
    def _update_all():
        numerator = 0

        if (len(VariableStore.__vars) > 0):
            for key, var in VariableStore.__vars.items():
                if type(var) == String:
                    for char in var.value:
                        numerator += float(ord(char))
                else:
                    numerator += var._value

            offset = numerator / VariableStore._total_length()
            for key, var in VariableStore.__vars.items():
                if type(var) == String:
                    var._value[:] = [x - offset for x in var._value]
                else:
                    VariableStore.__vars[key]._value -= offset    


class Variable(object):

    def __init__(self, type, value = 0.0):
        self.type = type
        self._value = value
        
    @property
    def value(self): # getter
        return conv_from_float(self._value, self.type)

    @value.setter
    def value(self, value):
        self._value = conv_to_float(value)

    @value.deleter
    def value(self):
        print("deleter of value called")
#VariableStore.Delete(xxx...)
        del self._value
    

class String(Variable):

    def __init__(self, length):
        Variable.__init__(self, str, [0] * length) # should be an array of float

    @property
    def length(self):
        return len(self.value)

    @property
    def value(self): # getter
        return ''.join([conv_from_float(i, str) for i in self._value])

    @value.setter
    def value(self, value):
        if type(value) == str:
            self._value[:] = [conv_to_float(x) for x in value]    
        else: # float
            self._value = value
