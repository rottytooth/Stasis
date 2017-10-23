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


def reset_store():
    Variable._store = {}


class Variable(object):

    # !!!use as static only!!!
    _store = {} # this is our variable store for all values

    def _update_all():
        numerator = 0
        denom = 0

        if (len(Variable._store) > 0):
            for key, var in Variable._store.items():
                if isinstance(var, list): # each list is a list of floats
                    numerator += sum(var)
                    denom += len(var)
                else:
                    numerator += var
                    denom  += 1

            offset = numerator / denom
            for key, var in Variable._store.items():
                if isinstance(var, list):
                    Variable._store[key] = [x - offset for x in var]
                else:
                    Variable._store[key] -= offset    

    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        Variable._store[name] = conv_to_float(value)
        Variable._update_all()

    @property
    def value(self): # getter
        return conv_from_float(Variable._store[self.name], self.type)

    @value.setter
    def value(self, value):
        self.type = type(value)
        Variable._store[self.name] = conv_to_float(value)
        Variable._update_all()

    @value.deleter
    def value(self):
        del Variable._store[self.name]
        Variable._update_all()

    def __lt__(self, other):
        return self.value < other

    def ___le__(self, other):
        return self.value <= other

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __gt__(self, other):
        return self.value > other

    def __ge__(self, other):
        return self.value >= other

    def __str__(self):
        return str(self.value)

    
class String(Variable):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    @property
    def length(self):
        return len(self.value)

    @property
    def value(self): # return as array of floats
        return Variable._store[self.name]

    @property
    def string(self): # this is for actual display
        retstring = ''
        for a in Variable._store[self.name]:
            a = int(round(a))
            if 0 < a < 0x110000:
                retstring += chr(a)
        return retstring

    @value.setter
    def value(self, value):
        Variable._store[self.name] = []
        if type(value) == str or isinstance(value, list):
            for x in [conv_to_float(x) for x in value]: # for strings, we have to update_all after each char is added
                Variable._store[self.name].append(x)
                Variable._update_all()
        else: # float
            self._value = [value]

    def __str__(self):
        return ''.join([conv_from_float(i, str) for i in self._value])

    def append(self, float):
        self._value.append(float)
