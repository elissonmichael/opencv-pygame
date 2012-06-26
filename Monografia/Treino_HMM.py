from ghmm import *

sigma = IntegerRange(0,20)


passo_direita_1 = EmissionSequence(sigma,[1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4])
passo_direita_2 = EmissionSequence(sigma,[1, 1, 1, 2, 3, 3, 3, 3, 3, 8, 4, 4, 4, 4, 4, 4])
passo_direita_3 = EmissionSequence(sigma,[1, 1, 14, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 17, 1, 1])
passo_direita_4 = EmissionSequence(sigma,[1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4])
passo_direita_5 = EmissionSequence(sigma,[1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 8, 4, 4, 4, 4, 4, 4, 4])
passo_direita_6 = EmissionSequence(sigma,[1, 1, 1, 1, 2, 3, 3, 3, 3, 8, 8, 4, 4, 4, 4, 4, 4, 4])
passo_direita_7 = EmissionSequence(sigma,[1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 17])


passo_esquerda_1 = EmissionSequence(sigma,[5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8])
passo_esquerda_2 = EmissionSequence(sigma,[5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 5])
passo_esquerda_3 = EmissionSequence(sigma,[5, 5, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 17, 17, 5])
passo_esquerda_4 = EmissionSequence(sigma,[5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 17])
passo_esquerda_5 = EmissionSequence(sigma,[5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 13])
passo_esquerda_6 = EmissionSequence(sigma,[5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8])
passo_esquerda_7 = EmissionSequence(sigma,[5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 13])
passo_esquerda_8 = EmissionSequence(sigma,[5, 5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 4, 8, 8, 8, 8, 8, 8])


braco_direito_1 = EmissionSequence(sigma,[0, 17, 17, 17, 17, 9, 9, 9, 9, 9, 9, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12])
braco_direito_2 = EmissionSequence(sigma,[0, 17, 17, 9, 9, 9, 9, 10, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12])
braco_direito_3 = EmissionSequence(sigma,[0, 0, 0, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 9, 9, 9, 9, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12])
braco_direito_4 = EmissionSequence(sigma,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 17, 17, 17, 17, 9, 9, 9, 9, 9, 10, 10, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12])


braco_esquerdo_1 = EmissionSequence(sigma,[0, 0, 13, 13, 13, 14, 14, 14, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16])
braco_esquerdo_2 = EmissionSequence(sigma,[0, 13, 13, 14, 14, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16])
braco_esquerdo_3 = EmissionSequence(sigma,[0, 13, 13, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16])
braco_esquerdo_4 = EmissionSequence(sigma,[0, 0, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 16, 16, 16])


2_bracos_1 = EmissionSequence(sigma,[0, 0, 0, 0, 0, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20])
2_bracos_2 = EmissionSequence(sigma,[0, 0, 0, 0, 0, 17, 17, 17, 18, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20])
2_bracos_3 = EmissionSequence(sigma,[17, 17, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20])
2_bracos_4 = EmissionSequence(sigma,[17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 19])

