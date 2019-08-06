"""
Feito por Matheus Farias em 06/08/2019 às 01:45
Algoritmo Genético que reconhece a frase dada
"""

import time
from funcoes import initialize_population, calculate_fitness_population, getBest, crossingOver


word = input ('Digite a frase que gostaria de testar no algorítmo: ')
tic = time.time()
alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !,.'
individuos = initialize_population(word, 10, alfabeto)
fitness = calculate_fitness_population(individuos, word)
geracao = 0

while max(fitness)!=len(word):
    fitness = calculate_fitness_population(individuos, word)
    populacao = getBest(individuos,fitness)
    if geracao == 0:
        melhorini = populacao[0][0]
        
    melhorfim = populacao[0][0]
    print('O melhor indivíduo da geração {}: "{}"'.format(geracao, populacao[0][0]))
    individuos = crossingOver(populacao,individuos, word, alfabeto)
    geracao = geracao + 1
    
toc = time.time()
tempo = toc-tic
print('\nO tempo que durou o processo de convergência: {:.2f} segundos'.format(tempo))
print('O melhor individuo inicial: "{}"'.format(melhorini))
        
