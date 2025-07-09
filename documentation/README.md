InferLang Compiler Framework
===============================

Author: Arron Kian M. Parejas  
Course: 6IMSOFTENG - Implementation & Management of Software Engineering  
Semester: 1st Semester, AY 2025–2026  

----------------------------------------------------
📌 Project Title:
InferLang: A Type-Inference Engine for a Gradually Typed Programming Language Implemented with Time Complexity

----------------------------------------------------
📄 Description:
InferLang is a custom-built programming language prototype that supports both dynamic and static typing. It includes a Hindley-Milner-based type inference engine extended for gradual typing. This version introduces a modular compiler framework that tracks time complexity, evaluates typed expressions, and offers optimized compilation.

The framework is organized for speed, clarity, and future extensibility (LLVM, JS transpilation, etc.).

----------------------------------------------------
📦 Folder Structure:

App/
│
├── __main__.py         # CLI entry point
├── config.py           # Compile-time configuration (mode, optimization)
├── typesys.py          # Type system with complexity tracking
├── env.py              # Type and value environment
├── evaluator.py        # Core evaluator and inference logic
├── compiler.py         # Compiles a single line (let/print/expr)
└── repl.py             # REPL for interaction

----------------------------------------------------
🧠 Key Features:

✅ Gradual Typing (typed + untyped variables)  
✅ Type Inference (for literals and arithmetic)  
✅ Type Environment and Symbol Table  
✅ Time Complexity tracking (O(1), O(n), O(?))  
✅ Configurable Compilation Modes  
✅ Clean CLI Interface (REPL)  
✅ Modular and Extendable Design  

----------------------------------------------------
⚙️ Compile-Time Configuration:

Located in: config.py

- CONFIG.mode: fast / debug / strict
- CONFIG.optimize: True / False
- CONFIG.show_complexity: True / False

To check current config in REPL:
> config

----------------------------------------------------
🚀 How to Run:

1. Place all files in a folder named `inferlang/`
2. Open terminal and run:

    cd inferlang  
    python -m inferlang

----------------------------------------------------
📘 Sample REPL Session:

InferLang Framework REPL  
Type `exit` to quit | `env` for environment | `config` to view mode

>> let x = 5  
[~] x = 5 (int // O(1))

>> let name: str = "InferLang"  
[✓] name = InferLang (str // O(n))

>> print x + 10  
15 (int // O(1))

>> env  
x: int // O(1)  
name: str // O(n)

>> config  
CompileMode: fast, ShowComplexity: True, Optimize: True

----------------------------------------------------
📚 Technologies Used:

- Python 3.10+  
- Operator module (Python standard)  
- Regular Expressions  
- CLI / REPL (Read-Eval-Print Loop)  
- No third-party libraries needed

----------------------------------------------------
🧩 Planned Extensions (Future Work):

- AST and Optimization Passes  
- Full Function Support (with parameters + return types)  
- Recursion and Loop Time Complexity Analysis  
- Export to LLVM IR or JavaScript  
- CLI `--compile file.ilang` option  
- Web-based IDE or visualizer

----------------------------------------------------
📚 Technologies Used:

- Python 3.10+  
- Operator module (Python standard)  
- Regular Expressions  
- CLI / REPL (Read-Eval-Print Loop)  
- No third-party libraries needed

----------------------------------------------------
🔍 Research Conducted:

- Studied the Hindley-Milner type system and its relevance to modern statically-typed languages.
- Investigated how gradual typing bridges the gap between dynamic and static systems (e.g., TypeScript, Pyright).
- Explored type inference mechanisms and the limits of inferring types for complex and recursive expressions.
- Analyzed the impact of type annotations and inference on compile-time speed and runtime safety.
- Reviewed time complexity notations and how to integrate static complexity awareness into language design.

----------------------------------------------------
📖 What I Learned:

- How compilers infer types based on partial information and behavior patterns.
- How type safety can reduce runtime errors and improve software quality.
- The difficulty of balancing expressiveness and simplicity in a language's syntax and semantics.
- That modular design is essential for maintainability and scalability of language tools.
- That tracking time complexity at compile-time requires strong static analysis, especially for loops and recursion.

----------------------------------------------------
🔬 Findings:

- Gradual typing improves developer productivity by allowing flexible annotation and powerful inference.
- A modular compiler design (types, parser, evaluator, environment) improves clarity and makes it extensible.
- Time complexity tracking, even at a basic level, can help developers write more efficient code and understand algorithm performance.
- CLI tools like REPLs are invaluable for testing language behavior in real-time.

----------------------------------------------------
✅ Conclusion:

InferLang demonstrates that a small but robust gradually typed language with built-in type inference and complexity tracking can be created using Python. With modular components and a configuration system, the compiler is both fast and extensible. While the current version supports basic expressions, the structure allows future development such as function definitions, recursion analysis, and full IR compilation.

This project bridges Theoretical / Technical concepts in programming language design and practical compiler implementation, showcasing how academic principles like type systems and complexity analysis can be translated into real-world development tools.

----------------------------------------------------
🧩 Planned Extensions (Future Work):

- AST and Optimization Passes  
- Full Function Support (with parameters + return types)  
- Recursion and Loop Time Complexity Analysis  
- Export to LLVM IR or JavaScript  
- CLI `--compile file.ilang` option  
- Web-based IDE or visualizer

----------------------------------------------------
🔧 Maintained By:
Arron Kian M. Parejas  
Email: parejasarronkian@gmail.com  
School: Holy Angel University  

----------------------------------------------------
📄 License: MIT (For educational and academic use only)
