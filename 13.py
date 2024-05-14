def subconjunto_soma(nums, alvo):
    def auxiliar(indice, soma_atual):
        if soma_atual == alvo:
            return True
        if indice == len(nums) or soma_atual > alvo:
            return False
       
        return auxiliar(indice + 1, soma_atual + nums[indice]) or auxiliar(indice + 1, soma_atual)

    return auxiliar(0, 0)

nums = [5, 12, 1, 3, 2]
alvo = 16
print(subconjunto_soma(nums, alvo))  