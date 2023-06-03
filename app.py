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
    
    if "placeholder_text" not in st.session_state:
        st.session_state.placeholder_text = ""
    
    # Callback function for regex_input
    def regex_input_callbk():
        # Set disable for string_input and validity_button
        if st.session_state.regex_input == "--- Select ---":
            st.session_state.disabled = True
        else:
            st.session_state.disabled = False
        
        # Set placeholder text for string_input
        if st.session_state.regex_input == utils.regex_options[1]:
            st.session_state.placeholder_text = "abaababbab"
        elif st.session_state.regex_input == utils.regex_options[2]:
            st.session_state.placeholder_text = "101110001"
        
        # Clear string_input
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
        st.subheader("Regex to DFA, CFG, & PDA")
        st.markdown(
            '''
            1. Select a given Regex from the select box. The application will perform the conversion and display 
            the resulting DFA on the screen. Its corresponding CFG and PDA will be displayed on an expander below the DFA.
            2. Enter a string to check if it is valid for the DFA and then the program will check the 
            validity of the string by checking each state through an animation.
            '''
            )
        
        # Select box input to select regex
        regex_input = st.selectbox(
            label = "Select a Regular Expression",
            options = utils.regex_options,
            key="regex_input",
            on_change=regex_input_callbk
        )
        
        # Text input for string validation
        string_input = st.text_input(
            label = "Enter a string to check its validity for selected regex",
            key="string_input",
            disabled=st.session_state.disabled,
            placeholder=st.session_state.placeholder_text
        )
        
        # Validate button to run string validation
        validity_button = st.button(
            label = "Validate",
            disabled=st.session_state.disabled
        )
        
        # Output for regex_input, display dfa, cfg, and pda of selected regex
        if regex_input == utils.regex_options[1]:
            dfa = utils.generate_dfa_visualization(utils.dfa_1)
            st.graphviz_chart(dfa)

            with cfg_and_pda_exp:
                st.write("**Context Free Grammar**")
                st.markdown(utils.cfg_1)                
                st.write("**Pushdown Automata**")
                st.write(utils.pda_2)
        
        elif regex_input == utils.regex_options[2]:
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