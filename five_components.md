1. Initial State: Sa

The farmer will initially be with the wolf, goat and cabbage altogether. So long as the farmer is with them, they will not get eaten by eachother. All four of the items, including the farmer will also be at the starting position, which is the initial side of the river.

2. Actions: 
#Need the direction of travel and what he is carrying, including the ability to go alone

States:
(Wolf, Goat, Cabbage, Farmer)

0 = Start
1 = Other Side

0   0000
1	0001
2	0010
3	0011
4	0100
5	0101
6	0110
7	0111
8	1000
9	1001
10	1010
11	1011
12	1100
13	1101
14	1110
15	1111


Actions To Take:
A = Take Wolf
B = Take Goat
C = Take Cabbage
D = Farmer Alone

Actions(0) -> {A, B, C, D}
Actions(1) -> {None}
Actions(2) -> {A, B, D}
Actions(3) -> {None}
Actions(4) -> {A, C, D}
Actions(5) -> {B, D}
Actions(6) -> {None}
Actions(7) -> {B, C, D}
Actions(8) -> {B, C, D}
Actions(9) -> {None}
Actions(10) -> {B, D}
Actions(11) -> {A, C, D}
Actions(12) -> {None}
Actions(13) -> {A, B, D}
Actions(14) -> {None}
Actions(15) -> {None}




#describe what a transition is like, what the operation of the transition is doing to change the state


3. Transition Model:

States:
(Wolf, Goat, Cabbage, Farmer)

0 = Start
1 = Other Side

0   0000
1	0001
2	0010
3	0011
4	0100
5	0101
6	0110
7	0111
8	1000
9	1001
10	1010
11	1011
12	1100
13	1101
14	1110
15	1111


Actions To Take:
A = Take Wolf
B = Take Goat
C = Take Cabbage
D = Farmer Alone


Transition(0, A) -> 9
Transition(0, B) -> 5
Transition(0, C) -> 3
Transition(0, D) -> 14
Transition(2, A) -> 11
Transition(2, B) -> 7
Transition(2, D) -> 3
Transition(4, A) -> 12
Transition(4, C) -> 6
Transition(4, D) -> 5
Transition(5, B) -> 0
Transition(5, D) -> 4
Transition(7, B) -> 2
Transition(7, C) -> 4
Transition(7, D) -> 6
Transition(8, B) -> 13
Transition(8, C) -> 11
Transition(8, D) -> 9
Transition(10, B) -> 15 (success)
Transition(10, D) -> 11
Transition(11, A) -> 2
Transition(11, C) -> 8
Transition(11, D) -> 10
Transition(13, A) -> 4
Transition(13, B) -> 8
Transition(13, D) -> 12





4. Goal Test:

5. Path Cost: