from core.variables import global_variables
from core.executor import executor_start
import re

def parser_main(code, fail):
    fun = []  # список викликів функцій або рядків з { } / " " / ' '
    
    # список всіх функцій, які треба ловити
    function_names = [
        "print", "cheknut()", "sum", "pom", "riz", "dil", "napus"
    ]
    # regex для пошуку будь-якої функції з list
    func_pattern = re.compile(r"\b(" + "|".join(function_names) + r")\b")

    for i, line in enumerate(code):
        #veriables
        if "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()
            global_variables.set_variables(key=key, value=(i, value))

        # funck
        if func_pattern.search(line) or "{" in line or "}" in line or '"' in line or "'" in line:
            fun.clear()
            fun.append((i, line))
            executor_start(fun, fail)
            
        

