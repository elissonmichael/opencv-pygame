from ghmm import *

sigma = IntegerRange(0,21)


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
braco_direito_3 = EmissionSequence(sigma,[0, 0, 0, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,17, 9, 9, 9, 9, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12])
braco_direito_4 = EmissionSequence(sigma,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 17, 17, 17, 17, 9, 9, 9, 9, 9, 10, 10, 11, 11,11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12])


braco_esquerdo_1 = EmissionSequence(sigma,[0, 0, 13, 13, 13, 14, 14, 14, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16])
braco_esquerdo_2 = EmissionSequence(sigma,[0, 13, 13, 14, 14, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16])
braco_esquerdo_3 = EmissionSequence(sigma,[0, 13, 13, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16])
braco_esquerdo_4 = EmissionSequence(sigma,[0, 0, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 16, 16, 16])


ambos_bracos_1 = EmissionSequence(sigma,[0, 0, 0, 0, 0, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20])
ambos_bracos_2 = EmissionSequence(sigma,[0, 0, 0, 0, 0, 17, 17, 17, 18, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20])
ambos_bracos_3 = EmissionSequence(sigma,[17, 17, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20])
ambos_bracos_4 = EmissionSequence(sigma,[17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 19])


pi = [1.0, 0.0, 0.0, 0.0]
A = [[0.75, 0.25, 0.0, 0.0],[0.0, 0.75, 0.25, 0.0],[0.0, 0.0, 0.75, 0.25],[0.0, 0.0, 0.0, 1.0]]
estado_1 = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
estado_2 = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
estado_3 = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
estado_4 = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
B = [estado_1,estado_2,estado_3,estado_4]

HMM_passo_para_direita = HMMFromMatrices (sigma, DiscreteDistribution(sigma), A, B, pi)
HMM_passo_para_esquerda = HMMFromMatrices (sigma, DiscreteDistribution(sigma), A, B, pi)
HMM_levantar_braco_direito = HMMFromMatrices (sigma, DiscreteDistribution(sigma), A, B, pi)
HMM_levantar_braco_esquerdo = HMMFromMatrices (sigma, DiscreteDistribution(sigma), A, B, pi)
HMM_levantar_ambos_os_bracos = HMMFromMatrices (sigma, DiscreteDistribution(sigma), A, B, pi)

HMM_passo_para_direita.baumWelch(passo_direita_1)
HMM_passo_para_esquerda.baumWelch(passo_esquerda_1)
HMM_levantar_braco_direito.baumWelch(braco_direito_1)
HMM_levantar_braco_esquerdo.baumWelch(braco_esquerdo_1)
HMM_levantar_ambos_os_bracos.baumWelch(ambos_bracos_1)
