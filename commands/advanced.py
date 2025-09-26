

def print_stm(fun, variables):
    ret_print = []
    max_value_in_print = fun[1].split()[1:]  # minus 'print'
    for item in max_value_in_print:
        if item.startswith("{") and item.endswith("}"):
            var_name = item[1:-1]
            for var in variables:
                if var['key'] == var_name and fun[0] > var['value'][0]:
                    ret_print.append(var["value"][1])

                
            #if var_name in variables and fun[0] > variables[var_name][0]:
                #ret_print.append((variables[var_name][1]))
               
        elif item.startswith('"') and not item.endswith('"'):
            ret_print.append((item[1:]))
        elif not item.startswith('"') and item.endswith('"'):
            ret_print.append((item[:-1]))
        elif not item.startswith('"') and not item.endswith('"'):
            ret_print.append((item[:]))
            
        elif item.startswith('"') and item.endswith('"'):
            ret_print.append((item[1:-1]))

    result = ' '.join(ret_print)
    return result


            
    


commands_advanced = {
    'print': print_stm,
}