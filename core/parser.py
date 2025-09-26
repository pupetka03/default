def parser_main(code):

    fun = []
    variables = {}
    
    size = len(code)

    #fun
    for i in range(size):
        if "=" in code[i]:
            key, value = code[i].split('=', 1)
            key = key.strip()
            value = value.strip()
            variables[key] = (i, value) 

        if "{" in code[i] or "}" in code[i] or '"' in code[i] or "'" in code[i]:
            fun.append((i, code[i]))

    return fun, variables
