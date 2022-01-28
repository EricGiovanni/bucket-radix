def lsd(arreglo, posicion_actual):
    if(posicion_actual < -4):
        return
    print("=========================================================================")
    print("Arreglo original", arreglo)
    print("=========================================================================")
    matriz = [["0", "1", "2", "3", "4", "5", "6", "7",
               "8", "9", "A", "B", "C", "D", "E", "F"],
              [[], [], [], [], [], [], [], [], [], [],
               [], [], [], [], [], []]]

    for i in range(len(arreglo)):
        pos = int(arreglo[i][posicion_actual], 16)
        matriz[1][pos].append(arreglo[i])
    print(matriz[0])
    rec = []
    for i in range(len(matriz[1])):
        print(matriz[1][i])
        for j in matriz[1][i]:
            rec.append(j)

    lsd(rec, posicion_actual - 1)


if __name__ == "__main__":
    lsd(["E41E", "A317", "0250", "CD17", "2273", "567B",
         "ABCD", "8C55", "D139", "6D9F", "205C", "A925",
         "C14E", "31A0", "BF92", "7722", "9C88", "D4CA",
         "48DE", "B14C", "2E50", "EB46", "4168", "35A1",
         "668B", "FA38", "70F0", "74E4", "9526", "EF4A",
         "0E65", "BAF3", "F154", "05BE", "5469", "C2FB"], -1)
