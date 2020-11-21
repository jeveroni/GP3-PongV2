import tkinter
import tkinter.messagebox
import numpy as np
import random
from PIL import Image, ImageTk
from tkinter import *
import pickle


window = tkinter.Tk()
window.geometry("800x600")
window.title("Jev's Pong Game")
window.resizable(0, 0)


def circle_move():
    global velocity
    global circle_centre
    global curr_score
    global paddle_length
    global circle_radius
    global timer_length
    global hy_score
        
    if((circle_centre[0]-circle_radius+velocity[0] < 0) or (circle_centre[0]+circle_radius+velocity[0] > 400)):
        velocity[0] = -velocity[0]
    elif((circle_centre[1]-circle_radius+velocity[1] < 0)):
        velocity[1] = -velocity[1]
    elif(circle_centre[1]+circle_radius+velocity[1] > 600):
        if(curr_score > hy_score):
            hy_score = curr_score
            with open('score.dat', 'wb') as file:
                pickle.dump(hy_score, file)
            hi_score.configure(text = f'High Score: {hy_score}')
        curr_score = 0
        velocity[1] = - velocity[1]
        score.configure(text=f'Score: {curr_score}')
        circle_radius=20
        paddle_length=30
        if(velocity[0] > 0):
            velocity[0]=velocities[0]
        else:
            velocity[0]=-velocities[0]
        velocity[1]=-velocities[0]
        board.coords(ball,circle_centre[0]-circle_radius,circle_centre[1]-circle_radius,circle_centre[0]+circle_radius,circle_centre[1]+circle_radius)
        board.coords(paddle, paddle_x-paddle_length, 550, paddle_x+paddle_length, 560)

    if(circle_centre[1]+circle_radius>549 and circle_centre[1]+circle_radius<560 and circle_centre[1]+circle_radius<circle_centre[1]+circle_radius+velocity[1]):
        for i in range(paddle_x-paddle_length, paddle_x+paddle_length, 1):
            if(circle_centre[0] == i):
                velocity[1] = -velocity[1]
                curr_score = curr_score+1
                score.configure(text=f'Score: {curr_score}')
                if(curr_score%10==0):
                    circle_radius=circle_radius-(curr_score/10)
                    board.coords(ball,circle_centre[0]-circle_radius,circle_centre[1]-circle_radius,circle_centre[0]+circle_radius,circle_centre[1]+circle_radius)
                    paddle_length=int(paddle_length-(5*(curr_score/10)))
                    board.coords(paddle, paddle_x-paddle_length, 550, paddle_x+paddle_length, 560)
                    if(velocity[0] > 0):
                        velocity[0] = velocities[int(curr_score/10)]
                    else:
                        velocity[0]= -velocities[int(curr_score/10)]
                    if(velocity[1] > 0):
                        velocity[1] = velocities[int(curr_score/10)]
                    else:
                        velocity[1] = -velocities[int(curr_score/10)]

                
                
    board.move(ball,velocity[0],velocity[1])
    circle_centre[0] = circle_centre[0] + velocity[0]
    circle_centre[1] = circle_centre[1] + velocity[1]
    

def position(event):
    global paddle_x
    xroot = event.x_root
    boardx = board.winfo_rootx()
    newx = xroot-boardx
    while(newx > paddle_x):
            board.move(paddle, 1, 0)
            paddle_x = paddle_x + 1
    while(newx < paddle_x):
            board.move(paddle, -1, 0)
            paddle_x = paddle_x - 1
    
def timer():
    circle_move()
    window.after(timer_length, timer)
  


      
paddle_x = 200
circle_radius = 20
circle_centre = [75,75]
velocity=[5,5]
paddle_length = 30
timer_length = 10
curr_score=0
velocities=[5,6,7,8,9]






try:
    with open('score.dat', 'rb') as file:
        hy_score = pickle.load(file)
except:
    hy_score = 0


board = Canvas(window, background = 'light grey',borderwidth=0, highlightthickness=0)
board.place(x=200, y=0, height=600, width=400)
board.bind("<Motion>", position)
paddle =board.create_rectangle(paddle_x-paddle_length, 550, paddle_x+paddle_length, 560, fill="black")
ball = board.create_oval(circle_centre[0]-circle_radius,circle_centre[1]-circle_radius,circle_centre[0]+circle_radius,circle_centre[1]+circle_radius, fill= 'red')
score= tkinter.Label(window, background='light blue', text=f'Score: {curr_score}',font = "Helvetica 40 bold")
score.place(x=0,y=0, height=50, width=200)
hi_score = tkinter.Label(window,background='pink', text = f'High Score: {hy_score}', font="Helvetica 20 bold")
hi_score.place(x=600, y=0, height=50, width = 200)
timer()





window.mainloop()

#not very much commenting on this one, i'd actually given up because i found it too difficult and decided
#i was going to try pygame or c++, however i got it done in one sitting and didnt do any commenting
#however i think it runs well 
#might try and add a high score system but idk if its possible
