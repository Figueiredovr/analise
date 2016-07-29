import sys
def separar(vet, begin, end):


    pivot   = vet[int((begin + end) / 2)]
    i       = begin
    j       = end

    while (i <= j):
        while (vet[i] < pivot):
            i += 1

        while (vet[j] > pivot):
            j -=  1

        if (i <= j):
            vet = troca(vet, i, j)
            i += 1
            j -= 1



    return i


def troca(vet, begin, end):
    aux = vet[begin]
    vet[begin] = vet[end]
    vet[end] = aux
    return vet


def quickSort(vet, begin, end):
    index=0

    if (len(vet) > 1):
        index = separar(vet, begin, end)

        if (begin < index - 1):
            quickSort(vet, begin, index - 1)

        if (index < end):
            quickSort(vet, index, end)

    return vet

sys.argv.pop(0)
vet = []
for i in sys.argv:
    vet.append(int(i))
vet = quickSort(vet,0,len(vet)-1)
print(vet)
