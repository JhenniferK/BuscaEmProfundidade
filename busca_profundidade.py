def dfs(inicio, fim):
    pilha = [(inicio, (inicio))]
    visitado = set()
    nosVisitados = 0

    while pilha:
        atual, caminho = pilha.pop()
        nosVisitados += 1

        if atual == fim:
            print("Caminho percorrido:", caminho)
            print("Quantidade de nós visitados:", nosVisitados)
            print("Custo total:", len(caminho)-1)
            return
        
        visitado.add(atual)

        for proximo in [atual+1, atual*2]:
            if proximo not in visitado and proximo <= fim * 2:
                pilha.append((proximo, caminho + [proximo]))

    print("Caminho não encontrado.")

entradaInicio = int(input("Digite o número inicial: "))
entradaObjetivo = int(input("Digite o número do objetivo final: "))

dfs(entradaInicio, entradaObjetivo)