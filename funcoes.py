import random

def takeSecond(elem):
    return elem[1]

def initialize_population(word, quantity=10, alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !,.'):
    individuos = []
    palavra = ''
    for j in range (0,10):
        for i in range(0,len(word)):
            palavra = palavra + str(random.choices(alfabeto)[0])
        individuos.append(palavra)
        palavra = ''
    
    return individuos

def calculate_fitness_individuo(individuo, word):
    valor = 0
    for letra in range(0,len(individuo)):
            if individuo[letra]==word[letra]:
                valor = valor +1
    return valor

def calculate_fitness_population(population, word):
    fitness = []
    valor = 0
    for individuo in population:
        valor = calculate_fitness_individuo(individuo,word)
        fitness.append(valor)
        valor = 0
    return fitness
    
def mutate(novo_individuo1, novo_individuo2, alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !,.'):
    mutate1 = random.randint(0,len(novo_individuo1)-1)
    mutate2 = random.randint(0,len(novo_individuo2)-1)
    
    mutate_c1 = str(random.choices(alfabeto)[0])
    mutate_c2 = str(random.choices(alfabeto)[0])    
    
    novo_individuo1 = novo_individuo1[:mutate1] + mutate_c1 + novo_individuo1[mutate1+1:len(novo_individuo1)]
    novo_individuo2 = novo_individuo2[:mutate2] + mutate_c2 + novo_individuo2[mutate2+1:len(novo_individuo2)]
    
    return novo_individuo1, novo_individuo2

def getBest(individuos,fitness):
    populacao = zip(individuos,fitness)
    populacao = sorted(populacao, key = takeSecond, reverse= True)
    populacao_aux = []
    for individuo in populacao:
        individuo = list(individuo)
        populacao_aux.append(individuo)
    populacao = populacao_aux
    return populacao

def crossingOver(populacao, individuos, word, alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !,.'):
    aux = populacao[0][0]
    aux_ini = aux[0:int(len(aux)/2)]
    aux_fim = aux[int(len(aux)/2):len(aux)]
    
    auxi = populacao[1][0]
    auxi_ini = auxi[0:int(len(auxi)/2)]
    auxi_fim = auxi[int(len(auxi)/2):len(auxi)]
    
    novo_individuo1 = aux_ini + auxi_fim
    novo_individuo2 = auxi_ini + aux_fim
    
    novo_individuo1, novo_individuo2 = mutate(novo_individuo1, novo_individuo2, alfabeto)
    
    
    fitness1 = calculate_fitness_individuo(novo_individuo1, word)
    fitness2 = calculate_fitness_individuo(novo_individuo2, word)
    
    if fitness1 >= populacao[len(individuos)-1][1]:
        populacao[len(individuos)-1][1] = fitness1
        populacao[len(individuos)-1][0] = novo_individuo1
        
    if fitness2 >= populacao[len(individuos)-2][1]:
        populacao[len(individuos)-2][1] = fitness2
        populacao[len(individuos)-2][0] = novo_individuo2
    individuo_aux = []
    for individuo in range (0,len(populacao)):
        individuo_aux.append(populacao[individuo][0])
    individuos = individuo_aux
    return individuos