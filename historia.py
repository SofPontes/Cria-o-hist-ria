import random

#função que gera a introdução da história
def gerar_introducao():
    introducoes = ["Em uma noite escura", "No porão assustador", "Atrás daquele enorme portão sombrio"]
    return random.choice(introducoes)

#função que gera o desenvolvimento da historia
def gerar_desenvolvimento():
    desenvolvimentos = ["podia ouvir assustadores gritos", "o silêncio se tornava preocupante", "avistava sombras movendo-se rapidamente"]
    return random.choice(desenvolvimentos)

#função que gera o final da história
def gerar_final():
    finais = ["e involuntariamente algo me puxava em sua direção.", "e infelizmente eu acabei parando lá.", "e algo chamava meu nome naquela direção."]
    return random.choice(finais)

#função principal que gera a história
def gerar_historia():
    introducao =  gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao} {desenvolvimento} {final}"
    return historia

#exibe a história criada
if __name__ =="__main__":
        print(gerar_historia())





