from tc.afd import AFD

# DEFINIÇÂO DO AUTOMATO

Sigma = {'a' , 'f', 's', 'd'}

QSet = {
  '1A', '2A', '3A', '4A', '5A',
  '1F', '2F', '3F', '4F', '5F',
}

FSet = {'1A'}

Delta = {
  # Transições 1A
  ('1A', 'a'): '1A',
  ('1A', 'f'): '1F',
  ('1A', 's'): '1A',
  ('1A', 'd'): '1A',
  # Transições 1F
  ('1F', 'a'): '1A',
  ('1F', 'f'): '1F',
  ('1F', 's'): '2F',
  ('1F', 'd'): '1F',
  # Transições 2A
  ('2A', 'a'): '2A',
  ('2A', 'f'): '2F',
  ('2A', 's'): '2A',
  ('2A', 'd'): '2A',
  # Transições 2F
  ('2F', 'a'): '2A',
  ('2F', 'f'): '2F',
  ('2F', 's'): '3F',
  ('2F', 'd'): '1F',
  # Transições 3A
  ('3A', 'a'): '3A',
  ('3A', 'f'): '3F',
  ('3A', 's'): '3A',
  ('3A', 'd'): '3A',
  # Transições 3F
  ('3F', 'a'): '3A',
  ('3F', 'f'): '3F',
  ('3F', 's'): '4F',
  ('3F', 'd'): '2F',
  # Transições 4A
  ('4A', 'a'): '4A',
  ('4A', 'f'): '4F',
  ('4A', 's'): '4A',
  ('4A', 'd'): '4A',
  # Transições 4F
  ('4F', 'a'): '4A',
  ('4F', 'f'): '4F',
  ('4F', 's'): '5F',
  ('4F', 'd'): '3F',
  # Transições 5A
  ('5A', 'a'): '5A',
  ('5A', 'f'): '5F',
  ('5A', 's'): '5A',
  ('5A', 'd'): '5A',
  # Transições 5F
  ('5F', 'a'): '5A',
  ('5F', 'f'): '5F',
  ('5F', 's'): '5F',
  ('5F', 'd'): '4F',
}

automato = AFD(QSet, Sigma, Delta, '1A', FSet)

# TESTES VALIDOS

AFD.testa(automato, "aaaaaaaaaa") #1
AFD.testa(automato, "fafafafafa") #2
AFD.testa(automato, "fssddffafa") #3
AFD.testa(automato, "fssssdddda") #4
AFD.testa(automato, "fsafsddfaa") #5
AFD.testa(automato, "fssasfddaa") #6
AFD.testa(automato, "affssddaaa") #7
AFD.testa(automato, "fsssffddda") #8
AFD.testa(automato, "ffssddsdfa") #9
AFD.testa(automato, "fsssfdddaa") #10

# TESTES INVALIDOS

AFD.testa(automato, "fsssssssss") #1
AFD.testa(automato, "fssasafsaf") #2
AFD.testa(automato, "fsssafafad") #3
AFD.testa(automato, "fsafasfasf") #4
AFD.testa(automato, "fasfasfasf") #5
AFD.testa(automato, "fsfsfsfsfs") #6
AFD.testa(automato, "fsafsafsaf") #7
AFD.testa(automato, "fffafsssss") #8
AFD.testa(automato, "aaaffsafas") #9
AFD.testa(automato, "ffsafasfas") #10