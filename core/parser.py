from core.variables import global_variables
from core.executor import executor_start
import re

def parser_main(code, fail):
    fun = []  # список викликів функцій або рядків з { } / " " / ' '
    
    # список всіх функцій, які треба ловити
    function_names = [
        "nadpys", "cheknut", "sum", "pom", "riz", "dil"
    ]
    # regex для пошуку будь-якої функції з list
    func_pattern = re.compile(r"\b(" + "|".join(function_names) + r")\b")

    for i, line in enumerate(code):
        #veriables
        if "=" in line:
            parts = line.split("=", 1)
            var_type = parts[0].split()[0]
            key = parts[0].split()[1]
            value = parts[1].split()[0]

            #key, value = line.split("=", 1)
            #key = keystrip()
            #value = value.strip()
            global_variables.set_variables(key=key, value=(i, var_type, value))

        # funck
        if func_pattern.search(line) or "{" in line or "}" in line or '"' in line or "'" in line:
            fun.clear()
            fun.append((i, line))
            executor_start(fun, fail)
            
        

