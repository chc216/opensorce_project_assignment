from tkinter import *
from time import *

fnameList = ["jeju1.jpg", "jeju2.jpg", "jeju3.jpg", "jeju4.jpg"]

photolist = [None] * 4
num = 0

def clicknext():
    global num
    num += 1
    if num > 3:
        num = 0
    photo = PhotoImage(file = "/Users/cheol/dev/opensorce_project_assignment/opensource_project/5w/gif/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 3
    photo = PhotoImage(file = "/Users/cheol/dev/opensorce_project_assignment/opensource_project/5w/gif/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<<이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clicknext)

photo = PhotoImage(file = "/Users/cheol/dev/opensorce_project_assignment/opensource_project/5w/gif/" + fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x=15, y=50)


window.mainloop()