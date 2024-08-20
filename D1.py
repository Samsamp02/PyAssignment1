

#Q1: Temps du voyage
def tempsVoyage(distance, vitesse):
    temps = distance / vitesse
    temps = temps * 60
    print(temps)
    return temps

tempsVoyage(400,100)
tempsVoyage(20.6,60)


#Q2: Note finale avec poids
def noteFinale(note1, note2, note3, note4, note5):
    noteFinale = abs(note1*(10/100)) + abs(note2*(25/100)) + abs(note3*(5/100)) + abs(note4*(20/100)) + abs(note5*(40/100))
    print(noteFinale)
    return noteFinale

noteFinale(100,100,100,100,100)
noteFinale(50,90.5,60,80,70)


#Q3: bibliographie a partir de variables
def bibformat(auteur, titre, ville, maisonEdition, annee): 
    string = auteur + " (" + str(annee) + "). " +  titre + ". " + ville + ": " + maisonEdition
    print(string)
    return string

bibformat("Antoine de Saint Exupery", "Le petit prince", "Paris", "Jeunesse", 1943)


#Q4: bibliographie a partir de input
def bibformatPrint():
    auteur = input("SVP entrez l'auteur: ")
    titre = input("SVP entrez le titre: ")
    ville = input("SVP entrez la ville: ")
    maisonEdition = input("SVP entrez la maison d'edition: ")
    annee = input("SVP entrez l'annee de publication: ")

    string = auteur + " (" + str(annee) + "). " +  titre + ". " + ville + ": " + maisonEdition
    print(string)
    return

bibformatPrint()


#Q5: resoudre avec log
import math
def logFun(x):
    #L'équation à résoudre est 10^(4y)=x+3
    y = math.log((x+3),10)/4
    print(y)
    return y

logFun(7)
logFun(20)
logFun(999999997)
logFun(0.1)
logFun(9997)


#Q6: leap year checker
def anneeBis(an):
    #plus grand que 1582, divisible par 4 et 100 mais pas 400
    ver = an % 400 != 0
    ver = an > 1582
    ver = an%4 == 0
    return print(ver)
    
anneeBis(1904)
anneeBis(1928)
anneeBis(1950)
anneeBis(1990)
anneeBis(1932)
