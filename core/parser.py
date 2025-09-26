from core.variables import global_variables

def parser_main(code):

    fun = [] #exemple [1, 'print' "Sohodni ok"'), ]
    variables_parser = {} #exemple {'q': (0, 'Ihor')}
    
    size = len(code)

    #fun
    for i in range(size):
        if "=" in code[i]:
            key, value = code[i].split('=', 1)
            key = key.strip()
            value = value.strip()
            variables_parser[key] = (i, value) 
            global_variables.set_variables(key=key, value = (i, value))

        if "{" in code[i] or "}" in code[i] or '"' in code[i] or "'" in code[i]:
            fun.append((i, code[i]))


    return fun, global_variables.get_variables()
