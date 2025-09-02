1. Initial State: Sa

The farmer will initially be with the wolf, goat and cabbage altogether. So long as the farmer is with them, they will not get eaten by eachother. All four of the items, including the farmer will also be at the starting position, which is the initial side of the river.

2. Actions: 

States:
G = "have goat"
W = "have wolf"
C = "have cabbage"
I_S = "on the initial side"
F_S = "on the final side"
A = "alone"


Actions to take:
a_G = "take goat" 
a_W = "take wolf"
a_C = "take cabbage"
a_S = "change sides"
a_DG = "drop off goat"
a_DW = "drop off wolf"
a_DC = "drop off cabbage"

#Need the direction of travel and what he is carrying, including the ability to go alone

Actions(G) -> {a_S, a_DG}
Actions(W) -> {a_S, a_DW}
Actions(C) -> {a_S, a_DC}
Actions(I_S) -> {a_G, a_W, a_C, a_S, a_DG, a_DW, a_DC}
Actions(F_S) -> {a_G, a_W, a_C, a_S, a_DG, a_DW, a_DC}
Actions(A) -> {a_G, a_W, a_C, a_S}

#describe what a transition is like, what the operation of the transition is doing to change the state


3. Transition Model:

T(G, a_S) -> {F_S, I_S}
T(G, a_DG) -> A
T(W, a_S) -> {F_S, I_S}
T(W, a_DW) -> A
T(C, a_S) -> {F_S, I_S}
T(C, a_DC) -> A
T(I_S, a_G) -> G
T(I_S, a_W) -> W
T(I_S, a_C) -> C
T(I_S, a_S) -> F_S
T(I_S, a_DG) -> A
T(I_S, a_DW) -> A
T(I_S, a_DC) -> A
T(F_S, a_G) -> G
T(F_S, a_W) -> W
T(F_S, a_C) -> C
T(F_S, a_S) -> I_S
T(F_S, a_DG) -> A
T(F_S, a_DW) -> A
T(F_S, a_DC) -> A
T(A, a_G) -> G
T(A, a_W) -> W
T(A, a_C) -> C
T(A, a_S) -> {I_S, F_S}

4. Goal Test:

5. Path Cost: