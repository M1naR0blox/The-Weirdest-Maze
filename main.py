import random
import pygame
import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
"""


before compiling, the pgzero engine breaks
and the game cannot load any new
image, so use the terminal to see which level are
you on


"""
joystick = pygame.joystick.Joystick(0)
joystick.init()

correctbeep = tone.create('A3', 0.5)
level = 1
WIDTH = 800
HEIGHT = 800
TITLE = f"Weird Maze, check terminal"
player = "character"
left = True
right = False
mode = "menu"
class Player:
    def func(pla):
        if keyboard.A or keyboard.left or joystick.get_button(1):
            pla.image = "cgarc"
            pla.x -= 10
            left = True
        elif keyboard.D or keyboard.right or joystick.get_button(2):
            pla.image = "character"
            pla.x += 10
            left = False
        if keyboard.W or keyboard.up or joystick.get_button(3):
            pla.y -= 10
        elif keyboard.S or keyboard.down or joystick.get_button(0):
            pla.y += 10

        elif joystick.get_button(6):
            mode = "menu"

random_num = random.randint(0, 1)

player = Actor("character", (WIDTH / 2, HEIGHT / 2))
menu_button = Actor("start", (WIDTH / 2, HEIGHT / 2))
puerta_buena = Actor("puertabuena", (40, 400))
puerta_mala = Actor("puertabuena", (760, 400))
puerta_mala1 = Actor("puertabuena", (400, 750))
puerta_mala2 = Actor("puertabuena", (760, 400))
final = Actor("truend", (400, 400))

def draw():
    global mode
    final.draw()
    if mode == "game":
        global random_num
        puerta_mala.draw()
        puerta_buena.draw()
        if level >= 3 and not level == 7:
            puerta_mala1.draw()
            puerta_mala2.draw()
        elif level == 8:
            screen.draw.text("The End of the game is here", (WIDTH / 2, HEIGHT))
        player.draw()
    elif mode == "menu":
        menu_button.draw()
    elif mode == "theend":
        menu_button.draw()
        print("YOU WON!")

def update(dt):
    global mode
    if mode == "game":
        global level
        if level == 1:
            if puerta_buena.colliderect(player):
                level += 1
                player.pos = WIDTH / 2, HEIGHT / 2
                correctbeep.play()
            if puerta_mala.colliderect(player) or puerta_mala1.colliderect(player) or puerta_mala2.colliderect(player):
                player.pos = 400, 400
            screen.clear()
            Player.func(player)
            print(level)
        elif level == 2:
            puerta_mala.pos = 40, 400
            puerta_buena.pos = 760, 400
            if puerta_buena.colliderect(player):
                level += 1
                player.pos = 400, 400
                correctbeep.play()
            screen.clear()
            Player.func(player)
            print(level)
        elif level == 3:
            puerta_mala.pos = 40, 400
            puerta_buena.pos = 400, 70
            if puerta_mala.colliderect(player) or puerta_mala1.colliderect(player) or puerta_mala2.colliderect(player):
                player.pos = 400, 400
            if puerta_buena.colliderect(player):
                level += 1
                player.pos = WIDTH / 2, HEIGHT / 2
                correctbeep.play()
            screen.clear()
            Player.func(player)
            print(level)
        elif level == 4:
            puerta_mala.pos = 760, 400
            puerta_buena.pos = 40, 400
            puerta_mala1.pos = 400, 50
            puerta_mala2.pos = 400, 750
            if puerta_mala.colliderect(player) or puerta_mala1.colliderect(player) or puerta_mala2.colliderect(player):
                player.pos = 400, 400
            if puerta_buena.colliderect(player):
                level += 1
                player.pos = WIDTH / 2, HEIGHT / 2
            screen.clear()
            Player.func(player)
            print(level)
        elif level == 5:
            puerta_mala.pos = 40, 400
            puerta_buena.pos = 400, 750
            puerta_mala1.pos = 400, 50
            puerta_mala2.pos = 760, 400
            if puerta_mala.colliderect(player) or puerta_mala1.colliderect(player) or puerta_mala2.colliderect(player):
                player.pos = 400, 400
            if puerta_buena.colliderect(player):
                level += 1
                player.pos = WIDTH / 2, HEIGHT / 2
                correctbeep.play()
            screen.clear()
            Player.func(player)
            print(level)
        elif level == 6:
            puerta_mala.pos = 40, 400
            puerta_buena.pos = 760, 400
            puerta_mala1.pos = 400, 50
            puerta_mala2.pos = 400, 750
            if puerta_mala.colliderect(player) or puerta_mala1.colliderect(player) or puerta_mala2.colliderect(player):
                print("WRONG DOOR")
                mode = "menu"
            if puerta_buena.colliderect(player):
                level += 1
                player.pos = WIDTH / 2, HEIGHT / 2
                correctbeep.play()
            screen.clear()
            Player.func(player)
            print(level)
        elif level == 7:
            puerta_mala.pos = 40, 400
            puerta_buena.pos = 760, 400
            puerta_mala1.pos = 400, 50
            puerta_mala2.pos = 400, 750
            if puerta_mala.colliderect(player) or puerta_mala1.colliderect(player) or puerta_mala2.colliderect(player):
                exit()
            if puerta_buena.colliderect(player):
                level += 1
                player.pos = WIDTH / 2, HEIGHT / 2
                correctbeep.play()
            screen.clear()
            Player.func(player)
            print(level)
        elif level == 8:
            puerta_mala.pos = 2000, 2000
            puerta_buena.pos = 2000, 2000
            puerta_mala1.pos = 2000, 2000
            puerta_mala2.pos = 2000, 2000
            screen.clear()
            Player.func(player)
            print("The End")

def on_key_down(key):
    if keyboard[keys.SPACE]  or keyboard[keys.SPACE] or joystick.get_button(4) and level == 7:
        screen.clear()
        print("Goodbye")
        print("BTW, this was made in a day lol")
        print("bc all my ideas werent wonna work")
        print("""on an engine like pgzero
        of course it would have worked on a
        engine like pygame or anything else
        but anyways, this is my game.
        YES, THIS WAS MY DUMBEST IDEA
        but hey, it works.
        and it has good controls""")
        import time
        time.sleep(10)
        exit()


def on_mouse_down(button):
    global mode
    if button == mouse.LEFT or joystick.get_button(1):
        mode = "game"

pgzrun.go()