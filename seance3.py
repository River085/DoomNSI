# Séance 2 du 16/01/2024
# Dessin et déplacement 2d du joueur

# module pyglet principal (qu'on nenomme en pg pour plus de simplicité)
import pyglet as pg
# import des fonctions trigo du module math
from math import cos, sin

# création de la fenêtre pour le plan 2D
# résolution : 320x200 (comme le Doom de l'époque)
window2d = pg.window.Window(1920, 1080, "Plan 2D", vsync=False)

# variables globales 
x, y, a = 500, 500, 0 # position et angle du joueur
# "batch" du joueur
joueur = pg.graphics.Batch()
# dico qui contient les mouvements actifs (true) ou inactifs (false)
actions= {"tourner_gauche": False, "tourner_droite" : False, "avancer": False, "reculer": False}
# détection d'un touche pressée au clavier
@window2d.event
def on_key_press(symbol, modifiers):
  global x, y, a
  # Touche Q : on quitte le jeu  
  if symbol == pg.window.key.ESCAPE:
      pg.app.exit()
  # touches de déplacement
  if symbol == pg.window.key.S: # reculer
      # x -= 20*cos(a)
      # y -= 20*sin(a)
      actions["reculer"]= True
  if symbol == pg.window.key.Z: # avancer
      # x += 20*cos(a)
      # y += 20*sin(a)
      actions["avancer"]= True
  # touches pour pivoter
  if symbol == pg.window.key.Q:
      actions["tourner_gauche"]= True
      # a += 0.5	# rotation gauche
  if symbol == pg.window.key.D:
      actions["tourner_droite"]= True
      # a -= 0.5	# rotation droite
      actions["tourner_droite"]= True
# détection d'un touche relâchée au clavier
@window2d.event
def on_key_release(symbol, modifiers):
    if symbol == pg.window.key.S:
        actions["reculer"] = False
    if symbol == pg.window.key.Z:
        actions["avancer"] = False
    if symbol == pg.window.key.Q:
        actions["tourner_gauche"] = False
    if symbol == pg.window.key.D:
        actions["tourner_droite"] = False
# évènement principal : rendu graphique
@window2d.event
def on_draw():
    global x, y, a
    window2d.clear()
    # le joueur comme un cercle
    circle = pg.shapes.Circle(x, y, 15, color =(250, 216, 216), batch = joueur)
    # segment "vecteur vitesse" qui pointe vers la direction de visée
    visée = pg.shapes.Line(x, y, x + 20*cos(a), y + 20*sin(a), width=5, batch = joueur)
    # on dessine le "batch"
    joueur.draw()

def update(dt):
    global x, y, a
    if actions["avancer"]:
      x += 15*cos(a)
      y += 15*sin(a)
    if actions["reculer"]:
      x -= 15*cos(a)
      y -= 15*sin(a)
    if actions["tourner_gauche"]:
        a += 0.2	# rotation gauche
    if actions["tourner_droite"]:
        a -= 0.2	# rotation droite
        
pg.clock.schedule_interval(update, 1/30.0)
# lancement du jeu
pg.app.run()