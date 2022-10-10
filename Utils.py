def_indent = "    "


def print_formatted(param, indent_level: int = 0):
    indent = ""
    for inx in range(indent_level):
        indent += def_indent
    obj_type = type(param)
    if obj_type is list or obj_type is tuple:
        inx = 0
        for element in param:
            line = indent + "[" + str(inx) + "]: "
            ele_type = type(element)
            if ele_type is list or ele_type is tuple or ele_type is dict:
                print(line)
                print_formatted(element, indent_level + 1)
            else:
                line += str(element)
                print(line)
            inx += 1
    elif obj_type is dict:
        for key in param.keys():
            element = param[key]
            ele_type = type(element)
            line = indent + "[" + str(key) + "]: "
            if ele_type is list or ele_type is tuple or ele_type is dict:
                print(line)
                print_formatted(element, indent_level + 1)
            else:
                line += str(element)
                print(line)
