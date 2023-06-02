import streamlit as st
from graphviz import Digraph


# DFA for (aba+bab) (a+b)* (bab) (a+b)* (a+b+ab+ba) (a+b+aa)*
dfa_1 = {
    "nodes": ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "T"],
    "alphabet": ["a", "b"],
    "start_state": "q1",
    "end_states": ["q10", "q11"],
    "transitions": {
        ("q1", "a"): "q2",
        ("q2", "b"): "q3",
        ("q3", "a"): "q6",
        ("q1", "b"): "q4",
        ("q4", "a"): "q5",
        ("q5", "b"): "q6",
        ("q2", "a"): "T",
        ("q3", "b"): "T",
        ("q4", "b"): "T",
        ("q5", "a"): "T",
        ("q6", "a"): "q6",
        ("q6", "b"): "q7",
        ("q7", "b"): "q7",
        ("q7", "a"): "q8",
        ("q8", "a"): "q6",
        ("q8", "b"): "q9",
        ("q9", "a"): "q10",
        ("q9", "b"): "q11",
        ("q10", "a"): "q10",
        ("q11", "b"): "q11",
        ("q10", "b"): "q11",
        ("q11", "a"): "q10",
    }
}

# DFA for ((101 + 111 + 101) + (1+0+11)) (1 + 0 + 01)* (111 + 000 + 101) (1+0)*
dfa_2 = {
    "nodes": ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"],
    "alphabet": ["1", "0"],
    "start_state": "q1",
    "end_states": ["q8"],
    "transitions": {
        ("q1", "0,1"): "q2",
        ("q2", "1"): "q3",
        ("q2", "0"): "q4",
        ("q3", "0"): "q5",
        ("q3", "1"): "q6",
        ("q4", "1"): "q3",
        ("q4", "0"): "q7",
        ("q5", "1"): "q8",
        ("q5", "0"): "q7",
        ("q6", "0"): "q5",
        ("q6", "1"): "q8",
        ("q7", "1"): "q3",
        ("q7", "0"): "q8",
        ("q8", "0,1"): "q8",
    }
}

# List of regular expressions assigned to our group
regex_options = [
    "--- Select ---",
    "(aba+bab) (a+b)* (bab) (a+b)* (a+b+ab+ba) (a+b+aa)*",
    "((101 + 111 + 101) + (1+0+11)) (1 + 0 + 01)* (111 + 000 + 101) (1+0)*"
]


# Generate DFA visualization using Graphviz
def generate_dfa_visualization(dfa):
    dot = Digraph(engine="dot", graph_attr={'rankdir': 'LR'}, renderer="gd")

    # Add nodes
    for node in dfa["nodes"]:
        if node in dfa["end_states"]:
            dot.node(node, shape="doublecircle")
        else:
            dot.node(node, shape="circle")

    # Add edges/transitions
    for transition, target_state in dfa["transitions"].items():
        source_state, symbol = transition
        dot.edge(source_state, target_state, label=symbol)

    # Return the Graphviz source code for the DFA visualization
    return dot

# Validate given string for DFA through an animation going through each state
def validate_dfa(dfa, string):
    pass


# Streamlit interface
def main():
    # Set page title and icon
    st.set_page_config(
        page_title="Automata Project",
        page_icon="🔀"
    )

    # Initialize streamlit session state values
    if "disabled" not in st.session_state:
        st.session_state.disabled = True
    
    # Callback function for regex_input
    def regex_input_callbk():
        if st.session_state.regex_input == "--- Select ---":
            st.session_state.disabled = True
        else:
            st.session_state.disabled = False
        
        st.session_state.string_input = ""
    

    # Create container to group blocks of code
    title_con = st.container()
    st.divider()
    regex_to_dfa_con = st.container()
    cfg_to_pda_con = st.container()

    # Code block for title and description
    with title_con:
        st.title("Automata Project")
        st.markdown(
            '''
            This project is a web application that will convert the given regular expressions below to Deterministic Finite Automata (DFA) 
            and Context-Free Grammars (CFG) to Pushdown Automata (PDA).

            **Regular Expressions**
            1. `(aba+bab) (a+b)* (bab) (a+b)* (a+b+ab+ba) (a+b+aa)*`
            2. `((101 + 111 + 101) + (1+0+11)) (1 + 0 + 01)* (111 + 000 + 101) (1+0)*`

            '''
            )

    # Code block for regex to dfa feature
    with regex_to_dfa_con:
        st.subheader("Regex to DFA Converter")
        st.markdown(
            '''
            1. Select a given Regex from the select box. The application will perform the conversion and display 
            the resulting DFA on the screen.            
            2. Enter a string to check if it is a valid string for the DFA and then the program will check the 
            validity of the string by checking each state.
            '''
            )
        
        # Input Widgets
        regex_input = st.selectbox("Select a Regular Expression", regex_options, key="regex_input", on_change=regex_input_callbk)
        string_input = st.text_input("Enter a string to check its validity for selected regex", key="string_input", disabled=st.session_state.disabled)
        validity_button = st.button("Validate", disabled=st.session_state.disabled)
        
        # Output for regex_input, display dfa of converted selected regex
        if regex_input == "(aba+bab) (a+b)* (bab) (a+b)* (a+b+ab+ba) (a+b+aa)*":
            dfa = generate_dfa_visualization(dfa_1)
            st.graphviz_chart(dfa)
        elif regex_input == "((101 + 111 + 101) + (1+0+11)) (1 + 0 + 01)* (111 + 000 + 101) (1+0)*":
            dfa = generate_dfa_visualization(dfa_2)
            st.graphviz_chart(dfa)

        # Output for string_input, play validation animation on displayed dfa
        if validity_button:
            string_input.strip()

            if len(string_input) == 0:
                st.warning("Please enter a string to validate first")
            else:
                st.write("Entered String: ", string_input)
                st.write("Success!")
                st.write("*Display Animation*")
                st.write("String Validation not implemented yet")


if __name__ == "__main__":
    main()
