def is_prime (x):
    '''
    verificam daca un numar este prim
    :param x:int
    :return:True daca este prim, False in caz contrar
    '''
    if x<2:
      return False
    if x==2:
      return True
    for i in range(2,x):
      if x%i==0:
       return False
    return True

def get_largest_prime_below(n):
    '''
    Gaseste ultimul numar prim mai mic decat un numar dat
    Input:
    -n:numar dat
    Output:
    -x,ultimul numar prim mai mic decat n
    '''
    for i in range(n-1,2,-1):
        if is_prime(i):
            return i
    return 0

def test_get_largest_prime_below():
    assert get_largest_prime_below(5)==3
    assert get_largest_prime_below(7)==5
    assert get_largest_prime_below(53)==47
    assert get_largest_prime_below(31)==29

def get_n_choose_k(n,k):
    '''
    Calculeaza combinari de n luate cate k
    :param n: int
    :param k: int
    :return: x//y, combinari de n luate cate k
    '''
    x=1
    for i in range(n-k+1,n+1):
       x=x*i
    y=1
    for i in range(2,k+1):
          y=y*i
    return x//y

def test_get_n_choose_k():
    assert test_get_n_choose_k(5,3)==10
    assert test_get_n_choose_k(8,2)==28
    assert test_get_n_choose_k(12,8)==495
    assert test_get_n_choose_k(14,9)==2002

def is_palindrome(n):
    '''
    Determinati daca un numar dat este palindrom
    :param n: int
    :return: True daca este palindrom, False in caz contrar
    '''
    copie=n
    ogl=0
    while copie!=0:
        ogl=ogl*10+copie%10
        copie=copie//10
    if ogl==n:
        return True
    return False

def test_is_palindrome():
    assert test_is_palindrome(565)==True
    assert test_is_palindrome(1)==True
    assert test_is_palindrome(253)==False
    assert test_is_palindrome(545)==True

if __name__=="__main__":
    while True:
        print('1.Ultimul numar prim mai mic decat un numar dat')
        print('2.Combinari de n luate cate k')
        print('3.Determina daca un numar dat este palindrom')
        print('x.Exit')
        optiune=input('Alegeti o optiune: ')
        if optiune == '1':
            nr= int(input('Dati numar: '))
            prim=get_largest_prime_below(nr)
            print(f'ultimul numar prim mai mic decat {nr} este {prim}')
        elif optiune=='2':
             nrn=int(input('Dati primul numar: '))
             nrk=int(input('dati al doilea numar: '))
             comb= get_n_choose_k(nrn,nrk)
             print(f'Combinari de {nrn} luate cate {nrk} este {comb}')
        elif optiune=='3':
            nr1=int(input('Dati un numar: '))
            print(is_palindrome(nr1))








