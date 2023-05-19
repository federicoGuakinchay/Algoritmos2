def ej4 (L):                
    long		= len(L)        
    if long <= 1 :          
        return (L)          
    cont= 1                 
    list.sort(L)            # ordeno la lista 
    print(L)                
    if long % 2 == 0:       # aqui obtengo el nodo del medio  
        a  =  long//2       
    else:                   
        a	 =  long//2 + 1     
    print(a)                 
    if a % 2 == 0:           # aqui obtengo la mitad de la cantidad de Nros menores de la lista
        b = a//2            
    else:                   
        b = a//2 +1         
    for i in range (b):     # cambio los elemetos de la lista  
        G  = L[i-1]         
        L[i-1] = L[a+i]     
        L[a+i] = G          
    return(L)               

L = [7,3,2,8,5,4,1,6,10,9]
L=ej4(L)
print(L)
