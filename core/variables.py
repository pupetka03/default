class Variables():
    def __init__(self):
        self.global_variables = []


    def set_variables(self, **kwargs): 
        self.global_variables.append(kwargs)


    def get_variables(self):
        return self.global_variables



global_variables = Variables()



