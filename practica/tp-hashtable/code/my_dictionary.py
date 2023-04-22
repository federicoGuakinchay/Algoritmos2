import random 

class dictionary_node():
    key     = None
    value   = None
    alfanumeric_key = None 

class L_ab_node():
    a = None 
    b = None 
    
'''hash table universal funtión'''  
def create_hashtable(long=None,Nro_funtions=None): 
    if long == None:
        long = input('ingresar la longitud de la hash-table ')
    if Nro_funtions == None:
        Nro_funtions = input('ingresar la cantidad de fuciones ')
    d =[]
    for i in range (0,long):
       d.append([])
    L_ab        = []
    for j in range (0,Nro_funtions):
        new_node    = L_ab_node()
        new_node.a  = random.randint(1,101) # cambiar si la tabla de hash sera mas grande 
        new_node.b  = random.randint(0,101) # cambiar si la tabla de hash sera mas grande 
        L_ab.append(new_node) 
    return(d,L_ab)


def hash_insert(D,L_ab,key,value):
    long= len(L_ab)
    index = random.randint(0,long-1)
    a   = L_ab[index].a
    b   = L_ab[index].b 
    i = ((a*key+b) % 28) % 29     # modificar dependiendo de la tabla de hash que utilise 
    #   (a*k+b)mod p mod m  ///siendo p un primo mayor a m  /// y m la longitud de la tabla 
    if D[i] == None:
        D[i]= []
    insert          = dictionary_node()
    insert.key      = key
    insert.value    = value
    D[i].append (insert)   
    return(D)


def hash_search(D,L_ab,key,element=False):
    resultado = False
    for i in range (0,len(L_ab)):
        a=L_ab[i].a
        b=L_ab[i].b
        i = ((a*key+b) % 28 ) % 29 
        if D[i] != None:
            resultado =  search(D[i],key,element)
            if resultado != False and element == False:
                return resultado
            elif resultado != False and element == True:
                return resultado,D[i]
            elif resultado == False and element == True:
                return False, None
    return(resultado)

def search(L,key,element):
    long= len (L)
    if long == 0 : 
        return False
    else:
        long = long-1
    for i in (0,long) :
        if L[i] != []:
            if L[i].key == key:
                if element == False:
                    return L[i].value
                else :
                    return L[i]
    return False

def hash_delete(D, L_ab, key):
    element,L=hash_search(D,L_ab,key,True)
    L.remove(element)
    if element == False:
        return False
    else:
        return True

def print_hahs_table(D):
    long = len(D)
    print('_______________Hash_table_______________')
    print('Nro     key          value')
    for i in range(0,long):
        print('________________________________________')
        print(f'{i}_' ,end='')
        if D[i] != [] and D[i] != None: 
            long_2 = len (D[i])
            if long_2 == 1: 
                print(f'      {D[i][0].key}          {D[i][0].value}')
            else: 
                print_L(D[i],long_2)
        else:
            print(f'      {None}          {None}')
        
def print_L(L, long):
    for i in range (0,long):
        print(f'      {L[i].key}          {L[i].value}',end='  //  ')
        
    print('')
    
    
    
def hash_insert_codigopostal(D,L_ab,key,alfanumeric_key,value):
    long= len(L_ab)
    index = random.randint(0,long-1)
    a   = L_ab[index].a
    b   = L_ab[index].b 
    i = ((a*key+b) % 28) % 29     # modificar dependiendo de la tabla de hash que utilise 
    #   (a*k+b)mod p mod m  ///siendo p un primo mayor a m  /// y m la longitud de la tabla 
    if D[i] == None:
        D[i]= []
    insert          = dictionary_node()
    insert.key      = key
    insert.value    = value
    insert.alfanumeric_key = alfanumeric_key
    D[i].append (insert)   
    return(D)


    
def hash_search_codigopostal(D,L_ab,key,alfanumeric_key,element=False):
    resultado = False
    for i in range (0,len(L_ab)):
        a=L_ab[i].a
        b=L_ab[i].b
        i = ((a*key+b) % 28 ) % 29 
        if D[i] != None:
            resultado =  search_codigopostal(D[i],key,alfanumeric_key,element)
            if resultado != False and element == False:
                return resultado
            elif resultado != False and element == True:
                return resultado,D[i]
            elif resultado == False and element == True:
                return False, None
    return(resultado)

def search_codigopostal(L,key,alfanumeric_key,element):
    long= len (L)
    if long == 0 : 
        return False
    else:
        long = long-1
    for i in (0,long) :
        if L[i] != []:
            if L[i].key == key and L[i].alfanumeric_key == alfanumeric_key:
                if element == False:
                    return L[i].value
                else :
                    return L[i]
    return False
