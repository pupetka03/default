from core.variables import global_variables
import re

def parser_main(code):
    fun = []  # список викликів функцій або рядків з { } / " " / ' '
    
    # список всіх функцій, які треба ловити
    function_names = [
        "print", "cheknut()", "sum", "pom", "riz", "dil", "napus"
    ]
    # regex для пошуку будь-якої функції з list
    func_pattern = re.compile(r"\b(" + "|".join(function_names) + r")\b")

    for i, line in enumerate(code):
        if "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()
            global_variables.set_variables(key=key, value=(i, value))

        # якщо рядок містить функцію або { } або " "
        if func_pattern.search(line) or "{" in line or "}" in line or '"' in line or "'" in line:
            fun.append((i, line))


    return fun