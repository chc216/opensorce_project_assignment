from myTurtle import *
import turtle

inStr = ''
swidth, sheight = 300, 300
tx, ty, tangle, tsize = [0]*4

turtle.title('거북이 글자쓰기(모듈버전)')
turtle.shape('turtle')
turtle.setup(width = swidth+50, height = sheight+50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.speed(5)

inStr = getString()

for ch in inStr:
    tx, ty, tangle, txtsize = getXYAS(swidth, sheight)
    r,g,b = getRGB()

    turtle.goto(tx,ty)
    turtle.left(tangle)

    turtle.pencolor((r,g,b))
    turtle.write(ch,font = ('맑은고딕', txtsize, 'bold'))

turtle.done()
