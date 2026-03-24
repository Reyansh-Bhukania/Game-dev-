import pgzrun 
import random

HEIGHT = 500
WIDTH = 600

basket = Actor("basket", (300, 400))

bomblist = []
fruitlist = []

fruits = ["apple", "dragonfruit", "strawberry", "banana"]
gameover=False
score = 0

def draw():
    if gameover==True:
        screen.blit("gameover" , (0,0))
        return
    screen.blit("background", (0, 0))
    basket.draw()
    
    for fruit in fruitlist:
        fruit.draw()
    
    for bomb in bomblist:
        bomb.draw()
    
    screen.draw.text("Score: " + str(score), (10, 10), color="white")

def new_fruit():
    fruit = Actor(random.choice(fruits), (random.randint(50, 550), 10))
    fruitlist.append(fruit)
    clock.schedule(new_fruit, 1)

def new_bomb():
    bomb = Actor("bomb", (random.randint(50, 550), 10))
    bomblist.append(bomb)
    clock.schedule(new_bomb, 3)



def update():
    global gameover
    global score

  
    if keyboard.right:
        basket.x += 5
    if keyboard.left:
        basket.x -= 5

    for fruit in fruitlist[:]:
        fruit.y += 3

        if basket.colliderect(fruit):
            fruitlist.remove(fruit)
            score += 1

        elif fruit.y > HEIGHT:
            fruitlist.remove(fruit)


    for bomb in bomblist[:]:
        bomb.y += 4

        if basket.colliderect(bomb):
            bomblist.remove(bomb)
            score -= 2   

        elif bomb.y > HEIGHT:
            bomblist.remove(bomb)

    if score <0:
        gameover=True

        



new_fruit()
new_bomb()

pgzrun.go()
