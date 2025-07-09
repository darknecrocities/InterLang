import operator, re
from app.typesys import IntType, BoolType, StrType, UnknownType
from app.config import CONFIG

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}

def infer_literal(expr):
    if re.match(r"^\d+$", expr):
        return int(expr), IntType()
    elif expr in ("true", "false"):
        return expr == "true", BoolType()
    elif re.match(r'^".*"$', expr):
        return expr.strip('"'), StrType()
    return None, UnknownType()

def evaluate_expr(expr: str, env):
    expr = expr.strip()

    # Literal
    val, typ = infer_literal(expr)
    if val is not None:
        return val, typ

    # Variable
    if expr in env.values:
        val = env.get_value(expr)
        typ = env.get_type(expr)
        return val, typ

    # Binary
    for op in OPS:
        if op in expr:
            left, right = expr.split(op, 1)
            val1, typ1 = evaluate_expr(left, env)
            val2, typ2 = evaluate_expr(right, env)
            if isinstance(typ1, IntType) and isinstance(typ2, IntType):
                result = OPS[op](val1, val2)
                return result, IntType()
            else:
                raise Exception(f"TypeError: Invalid types for {op}: {typ1} and {typ2}")
    raise Exception(f"Unknown expression: {expr}")
