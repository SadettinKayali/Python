def topla(liste:list):
    toplam=0
    for i in liste:
        toplam+=i
    return toplam


import deneme # dosya adı fonksiyonla aynı olucak. dosya adını çağırıp içinden tek bir fonksiyona çekilebilir.
print(deneme.topla([10,50,60,90]))