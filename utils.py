from graphviz import Digraph
import streamlit as st
import time

# List of regular expressions assigned to our group
regex_options = [
    "--- Select ---",
    "(aba+bab) (a+b)* (bab) (a+b)* (a+b+ab+ba) (a+b+aa)*",
    "((101 + 111 + 101) + (1+0+11)) (1 + 0 + 01)* (111 + 000 + 101) (1+0)*"
]

# DFA for (aba+bab) (a+b)* (bab) (a+b)* (a+b+ab+ba) (a+b+aa)*
dfa_1 = {
    "states": ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "T"],
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
        ("T", "a,b"): "T",
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
    "states": ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"],
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

# CFG for (aba+bab) (a+b)* (bab) (a+b)* (a+b+ab+ba) (a+b+aa)*
cfg_1 = '''
        S -> WXbabXYZ \n
        W -> aba | bab \n
        X -> aX | bX | ^ \n
        Y -> a | b | ab | ba \n
        Z -> aZ | bZ | aaZ | ^
        '''

# CFG for ((101 + 111 + 101) + (1+0+11)) (1 + 0 + 01)* (111 + 000 + 101) (1+0)*
cfg_2 = '''
        S -> WXYZ \n
        W -> 101 | 111 | 1 | 0 | 11 \n
        X -> 1X | 0X | 01X | ^ \n
        Y -> 111 | 000 | 101 \n
        Z -> 1Z | 0Z | ^
        '''

# PDA for (aba+bab) (a+b)* (bab) (a+b)* (a+b+ab+ba) (a+b+aa)*
pda_1 = {
    "states": ["Start", "Read1", "Read2", "Read3", "Read4", "Read5", "Read6", "Read7", 
               "Read8", "Read9", "Read10", "Read11", "Read12", "Read13", "Accept1", "Accept2"],
    "alphabet": ["a", "b"],
    "start_state": "Start",
    "push_states": [None],
    "pop_states": [None],
    "accept_states": ["Accept1", "Accept2"],
    "transitions": {
        ("Start", ""): "Read1",
        ("Read1", "a"): "Read2",
        ("Read1", "b"): "Read3",
        ("Read2", "b"): "Read4",
        ("Read3", "a"): "Read5",
        ("Read4", "a"): "Read6",
        ("Read5", "b"): "Read6",
        ("Read6", "b"): "Read7",
        ("Read7", "a"): "Read8",
        ("Read8", "b"): "Read9",
        ("Read9", "a"): "Read10",
        ("Read9", "b"): "Read11",
        ("Read10", "b"): "Read12",
        ("Read11", "a"): "Read13",
        ("Read10", "^"): "Accept1",
        ("Read11", "^"): "Accept1",
        ("Read12", "a, b, ^"): "Accept2",
        ("Read13", "a, b, ^"): "Accept2",
        ("Read6", "a"): "Read6",
        ("Read7", "b"): "Read7",
        ("Read8", "a"): "Read6",
        ("Read10", "a"): "Read10",
        ("Read11", "b"): "Read11",
    }
}

# PDA for ((101 + 111 + 101) + (1+0+11)) (1 + 0 + 01)* (111 + 000 + 101) (1+0)*
pda_2 = {
    "states": ["Start", "Read1", "Read2", "Read3", "Read4", "Read5", "Read6", "Read7", "Read8", "Accept"],
    "alphabet": ["1", "0"],
    "start_state": "Start",
    "push_states": [None],
    "pop_states": [None],
    "accept_states": ["Accept"],
    "transitions": {
        ("Start", ""): "Read1",
        ("Read1", "0,1"): "Read2",
        ("Read2", "0"): "Read3",
        ("Read2", "1"): "Read4",
        ("Read3", "0"): "Read5",
        ("Read3", "1"): "Read4",
        ("Read4", "0"): "Read7",
        ("Read4", "1"): "Read6",        
        ("Read6", "0"): "Read7",
        ("Read5", "0"): "Read8",        
        ("Read5", "1"): "Read4",
        ("Read6", "1"): "Read8",
        ("Read7", "1"): "Read8",
        ("Read7", "0"): "Read3",
        ("Read8", "0,1"): "Read8",
        ("Read8", "^"): "Accept",
    }
}



# Generate DFA visualization using Graphviz
def generate_dfa_visualization(dfa):
    dot = Digraph(engine="dot", graph_attr={'rankdir': 'LR'}, renderer="gd")

    # Add graph nodes for the states
    for state in dfa["states"]:
        if state in dfa["end_states"]:
            dot.node(state, shape="doublecircle")
        else:
            dot.node(state, shape="circle")

    # Add edges/transitions
    for transition, target_state in dfa["transitions"].items():
        source_state, symbol = transition
        dot.edge(source_state, target_state, label=symbol)

    # Return the Graphviz graph for the DFA visualization
    return dot


# Generate PDA visualization using Graphviz
def generate_pda_visualization(pda):
    dot = Digraph(engine="dot", renderer="gd")

    # Add graph nodes for the states
    for state in pda["states"]:
        if state in pda["start_state"] or state in pda["accept_states"]:
            dot.node(state, shape="ellipse")
        elif state in pda["push_states"]:
            dot.node(state, shape="rectangle")
        else:
            dot.node(state, shape="diamond")

    # Add edges/transitions
    for transition, target_state in pda["transitions"].items():
        source_state, symbol = transition
        dot.edge(source_state, target_state, label=symbol)

    # Return the Graphviz graph for the DFA visualization
    return dot


# Validate given string for DFA 
def validate_dfa(dfa, string):
    state_checks = []
    current_state = dfa["start_state"]

    # Iterate through each character in string
    for char in string:
        # Check if transition has "0,1", if so replace char with "0,1"
        if (current_state,"0,1") in dfa["transitions"].keys():
            char = "0,1"
        
        # Check if transition has "a,b", if so replace char with "a,b"
        if (current_state,"a,b") in dfa["transitions"].keys():
            char = "a,b"
        
        transition = (current_state, char)
        transition_exists = transition in dfa["transitions"].keys()
        state_checks.append((current_state, transition_exists))

        # Check if current char is in transitions
        if transition_exists:
            current_state = dfa["transitions"][transition]
        # Return False if current character in the string is not in the dfa transitions
        else:
            return False
    
    # Add state check for last transition
    if current_state in dfa["end_states"]:
        state_checks.append((current_state, True))
    else:
        state_checks.append((current_state, False))

    result = current_state in dfa["end_states"] # Checks if last current_state is in dfa end_states

    # Return the validation result and state_checks array
    return (result, state_checks)


# Generate validation animation
def animate_dfa_validation(dfa, state_checks):
    dot = generate_dfa_visualization(dfa)  # Generate the DFA visualization
    graph = st.graphviz_chart(dot.source, use_container_width=True) # Create a Streamlit Graphviz component

    # Iterate through each state in state_checks
    for state_check in state_checks:
        state, is_valid = state_check

        time.sleep(1)  # Add a delay for visualization purposes

        if is_valid and state in dfa["end_states"]:
            dot.node(state, style="filled", fillcolor="green")  # Set end state to green
            graph.graphviz_chart(dot.source, use_container_width=True) # Render the updated visualization

        elif not is_valid:
            dot.node(state, style="filled", fillcolor="red")  # Set invalid state to red
            graph.graphviz_chart(dot.source, use_container_width=True) # Render the updated visualization

        else:
            dot.node(state, style="filled", fillcolor="yellow") # Set state to yellow if True                
            graph.graphviz_chart(dot.source, use_container_width=True) # Render the updated visualization

            time.sleep(0.5)  # Add a delay for blink effect
            dot.node(state, style="filled", fillcolor="white") # Set previous state back to white            
            graph.graphviz_chart(dot.source, use_container_width=True) # Render the updated visualization
