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
    current_state = dfa["start_state"]
    for char in string:
        found_transition = False
        for transition, target_state in dfa["transitions"].items():
            state, symbols = transition
            if state == current_state and char in symbols:
                current_state = target_state
                found_transition = True
                break
        if not found_transition:
            return False
    return current_state in dfa["end_states"]

