from tc.ap import AP

Q = {'q0', 'q1', 'q2'}
S = {'0', '1'}
G = {'0', '1', 'X'}
D = {
  ('q0', '1', 'X'): ('q1', ['X', 'X']),
  ('q1', '1', 'X'): ('q1', ['X', 'X']),
  ('q0', '0', 'X'): ('q0', []),
  ('q1', '0', 'X'): ('q0', []),
}
M = (Q, S, G, D, 'q0', 'X', {'q1'})

automato = AP(Q, S, G, D, 'q0', 'X', {'q1'})

automato.computa('111')