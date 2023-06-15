# Automata Project

This project is a web application that converts given regular expressions to Deterministic Finite Automata (DFA), Context-Free Grammars (CFG), and Pushdown Automata (PDA).

## Python Libraries Used

- Streamlit: Web application framework used to build the user interface.
- Graphviz: Library used for generating DFA and PDA graphical visualizations.

## Regular Expressions

1. `(aba+bab) (a+b)* (bab) (a+b)* (a+b+ab+ba) (a+b+aa)*`
2. `((101 + 111 + 101) + (1+0+11)) (1 + 0 + 01)* (111 + 000 + 101) (1+0)*`

## How to Use

1. Select a regular expression from the dropdown menu. The application will perform the conversion and display the resulting DFA on the screen. Its corresponding CFG and PDA will be displayed below the DFA.
2. Enter a string to check its validity for the displayed DFA. Click the "Validate" button to run the string validation.
3. The application will check the validity of the string by animating each state of the DFA.

## Code Explanation

The code is divided into two files: `app.py` and `utils.py`.

### app.py

The `app.py` file contains the main Streamlit interface and the logic for the web application.

#### Streamlit Interface

The Streamlit interface is set up using the `streamlit` library. The page title and icon are set using `st.set_page_config`. Streamlit session state values are initialized using `st.session_state`.

#### Regular Expression Input

A callback function `regex_input_callbk` is defined to handle changes in the selected regular expression. It sets the disable state for the string input and validate button, and updates the placeholder text for the string input based on the selected regular expression.

The regular expression is selected using a select box (`st.selectbox`) and stored in the `regex_input` variable. The string input is obtained using a text input (`st.text_input`) and stored in the `string_input` variable. The validate button is created using `st.button`.

#### Displaying DFA, CFG, and PDA

The DFA, CFG, and PDA corresponding to the selected regular expression are displayed using `st.graphviz_chart` and `st.markdown`. The DFA visualization is generated using the `generate_dfa_visualization` function from `utils.py`.

#### String Validation

The entered string is validated using the `validate_dfa` function from `utils.py`. The string input is checked for validity and the result is displayed using `st.success`, `st.error`, and `st.warning`. The state checks are also displayed.

### utils.py

The `utils.py` file contains utility functions and data structures used in the application.

#### Regular Expressions and Automata Definitions

The regular expressions and corresponding DFAs, CFGs, and PDAs are defined as variables in the file. Each regular expression is represented as a string, and the automata are represented as dictionaries with the states, alphabet, start state, end states, and transitions.

#### DFA Visualization

The `generate_dfa_visualization` function generates a Graphviz graph for visualizing the DFA. It uses the `Digraph` class from the `graphviz` library. Nodes are added for each state, and edges are added for each transition.

#### PDA Visualization

The `generate_pda_visualization` function generates a Graphviz graph for visualizing the PDA. It follows a similar approach to the DFA visualization.

#### String Validation

The `validate_dfa` function validates a given string for a DFA. It checks each character of the string against the transitions of the DFA and returns a list of state checks indicating whether the transitions exist for each character. The function also handles special cases where transitions have multiple symbols

## Developers
- De Salit, John Patrick
- Gamit, Mary Josephine
- Uriarte, Philip Ronin
- Uy, Richard Tyrese Michio