import streamlit as st


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
    # Create container to group blocks of code
    title_con = st.container()
    regex_to_dfa_con = st.container()
    cfg_to_pda_con = st.container()

    # Code block for title and description
    with title_con:
        st.title("Automata Project")
        st.markdown(
            '''
            This project is a web application that allows you to convert regular expressions to Deterministic Finite Automata (DFA) 
            and Context-Free Grammars (CFG) to Pushdown Automata (PDA). Simplify your automata conversion tasks with just a few clicks!
            '''
            )
        st.divider()

    # Code block for regex to dfa feature
    with regex_to_dfa_con:
        st.subheader("Regex to DFA Converter")
        st.markdown(
            '''
            1. Enter your regular expression in the provided input field.
            2. Click the "Convert to DFA" button.
            3. The application will perform the conversion and display the resulting DFA on the screen.
            '''
            )
        
        regex_input = st.text_input("Enter a regular expression")

        if st.button("Convert to DFA"):
            dfa = convert_regex_to_dfa(regex_input)
            st.write("DFA:")
            st.write(dfa)

        st.divider()
    
    # Code block for cfg to pda feature
    with cfg_to_pda_con:
        st.subheader("CFG to PDA Converter")
        st.markdown(
            '''
            1. Enter your Context-Free Grammar (CFG) in the provided input field.
            2. Click the "Convert to PDA" button.
            3. The application will perform the conversion and display the resulting Pushdown Automaton (PDA) on the screen.
            '''
            )

        cfg_input = st.text_input("Enter CFG")

        if st.button("Convert to PDA"):
            cfg = convert_cfg_to_pda(cfg_input)
            st.write("CFG:")
            st.write(cfg)


if __name__ == "__main__":
    main()
