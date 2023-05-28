import streamlit as st
from graphviz import Digraph


# Define a sample DFA
sample_dfa = {
    "nodes": ["A", "B", "C"],
    "alphabet": ["0", "1"],
    "start_state": "A",
    "accept_states": ["C"],
    "transitions": {
        ("A", "0"): "B",
        ("A", "1"): "A",
        ("B", "0"): "B",
        ("B", "1"): "C",
        ("C", "0"): "B",
        ("C", "1"): "A"
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
    dot = Digraph()

    # Add nodes
    for node in dfa["nodes"]:
        if node in dfa["accept_states"]:
            dot.node(node, shape="doublecircle")
        else:
            dot.node(node, shape="circle")

    # Add edges/transitions
    for transition, target_state in dfa["transitions"].items():
        source_state, symbol = transition
        dot.edge(source_state, target_state, label=symbol)

    # Return the Graphviz source code for the DFA visualization
    return dot.source


# Convert Regex to DFA function
def convert_regex_to_dfa(regex):
    # Placeholder implementation
    # Replace with actual conversion logic
    dfa = "Regex to DFA conversion not implemented yet"
    return dfa


# Convert CFG to PDA function
def convert_cfg_to_pda(cfg):
    # Placeholder implementation
    # Replace with actual conversion logic
    pda = "CFG to PDA conversion not implemented yet"
    return pda


# Streamlit interface
def main():
    # Set page title and icon
    st.set_page_config(
        page_title="Automata Project",
        page_icon="🔀"
    )

    # Add streamlit session state values
    if "disabled" not in st.session_state:
        st.session_state.disabled = True
    
    if "text" not in st.session_state:
        st.session_state.text = ""
    
    # callback for regex_input
    def regex_input_callbk():
        if st.session_state.regex_input == "--- Select ---":
            st.session_state.disabled = True
        else:
            st.session_state.disabled = False

    # Create container to group blocks of code
    title_con = st.container()
    sample_expander = st.expander("See Sample")
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

    # Code block to test if graphviz is able to display DFA's with streamlit
    with sample_expander:
        st.write("**DFA Visualization Using Graphviz Library**")

        col1, col2 = st.columns(2)
        with col1:
            st.write("**Regex**:")
            st.write("(0+1)*1(0+1)")
        with col2:
            st.write("**DFA**:")
            dfa_visualization = generate_dfa_visualization(sample_dfa)
            st.graphviz_chart(dfa_visualization)

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
        
        regex_input = st.selectbox("Select a Regular Expression", regex_options, on_change=regex_input_callbk, key="regex_input")
        string_input = st.text_input("Enter a string to check its validity for selected regex", disabled=st.session_state.disabled)
        validity_button = st.button("Check Validity", disabled=st.session_state.disabled)
        
        # Output for regex_input, display dfa of converted selected regex
        if regex_input != "--- Select ---":
            dfa = convert_regex_to_dfa(regex_input)
            st.write(dfa)

        # Output for string_input, play validation animation on displayed dfa
        if validity_button:
            if string_input == "":
                st.warning("Please enter a string to validate first")
            else:
                st.write("Success!")
                dfa = convert_regex_to_dfa(string_input)
                st.write("*Display Animation*")
                st.write("String Validation not implemented yet")

        st.divider()
    
    # Code block for cfg to pda feature
    # with cfg_to_pda_con:
    #     st.write("***STILL UNDER DEVELOPMENT***")
    #     st.subheader("CFG to PDA Converter")
    #     st.markdown(
    #         '''
    #         1. Enter your Context-Free Grammar (CFG) in the provided input field.
    #         2. Click the "Convert to PDA" button.
    #         3. The application will perform the conversion and display the resulting Pushdown Automaton (PDA) on the screen.
    #         '''
    #         )

    #     cfg_input = st.text_input("Enter CFG")

    #     if st.button("Convert to PDA"):
    #         cfg = convert_cfg_to_pda(cfg_input)
    #         st.write("CFG:")
    #         st.write(cfg)


if __name__ == "__main__":
    main()
