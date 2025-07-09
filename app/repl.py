from app.env import TypeEnv
from app.compiler import compile_line
from app.config import CONFIG

def start_repl():
    print("InferLang Framework REPL")
    print("Type `exit` to quit | `env` for environment | `config` to view mode\n")
    env = TypeEnv()

    while True:
        try:
            line = input(">> ").strip()
            if line == "exit":
                break
            elif line == "config":
                print(CONFIG)
            elif line:
                compile_line(line, env)
        except Exception as e:
            print("Error:", e)
