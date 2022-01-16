from tkinter import *
from tkinter.font import Font
import tkinter.messagebox as msg

root= Tk()
root.title('TIC-TAC-TOE')

Label(root,text="Player1 : X",font="times 15").grid(row=0,column=1)
Label(root,text="Player2 : O",font="times 15").grid(row=0,column=2) 

digits = [1,2,3,4,5,6,7,8,9]

mark = ''

count = 0

panels = ["panel"]*10

def win(sign,panels):
    return ((panels[1]== panels[2]== panels[3]== sign)
            or (panels[1]== panels[4]== panels [7]== sign)
            or (panels[1]== panels[5]== panels [9]== sign)
            or (panels[2]== panels[5]== panels [8]== sign) 
            or (panels[3]== panels[6]== panels [9]== sign)
            or (panels[3]== panels[5]== panels [7]== sign)
            or (panels[4]== panels[5]== panels [6]== sign)
            or (panels[7]== panels[8]== panels [9]== sign))

button1=Button(root,width=15,font=('Times 16 bold'),height=7, command=lambda:checker(1))
button1.grid(row=1,column=1)


button2=Button(root,width=15,height=7,font=('Times 16 bold'), command=lambda:checker(2))
button2.grid(row=1,column=2)


button3=Button(root,width=15,height=7,font=('Times 16 bold'), command=lambda:checker(3))
button3.grid(row=1,column=3)


button4=Button(root,width=15,height=7,font=('Times 16 bold'), command=lambda:checker(4))
button4.grid(row=2,column=1)


button5=Button(root,width=15,height=7,font=('Times 16 bold'), command=lambda:checker(5))
button5.grid(row=2,column=2)


button6=Button(root,width=15,height=7,font=('Times 16 bold'), command=lambda:checker(6))
button6.grid(row=2,column=3)


button7=Button(root,width=15,height=7,font=('Times 16 bold'), command=lambda:checker(7))
button7.grid(row=3,column=1)


button8=Button(root,width=15,height=7,font=('Times 16 bold'), command=lambda:checker(8))
button8.grid(row=3,column=2)

button9=Button(root,width=15,height=7,font=('Times 16 bold'), command=lambda:checker(9))
button9.grid(row=3,column=3)

listofButtons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

def checker(buttonNumber):
    global count, digits, mark, panels, listofButtons

    if buttonNumber < 10 and buttonNumber in digits:
        digits.remove(buttonNumber) #Removes Button Number from Digits List

        if count%2 == 0:
            mark = 'X'
        else:
            mark = 'O'

        panels[buttonNumber] = mark
        listofButtons[buttonNumber - 1].config(text=mark)

        if(win(mark,panels) and mark == "X"):
            msg.showinfo('Result', 'player 1 Wins')
            root.destroy()
        elif(win(mark, panels) and mark == "O"):
            msg.showinfo('Result', 'player 2 wins')
            root.destroy()

        count += 1

    if count > 8 and win('X', panels) == False and win('O',panels) == False:
        msg.showinfo('Result', 'No one Wins... Match Tied')
        root.destroy()


root.mainloop()
        

            
