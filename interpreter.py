import itertools
import runtime

def reverse_enum(L):
   for index in reversed(range(len(L))):
      yield index, L[index]

class VariableHolder(object):
    def __init__(self, type, size):
        self.type = type
        self.size = size

# find the inputs that will lead to the given array of floats
def build_input_array_floats(output):
    input = [0.0] * len(output)
    count = len(output) - 1
    for idx, x in reverse_enum(output):
        n = idx + 2.0  # because n is 1-based and we're not using the last one
        input[idx] += (n * x) / (n - 1.0)
        addt = 1
        for y in input[idx + 1:len(input)]:
            input[idx] += (n * y) / ((n - 1.0) * (n + addt))
            addt += 1

    return [0] + input # add leading 0

# find the inputs that will lead to an array of inputs of different types
def build_input(output_list):
    var_list = []
    raw_values = []
    input_list = []

    for obj in output_list:
        length = 1
        if (type(obj) == str):
            length = len(obj)
        var = VariableHolder(type(obj), length)
        var_list.append(var)

        if (type(obj) == str):
            raw_values.extend([float(ord(i)) for i in list(obj)])
        else:
            raw_values.append(float(obj))

    processed_values = build_input_array_floats(raw_values)
    input_list.append(processed_values.pop(0)) # pop the leading zero

    arr_idx = 0 
    for idx in range(len(var_list)):
        if (var_list[idx].type == str):
            float_vals = processed_values[idx : var_list[idx].size + idx]
            input_list.append(float_vals)
            arr_idx += var_list[idx].size
        else:
            input_list.append(runtime.conv_from_float(processed_values[arr_idx], var_list[idx].type))
            arr_idx += 1

    return input_list

