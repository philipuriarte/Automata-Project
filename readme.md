# Automata Project
This project is a web application that will convert the given regular expressions below to Deterministic Finite Automata (DFA) and Context-Free Grammars (CFG) to Pushdown Automata (PDA).

**Regular Expressions**
1. `(aba+bab) (a+b)* (bab) (a+b)* (a+b+ab+ba) (a+b+aa)*`
2. `((101 + 111 + 101) + (1+0+11)) (1 + 0 + 01)* (111 + 000 + 101) (1+0)*`

## Features
- Conversion of Regular Expressions to DFAs: Easily convert the provided regular expressions to their corresponding DFA representations.
- String Validation: Enter a string and check if it is valid for the DFA. The application will animate the DFA's state transitions, highlighting correct and incorrect paths.
- Conversion of CFGs to PDAs: Enter a Context-Free Grammar (CFG) and convert it to a PDA.

## Technologies Used
- Python: Backend logic and conversion algorithms are implemented in Python.
- Streamlit: Web application framework used to build the user interface.
- Graphviz: Library used for generating graphical visualizations of automata.

## Developers
- De Salit, John Patrick
- Gamit, Mary Josephine
- Uriarte, Philip Ronin
- Uy, Richard Tyrese Michio