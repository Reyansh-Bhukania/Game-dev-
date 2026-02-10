import pgzrun 
import random
HEIGHT=500
WIDTH=600
basket=Actor("baskett",(300,400))
fruitlist=[]
fruits=["apple","dragonfruit","strawberry"]
score=0
def draw():
    screen.blit("background",(0,0))
    basket.draw()
    for fruit in fruitlist:
      fruit.draw()
    screen.draw.text(str(score),center=(10,10))
def new_fruit():
    global fruit
    fruit=Actor(random.choice(fruits),(random.randint(50,550),10))
    fruitlist.append(fruit)

    clock.schedule(new_fruit,1)

def update():
    global score
    if keyboard.right:
        basket.x+=5
    
    if keyboard.left:
        basket.x-=5 
    for fruit in fruitlist:
        fruit.y+=3

        if basket.colliderect (fruit):
          fruitlist.remove(fruit)  
          score+=1
        if fruit.y>500:
            fruitlist.remove(fruit) 
            








new_fruit()





































pgzrun.go()
 
