import streamlit as st
import utils


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
    cfg_and_pda_exp = st.expander("Show CFG and PDA Conversion")

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
        regex_input = st.selectbox("Select a Regular Expression", utils.regex_options, key="regex_input", on_change=regex_input_callbk)
        string_input = st.text_input("Enter a string to check its validity for selected regex", key="string_input", disabled=st.session_state.disabled)
        validity_button = st.button("Validate", disabled=st.session_state.disabled)
        
        # Output for regex_input, display dfa, cfg, and pda of selected regex
        if regex_input == "(aba+bab) (a+b)* (bab) (a+b)* (a+b+ab+ba) (a+b+aa)*":
            dfa = utils.generate_dfa_visualization(utils.dfa_1)
            st.graphviz_chart(dfa)

            with cfg_and_pda_exp:
                st.write("**Context Free Grammar**")
                st.markdown(utils.cfg_1)                
                st.write("**Pushdown Automata**")
                st.write(utils.pda_2)
        
        elif regex_input == "((101 + 111 + 101) + (1+0+11)) (1 + 0 + 01)* (111 + 000 + 101) (1+0)*":
            dfa = utils.generate_dfa_visualization(utils.dfa_2)
            st.graphviz_chart(dfa)

            with cfg_and_pda_exp:
                st.write("**Context Free Grammar**")
                st.markdown(utils.cfg_2)                
                st.write("**Pushdown Automata**")
                st.write(utils.pda_2)

        # Output for string_input, play validation animation on displayed dfa
        if validity_button or string_input:
            string_input = string_input.replace(" ", "")# Removes any whitespaces

            if len(string_input) == 0:
                st.warning("Please enter a string to validate first")
            else:
                st.write("Entered String: ", string_input)
                st.write("Success!")
                st.write("*Display Animation*")
                st.write("String Validation not implemented yet")


if __name__ == "__main__":
    main()
