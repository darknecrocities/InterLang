import re
import operator

# --- Type System with Time Complexity ---

class Type:
    def __init__(self, name: str, complexity: str = "O(1)"):
        self.name = name
        self.complexity = complexity

    def __str__(self):
        return f"{self.name} // {self.complexity}"

class IntType(Type):
    def __init__(self): super().__init__("int", "O(1)")

class BoolType(Type):
    def __init__(self): super().__init__("bool", "O(1)")

class StrType(Type):
    def __init__(self): super().__init__("str", "O(n)")

class UnknownType(Type):
    def __init__(self): super().__init__("unknown", "O(?)")

# --- Type Environment ---

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
        return self.values.get(name)

    def __str__(self):
        return "\n".join([f"{k}: {self.types[k]}" for k in self.types])

# --- Parser and Evaluator ---

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}

def infer_type(value):
    if isinstance(value, int):
        return IntType()
    elif isinstance(value, bool):
        return BoolType()
    elif isinstance(value, str):
        return StrType()
    return UnknownType()

def evaluate_expr(expr, env: TypeEnv):
    expr = expr.strip()
    try:
        if re.match(r"^\d+$", expr):
            return int(expr), IntType()
        elif expr in ("true", "false"):
            return expr == "true", BoolType()
        elif re.match(r"^\".*\"$", expr):
            return expr.strip('"'), StrType()
        elif expr in env.values:
            val = env.get_value(expr)
            return val, env.get_type(expr)
        else:
            for op in OPERATORS:
                if op in expr:
                    left, right = expr.split(op, 1)
                    val1, type1 = evaluate_expr(left.strip(), env)
                    val2, type2 = evaluate_expr(right.strip(), env)
                    if isinstance(type1, IntType) and isinstance(type2, IntType):
                        result = OPERATORS[op](val1, val2)
                        return result, IntType()
                    else:
                        raise Exception(f"TypeError: Cannot apply {op} to {type1.name} and {type2.name}")
    except Exception as e:
        raise Exception(f"Evaluation Error: {e}")
    return None, UnknownType()

# --- Command Evaluator ---

def execute(line: str, env: TypeEnv):
    line = line.strip()
    if line.startswith("let "):
        content = line[4:]
        if '=' not in content:
            raise Exception("Syntax Error: Missing '=' in declaration.")
        lhs, rhs = content.split("=", 1)
        lhs = lhs.strip()
        rhs = rhs.strip()

        if ':' in lhs:
            name, type_name = [s.strip() for s in lhs.split(':')]
            typ = parse_type(type_name)
        else:
            name = lhs
            typ = None

        value, inferred_type = evaluate_expr(rhs, env)
        final_type = typ if typ else inferred_type
        env.define(name, value, final_type)
        status = "[✓]" if typ else "[~]"
        print(f"{status} '{name}' defined as {final_type}")
    elif line == "env":
        print("Environment:\n", env)
    elif line.startswith("print "):
        expr = line[6:]
        val, typ = evaluate_expr(expr, env)
        print(f"Output: {val} ({typ})")
    else:
        val, typ = evaluate_expr(line, env)
        print(f"Expr Result: {val} ({typ})")

def parse_type(s: str) -> Type:
    s = s.lower()
    if s == "int": return IntType()
    elif s == "bool": return BoolType()
    elif s == "str": return StrType()
    else: return UnknownType()

# --- REPL ---

def repl():
    print("InferLang v2 — Optimized Gradual Typing Engine")
    print("Supports expressions, typing, and complexity. Type 'env' or 'exit'.\n")
    env = TypeEnv()
    while True:
        try:
            line = input(">> ")
            if line.strip() == "exit":
                break
            execute(line, env)
        except Exception as e:
            print("Error:", e)

# --- Entry ---

if __name__ == "__main__":
    repl()