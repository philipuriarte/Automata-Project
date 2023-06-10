from graphviz import Digraph


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

# PDA image for (aba+bab) (a+b)* (bab) (a+b)* (a+b+ab+ba) (a+b+aa)*
pda_1 = "*insert PDA image*" # replace with pda image

# PDA image for ((101 + 111 + 101) + (1+0+11)) (1 + 0 + 01)* (111 + 000 + 101) (1+0)*
pda_2 = "*insert PDA image*" # replace with pda image


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

# Validate given string for DFA through an animation going through each state
def validate_dfa(dfa, string):
    current_state = dfa["start_state"]
    for char in string:
        if (current_state, char) in dfa["transitions"]:
            current_state = dfa["transitions"][(current_state, char)]
        else:
            return False
    return current_state in dfa["end_states"]


