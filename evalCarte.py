from calendar import c
import random

class Carte:
    def __init__(self,name,coutMana,description):
        self.name=name
        self.coutMana=coutMana
        self.description=description
    
    def getName(self):
        return self.name
    
    def getCoutMana(self):
        return self.coutMana
    
    def getDescription(self):
        return self.description

    def effetCarte(self):
        pass

class Cristal(Carte):
    def __init__(self,name,coutMana,description,valeur):
        Carte.__init__(self,name,coutMana,description)
        self.valeur=valeur
        self.type="cristal"
    
    def getValeur(self):
        return self.valeur
    
    def getType(self):
        return self.type

    def effetCarte(self):
        joueurActuel.setManaActuel(joueurActuel.getManaActuel()+self.getValeur())
        print("Le Mana Max de", joueurActuel.getName(),"augmente de ",self.getValeur(),"points." )
        joueurActuel.getZoneDeJeu().remove(self)
        joueurActuel.getDefausse().append(self)


class Creature(Carte):
    def __init__(self,name,coutMana,description,attaque,vie):
        Carte.__init__(self,name,coutMana,description)
        self.attaque=attaque
        self.vie=vie
        self.type="creature"
    
    def getType(self):
        return self.type

    def getVie(self):
        return self.vie

    def getAttaque(self):
        return self.attaque

    def perdrePv(self,nb):
        self.vie=self.vie-nb
        if (self.vie<=0):
            print(self.getName(),"est mort et va dans la défausse.")
            joueurActuel.getZoneDeJeu().remove(self)
            joueurActuel.getDefausse().append(self)

    def Combat(self):
        print("Quelle cible? (0) Mage, (1) Une créature")
        cible=int(input())
        if(cible==0):
            cible=joueurNonActuel
        if (cible==1):
            affichageEnnemi=joueurNonActuel.getZoneDeJeu()
            for j in range(len(affichageEnnemi)):
                print("voulez-vous attaquer avec cette créature? Oui (0) Non (1)")
                print(affichageEnnemi[j].getName())
                print("Attaque:",affichageEnnemi[j].getAttaque())
                print("Pv:",affichageEnnemi[j].getVie())
                combat=int(input())
                if(combat==1):
                    cible=affichageEnnemi[j]


        if (cible.getType()=="mage"):
            cible.perdrePv(self.getAttaque())
        if (cible.getType()=="creature"):
            cible.perdrePv(self.getAttaque())
            self.perdrePv(cible.getAttaque())
        print(cible.getName(),"a perdu",self.getAttaque())

    def effetCarte(self):
        print(self.getName(),"est invoqué sur le terrain!")


class Blast(Carte):
    def __init__(self,name,coutMana,description,degat):
        Carte.__init__(self,name,coutMana,description)
        self.degat=degat
        self.type="blast"
    
    def getType(self):
        return self.type

    def getDegat(self):
        return self.degat

    def effetCarte(self):
        print("Quelle cible? (0) Mage, (1) Une créature")
        cible=int(input())
        if(cible==0):
            cible=joueurNonActuel
        if (cible==1):
            affichageEnnemi=joueurNonActuel.getZoneDeJeu()
            for j in range(len(affichageEnnemi)):
                print("voulez-vous attaquer avec cette créature? Oui (0) Non (1)")
                print(affichageEnnemi[j].getName())
                print("Attaque:",affichageEnnemi[j].getAttaque())
                print("Pv:",affichageEnnemi[j].getVie())
                combat=int(input())
                if(combat==1):
                    cible=affichageEnnemi[j]

        if (cible.getType()=="mage" or cible.getType()=="creature"):
            cible.perdrePv(self.getDegat())
        print(self.getName(),"inflige", self.getDegat(),"à",cible.getName(),".")
        joueurActuel.getZoneDeJeu().remove(self)
        joueurActuel.getDefausse().append(self)



    
class Mage:
    def __init__(self,name,pv,manaMax):
        self.name=name
        self.pv=pv
        self.manaMax=manaMax
        self.manaActuel=self.manaMax
        self.main=[]
        self.defausse=[]
        self.zoneDeJeu=[]
        self.type="mage"

    def getType(self):
        return self.type
    
    def getName(self):
        return self.name
    
    def getPv(self):
        return self.pv
    
    def getManaMax(self):
        return self.manaMax

    def getManaActuel(self):
        return self.manaActuel

    def getMain(self):
        return self.main
    
    def getDefausse(self):
        return self.defausse

    def getZoneDeJeu(self):
        return self.zoneDeJeu

    def getCarteMain(self,nb):
        return self.main[nb]

    
    def setManaActuel(self,nb):
        self.manaActuel=nb
    
    def perdrePv(self,nb):
        self.pv=self.pv-nb
        if (self.pv<=0):
            defaite==True
            print(joueurActuel.getName(),"à perdu!")
    
    def setManaMax(self,nb):
        self.manaMax=nb

    def jouerCarte(self,carteJouer):
        print(joueurActuel.getName(),"a utilisé",carteJouer.getName())
        self.manaActuel=self.manaActuel-carteJouer.getCoutMana()
        self.zoneDeJeu.append(carteJouer)
        self.main.remove(carteJouer)
        carteJouer.effetCarte()
        rejouer=False

    def piocherCarte(self,cartePiocher):
        self.main.append(cartePiocher)


j1=Mage("Géraldine",15,10)
j2=Mage("Bernard",25,5)


carte1=Blast("Boule de feu", 3, "envoi une belle boule de feu dans la tronche de votre adversaire.",5)
carte2=Blast("Douce brise", 1, "invoque une petite brise rafraichissante.",1)
carte3=Blast("Apocalypse", 20, "déclanche la fin du monde.",20)
carte4=Carte("Abandon", 0, "vous hissez le drapeau blanc, fin de la partie.")

carteCristal1=Cristal("Cristal brillant", 0, "Un cristal brillant d'une lumière aveuglante",2)

carteCreature1=Creature("Cristal ambulant", 0, "Un cristal brillant d'une lumière aveuglante",2,5)

pioche=[carte1,carte2,carte3,carte4]

joueurActuel=j1
joueurNonActuel=j2
defaite=False

while(defaite==False):
    tour=True

    print("Au tour de ",joueurActuel.getName()," de jouer!")
    print("Pv:",joueurActuel.getPv())
    print("Mana Max:",joueurActuel.getManaMax())
    print("Mana disponible:",joueurActuel.getManaActuel())

    print(joueurActuel.getName()," va piocher une carte!")
    cartePioche= pioche[random.randint(0,3)]
    joueurActuel.piocherCarte(cartePioche)
    joueurActuel.piocherCarte(carteCristal1)
    joueurActuel.piocherCarte(carte1)
    joueurActuel.piocherCarte(carteCreature1)   


    while(tour==True):
        print("Au tour de ",joueurActuel.getName()," de jouer!")
        print("Pv:",joueurActuel.getPv())
        print("Mana Max:",joueurActuel.getManaMax())
        print("Mana disponible:",joueurActuel.getManaActuel())

        rejouer=True
        while (rejouer==True):
            print("Que voulez-vous faire? Utiliser une carte (1) ? attaquer avec vos créature (2) ou terminer le tour (0) ?")
            actionTour=int(input())
            if(actionTour==1):
                print("quelle carte voulez vous jouer?")
                carteJouer=int(input())
                print(joueurActuel.getCarteMain(carteJouer).getName())
                if(carteJouer>=0 and carteJouer<len(joueurActuel.getMain())):
                    if (joueurActuel.getCarteMain(carteJouer).getCoutMana()<=joueurActuel.getManaActuel()):
                        joueurActuel.jouerCarte(joueurActuel.getCarteMain(carteJouer))
                    else:
                        print("Vous n'avez pas assez de mana.")
                else:
                    print("Vous n'avez pas rentre un nombre correct.")
            if(actionTour==2):
                affichage=joueurActuel.getZoneDeJeu()
                for j in range(len(affichage)):
                    print("voulez-vous attaquer avec cette créature? Oui (0) Non (1)")
                    print(affichage[j].getName())
                    print("Attaque:",affichage[j].getAttaque())
                    print("Pv:",affichage[j].getVie())
                    combat=int(input())
                    if (combat==0):
                        affichage[j].Combat()
                    

            if(actionTour==0):
                tour=False
                rejouer=False

    print("fin du tour de ",joueurActuel.getName())
    joueurActuel.setManaActuel(joueurActuel.getManaMax())

    if(joueurActuel.getName()=="Géraldine"):
        joueurActuel=j2
        joueurNonActuel=j1
    else:
        joueurActuel=j1
        joueurNonActuel=j2






