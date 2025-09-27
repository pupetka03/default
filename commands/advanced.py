from core.variables import global_variables

def print_stm(fun):
    ret_print = []
    max_value_in_print = fun[1].split()[1:]  # minus 'print'

    for item in max_value_in_print:
        # якщо рядок у лапках
        if item.startswith('"') and item.endswith('"'):
            ret_print.append(item[1:-1])
        # якщо містить змінну у фігурних дужках
        elif "{" in item and "}" in item:
            start = item.find("{")
            end = item.find("}")
            var_name = item[start+1:end]
            
            # знайти значення змінної
            var_value = var_name
            for var in global_variables:
                if var['key'] == var_name and fun[0] > var['value'][0]:
                    var_value = str(var['value'][1])
                    break
            
            # додати змінну + все, що після дужки (кома, символи)
            ret_print.append(var_value + item[end+1:])
        else:
            # все інше просто як рядок
            ret_print.append(item)

    return ' '.join(ret_print)


def cheknut(fun):
    pos = None
    funcia = fun[1].split()
    if "=" in funcia:
        change = funcia[0]
        for var in global_variables:
            if var['key'] == change:
                pos = var['value'][0]
                break

        new_value = input()

        global_variables.set_update(change, pos, new_value)

    else:
        none_value = input()

    


    


commands_advanced = {
    'print': print_stm,
    'cheknut()': cheknut
}