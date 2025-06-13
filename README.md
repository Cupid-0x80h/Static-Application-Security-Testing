# Static Application Security Testing (SAST) Tool for a Simple Language

## 📌 Project Overview

This project is a **Static Application Security Testing (SAST) Tool** designed for a simple C-like language. It statically analyzes source code to identify basic security vulnerabilities such as:

- Hardcoded secrets (passwords, keys, tokens, etc.)
- Dangerous function calls (e.g., `gets()` that can lead to buffer overflows)

It demonstrates how compiler design principles (lexical analysis, parsing, AST generation, semantic analysis) can be practically applied to build security tools.

---

## 🛠 Why This Project?

- To **learn compiler design** by building a functional tool.
- Apply **project-based learning** approach.
- Gain knowledge in **cybersecurity vulnerability detection**.
- Implement real-world **SAST** concepts for secure coding practices.

---

## 🔍 What Does This Tool Do?

1. **Lexical Analysis (Lexer)**
   - Reads raw source code and tokenizes it into meaningful components (keywords, identifiers, numbers, symbols).
2. **Syntax Analysis (Parser)**
   - Parses tokens into an Abstract Syntax Tree (AST) following grammar rules.
3. **Semantic Analysis (Security Analyzer)**
   - Traverses the AST to identify specific security vulnerabilities.
4. **Reporting**
   - Outputs clear warnings indicating security issues with line numbers.

---

## 🚀 Project Timeline

| Date   | Milestone             | Description                          |
| ------ | --------------------- | ------------------------------------ |
| Jun 12 | Phase 1 & 2 Completed | Lexer and Parser with AST generation |
| Jun 13 | Phase 3 & 4 Completed | Security Analyzer and Reporter       |

---

## 📂 Project Structure

```
.
├── lexer.py          # Lexical Analyzer
├── parser.py         # Syntax Analyzer (Parser) & AST generator
├── analyzer.py       # Security Analyzer (Semantic Analyzer)
├── main.py           # main program
├── learnindocs.txt   # Learning Notes & Documentation
└── README.md         # Project Documentation
```

---

## 📦 Package Requirements

- Python >= 3.7
- PLY (Python Lex-Yacc)

### Install Dependencies

```bash
pip install ply
```

---

## 🔧 How to Run

1. Clone the repository:

```bash
git clone https://github.com/Cupid-0x80h/Static-Application-Security-Testing.git
cd Static-Application-Security-Testing
```

2. Run the `main.py` file:

```bash
python main.py
```

3. The script will:
   - Tokenize the provided sample code.
   - Parse it into AST.
   - Analyze the AST for security issues.
   - Report any vulnerabilities found.

---

## 📖 Key Concepts Learned

- **Compiler Front-End Development**

  - Lexical Analysis using Regular Expressions
  - Syntax Analysis with Custom Grammar Rules
  - Abstract Syntax Tree (AST) Design

- **Cybersecurity Principles**

  - Static Code Analysis
  - Identifying Hardcoded Secrets
  - Detecting Dangerous Functions (`gets()`)

- **Project-Based Learning Approach**

  - Learned by building complete end-to-end tool
  - Solved practical issues like circular imports
  - Used Visitor Pattern for AST traversal

---

## ⚠ Limitations & Future Work

- Currently supports very small subset of C-like language.
- Limited to hardcoded secrets & single dangerous function (`gets()`).
- Future improvements:
  - Add support for more complex language constructs.
  - Detect more vulnerability patterns (SQL Injection, Command Injection, etc.)
  - Extend AST to handle control structures (if, while, etc.)
  - Add configuration for rules.

---

## 📝 License

> This project currently does not include any license. Feel free to fork, study, modify, and experiment for educational purposes.

---

## 📧 Contact

If you have any questions, suggestions, or feedback feel free to connect!
