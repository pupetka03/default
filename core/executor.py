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
    fun, variables = parser_main(code)
    size = len(fun)

    code = " "

    for i in range(size):
        function_commands = fun[i]
        function_commands_name = function_commands[1].split()[0]

        if function_commands_name in commands_advanced:
            result = commands_advanced[function_commands_name](function_commands, variables)
            code += f"{result}\n"

    print(code.strip())

    save_output_in_same_dir(file_path, code)