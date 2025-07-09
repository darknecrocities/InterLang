from app.typesys import Type, UnknownType

class TypeEnv:
    def __init__(self):
        self.types = {}
        self.values = {}

    def define(self, name, value, typ: Type):
        self.values[name] = value
        self.types[name] = typ

    def get_type(self, name):
        return self.types.get(name, UnknownType())

    def get_value(self, name):
        return self.values.get(name, None)

    def __str__(self):
        return "\n".join(f"{k}: {self.types[k]}" for k in self.types)
