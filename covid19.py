
archives = ["AY274119.txt" ,"AY278488.2.txt","MN908947.txt","MN988668.txt","MN988669.txt"]

for i in range(5):
    comparator = archives[i]
    #Leyendo archivo
    f = open(comparator, 'r')
    list_gen1 = f.readlines() #Lista de cadenas del gen comparador
    for j in range(5):
        iguales = 0
        total = 0
        #Leyendo archivo al comparar
        compared = archives[j]
        f_ = open(compared, 'r') #Lista de cadenas 
        list_gen2= f_.readlines() #Lista de cadenas del gen comparado
        for f in range(len(list_gen1)): #Itera entre cadenas
            for g in range(len(list_gen1[f])): #Itera en la cadena
                if list_gen1[f][g] == list_gen2[f][g] and list_gen2[f][g] != '\n' and list_gen2[f][g] != 'n':
                    iguales += 1
                if list_gen2[f][g] != '\n' and list_gen2[f][g] != 'n':
                    total += 1
        percentage = round((iguales/total)*100,2)
        print("El porcentaje de igualdad de ",comparator," con ", compared, " es: ", str(percentage))
    print()
            




