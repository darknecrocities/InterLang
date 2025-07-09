# 🔍 InferLang

**A Type-Inference Engine for a Gradually Typed Programming Language Implemented with Time Complexity**  
*Author: Arron Kian M. Parejas*

---

## 🧩 Project Overview

InferLang is a custom-designed programming language that supports both **dynamic** and **static typing**, embodying the principles of **gradual typing**. It features a robust type-inference engine capable of deducing types from minimal annotations and code behavior. This hybrid approach empowers developers to write flexible code with compile-time safety.

---

## ❓ Problem Statement

Languages like **Python** and **JavaScript** are dynamically typed, offering flexibility but lacking compile-time safety, which leads to runtime errors. On the other hand, statically typed languages provide more safety but are often verbose and less adaptable.

**Gradual typing** attempts to combine the best of both worlds, but current tools fall short in intelligent type inference and developer support. InferLang addresses this gap with a focus on:
- Robust inference engine
- Meaningful error reporting
- Typed intermediate representation generation

---

## 🎯 Project Objectives

- 🛠️ **Design a custom gradually typed language** that seamlessly blends dynamic and static typing.
- 🔎 **Develop a type-inference engine** that infers types from partial annotations and code behavior.
- 🧠 **Implement error checking and suggestions** for untyped or inconsistently typed code.
- 🔄 **Generate type-safe intermediate representations (IRs)** for optimization or compilation (LLVM or JavaScript).

---

## 👥 Target Users

- 🧑‍💻 Language designers and compiler researchers
- 💼 Developers in type-sensitive domains (e.g., fintech, healthtech)
- 🎓 Educators and students exploring type systems and PL theory

---

## 📦 Project Scope

### ✅ **Inclusions**
- Minimal programming language syntax with typed & untyped variables
- Hindley-Milner-based inference engine (with gradual typing extensions)
- Type-checker with diagnostic and correction suggestions
- CLI-based REPL and compilation interface
- Optional export to LLVM IR or JavaScript

### ❌ **Exclusions**
- Full-featured standard library (only basic types/operators included)
- GUI-based IDE (text-based interface only)
- Integration with third-party modules or packages

---

## 🛠️ Technologies To Be Used

| Category           | Tool / Technology               |
|--------------------|----------------------------------|
| Language           | Python or Rust                   |
| Parser Generator   | ANTLR (or Lark for Python)       |
| Type System        | Hindley-Milner, Gradual Typing   |
| IR Target          | Custom IR / LLVM / JavaScript    |
| Testing            | PyTest / Rust Test System        |
| Documentation      | MkDocs / LaTeX                   |

---

## ⚠️ Anticipated Challenges

1. **Syntax Design:** Crafting an intuitive but expressive syntax for gradual typing.
2. **Type Inference Edge Cases:** Handling inference for complex cases like higher-order functions, recursion, or nested closures.
3. **Balancing Semantics:** Ensuring the right trade-off between static guarantees and dynamic flexibility without bloating the language semantics.

---

## 🚀 Project Status

📍 *Planning and Architecture Design Phase*  
🧪 Type Inference Prototyping Underway

---

## 📄 License

[MIT License](./LICENSE) • © 2025 Arron Kian M. Parejas

---
