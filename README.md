# Compiler
## Compiler design using top-down analysis

G = ( {Z,I,D,L,X,K,O,S,E,R,T}, {var, : , id, , , integer, real, ; , :=, if, then,+}, P, Z)

P: <br>
Z → I S <br>
I → var D <br>
D → L : K O <br>
L → id X <br>
X → , L <br>
X → ε <br>
K → integer <br>
K → real <br>
O → ; D <br>
O →ε <br>
S → id := E <br>
S → if E then S <br>
E → T R <br>
R → + T R <br>
R → ε <br>
T → id <br>
