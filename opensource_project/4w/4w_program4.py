import random
import  turtle
import random
from tkinter.simpledialog import *

instr = ''
swidth, sheight = 300, 300
tx,ty,txtsize = [0] * 3

turtle.title('거북이 글자쓰기')
turtle.shape('turtle')
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth, sheight)
turtle.penup()

instr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')

for ch in instr :
    tx = random.randrange(-swidth/2, swidth/2)
    ty = random.randrange(-sheight/2, sheight/2)
    r = random.random()
    g = random.random()
    b = random.random()
    txtsize = random.randrange(10, 50)

    turtle.goto(tx,ty)

    turtle.pencolor((r,g,b))
    turtle.write(ch, font=('맑은고딕', txtsize, 'bold'))

turtle.done()

