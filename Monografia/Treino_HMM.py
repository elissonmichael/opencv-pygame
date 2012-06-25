from ghmm import *

sigma = IntegerRange(0,20)



passo_direita_1 = EmissionSequence(sigma,[1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4])
passo_direita_2 = EmissionSequence(sigma,[1, 1, 1, 2, 3, 3, 3, 3, 3, 8, 4, 4, 4, 4, 4, 4])
passo_direita_3 = EmissionSequence(sigma,[1, 1, 14, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 17, 1, 1])
passo_direita_4 = EmissionSequence(sigma,[1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4])
passo_direita_5 = EmissionSequence(sigma,[1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 8, 4, 4, 4, 4, 4, 4, 4])
passo_direita_6 = EmissionSequence(sigma,[1, 1, 1, 1, 2, 3, 3, 3, 3, 8, 8, 4, 4, 4, 4, 4, 4, 4])
passo_direita_7 = EmissionSequence(sigma,[1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 17])

