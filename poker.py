# Créé par nantou, le 30/11/2021 en Python 3.7
#import
import random
from random import randint
import pygame
from pygame import *

#fonctions
cartes = [["1trefle", "1pic", "1coeur", "1careaux"], ["2trefle", "2pic", "2coeur", "2carreaux"], ["3trefle", "3pic", "3coeur", "3carreaux"], ["4trefle", "4pic", "4coeur", "4carreaux"], ["4trefle", "4pic", "4coeur", "4carreaux"], ["5trefle", "5pic", "5coeur", "5carreaux"], ["6trefle", "6pic", "6coeur", "6carreaux"], ["7trefle", "7pic", "7coeur", "7carreaux"], ["8trefle", "8pic", "8coeur", "8carreaux"], ["9trefle", "9pic", "9coeur", "9carreaux"], ["10trefle", "10pic", "10coeur", "10carreaux"], ["Vtrefle", "Vpic", "Vcoeur", "Vcarreaux"], ["Qtrefle", "Qpic", "Qcoeur", "Qcarreaux"], ["Rtrefle", "Rpic", "Rcoeur", "Rcarreaux"]]

cartesPasDispo = []

class Game():
    plateau = []
    def __init__(self):
        self.mise = {"mise": 20}

class Poker():
    """Class pour le Poker"""
    def __init__(self, nom, solde = 500):
        self.nom = nom
        self.solde = solde
        self.main = []

    def distribution(self):
        if len(self.main) == 2:
            print(self.main)
            return
        nb = randint(0, 13)
        sy = randint(0, 3)
        if cartes[nb][sy] not in cartesPasDispo:
            cartesPasDispo.append(cartes[nb][sy])
            self.main.append(cartes[nb][sy])
            self.distribution()
        else:
            self.distribution()



def jouer(joueur, game):
    print("la mise actuelle est de:", game.mise["mise"])
    manche = int(input("Que voulez vous faire ? \n [1] Vous couchez \n [2] Suivre avec une mise de 200 \n [3] Relancer \n"))
    if manche == 1:
        print("Vous vous êtes couchez")
    elif manche == 2:
        joueur.solde -= 200
        print("Vous avez suivis, votre solde est actuellement de", joueur.solde)
    elif manche == 3:
        montant = int(input("De combien voulez-vous relancez: "))
        joueur.solde -= montant
        print("Vous avez relancez avec", montant, "\nvotre solde est actuellement de", joueur.solde)

#Pygame
###Fennetre
##pygame.init()
##screen = pygame.display.set_mode((600, 480))
##pygame.display.set_caption('Basic Pygame program')
##
### Fill background
##background = pygame.Surface(screen.get_size())
##background = background.convert()
##background.fill((250, 250, 250))
##
###Variables
##font = pygame.font.Font(None, 36)
##text = font.render("Hello There", 1, (10, 10, 10))
##textpos = text.get_rect()
##textpos.centerx = background.get_rect().centerx
##background.blit(text, textpos)
##screen.blit(background, (0, 0))
##pygame.display.flip()
##
### Events
##continuer = 1
##while continuer:
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            continuer = 0
##    screen.blit(background, (0, 0))
##    pygame.display.flip()