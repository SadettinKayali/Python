import random

class Düşman():
    def __init__(self):
        self.sagmi=True
        self.saglik=random.randint(50,100)
        self.kalkan=random.randint(10,25)
        self.güç=random.randint(30,100)
        
    def vur(self,player):
        damage=self.güç-player.kalkan
        player.saglik-=damage
        if player.saglik<=0:
            player.sagmi=False
        

class Player():
    def __init__(self):
        self.sagmi=True
        self.saglik=500
        self.kalkan=30
        self.güç=75
        
    
    def vur(self,düşman):
        damage=self.güç-düşman.kalkan
        düşman.saglik-=damage
        
        if düşman.saglik<=0:
            düşman.sagmi=False
            düşmanlar.remove(düşman)

düşmanlar=list()
for i in range(10):
    düşmanlar.append(Düşman()) # parantezleri koymak zorundayız.
player=Player()
while True:
    print("Player : =>> Sağlık : {} ---- Güç : {} ---- Kalkan : {}".format(player.saglik,player.güç,player.kalkan))
    if player.sagmi==False:
        print("GAME OVER BİTCHES !! :( :(")
        quit()
        
    if not düşmanlar:
        print("Hepsini pompaladık. :) :)")
        quit()
        
    for i in düşmanlar:
        print("{}. Düşman =>> Sağlık: {} ---- Güç:{} : ---- Kalkan: {}".format(düşmanlar.index(i),i.saglik,i.güç,i.kalkan))
    #break
    secim=int(input("Düşman Seçin : "))
    düşman=düşmanlar[secim]
    player.vur(düşman)
    if düşmanlar:
        saldıran=düşmanlar[random.randint(0,len(düşmanlar)-1)]
        saldıran.vur(player)