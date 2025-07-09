class Type:
    def __init__(self, name, complexity="O(1)"):
        self.name = name
        self.complexity = complexity

    def __str__(self):
        return f"{self.name} // {self.complexity}"

class IntType(Type):
    def __init__(self): super().__init__("int")

class BoolType(Type):
    def __init__(self): super().__init__("bool")

class StrType(Type):
    def __init__(self): super().__init__("str", "O(n)")

class UnknownType(Type):
    def __init__(self): super().__init__("unknown", "O(?)")

def parse_type(type_str: str):
    t = type_str.lower()
    return {
        "int": IntType(),
        "bool": BoolType(),
        "str": StrType()
    }.get(t, UnknownType())
