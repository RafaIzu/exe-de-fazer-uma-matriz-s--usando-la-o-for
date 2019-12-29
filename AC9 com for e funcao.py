def matriz(l,c,x):
    i=0
    n=0

    for n in range(c):
        for i in range (i+1,l+1):
            print()
            print(x,end='')
            n=0
            for n in range(1,c):
                print(x,end='')
linhas=int(input('Digite o numero de linhas:'))
colunas=int(input('Digite o numero de colunas:'))
caracter=input('Digite o caracter desejado')

matriz(linhas,colunas,caracter)
