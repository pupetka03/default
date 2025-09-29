class Variables():
    def __init__(self):
        self.global_variables = []


    def set_variables(self, **kwargs): 
        if not self.global_variables:
            self.global_variables.append(kwargs)
            return

        for i, var in enumerate(self.global_variables):
            if var["key"] == kwargs["key"]:
                self.global_variables[i] = kwargs
                break
        else:
            self.global_variables.append(kwargs)

    def set_update(self, key, pos, new_value):
        for var in self.global_variables:
            if var['key'] == key and var['value'][0] == pos:
                var['value'] = (pos, new_value)
                break

    def get_variables(self):
        return self.global_variables

    def __iter__(self):
        return iter(self.global_variables)
    
    def __str__(self):
        return str(self.global_variables)


global_variables = Variables()



