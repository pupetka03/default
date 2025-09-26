import sys, os
from core.parser import parser_main
from commands.advanced import commands_advanced

def resource_path(relative_path):

    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def save_output_in_same_dir(file_path, content):
    output_dir = os.path.dirname(os.path.abspath(file_path))
    output_file = os.path.join(output_dir, "output.txt")

    with open(output_file, "w") as f:
        f.write(content.strip())


def executor(code, file_path):
    fun = parser_main(code)
    size = len(fun)

    code = " "
    code_for_terminal = ' '

    def search_commands(function_commands_name, function_commands):
        nonlocal code
        if function_commands_name in commands_advanced:
            result = commands_advanced[function_commands_name](function_commands)
            if result is not None:
                code += f"{result}\n"
                code_for_terminal = f"{result}"
                print(code_for_terminal.strip())



    for i in range(size):
        function_commands = fun[i]

        if "=" in function_commands[1]:
            func_commands_name = function_commands[1].split()[2]
            search_commands(func_commands_name, function_commands)
        #print(function_commands)


        function_commands_name = function_commands[1].split()[0]
        search_commands(function_commands_name, function_commands)
        #print(f"function_commands_name: {function_commands_name}")


    save_output_in_same_dir(file_path, code)