from app.evaluator import evaluate_expr
from app.typesys import parse_type
from app.config import CONFIG

def compile_line(line: str, env):
    line = line.strip()
    if line.startswith("let "):
        lhs, rhs = line[4:].split("=", 1)
        rhs = rhs.strip()
        if ":" in lhs:
            name, type_hint = [s.strip() for s in lhs.split(":")]
            type_obj = parse_type(type_hint)
        else:
            name = lhs.strip()
            type_obj = None

        val, inferred = evaluate_expr(rhs, env)
        final_type = type_obj if type_obj else inferred
        env.define(name, val, final_type)

        prefix = "[✓]" if type_obj else "[~]"
        print(f"{prefix} {name} = {val} ({final_type})")
    elif line.startswith("print "):
        expr = line[6:]
        val, typ = evaluate_expr(expr, env)
        out = f"{val}"
        if CONFIG.show_complexity:
            out += f" ({typ})"
        print(out)
    elif line == "env":
        print(env)
    else:
        val, typ = evaluate_expr(line, env)
        print(f"Result: {val} ({typ})")
