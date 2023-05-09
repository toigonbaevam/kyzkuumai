from tkinter import*
import time
import random

winner = False
boy_x=0
boy_y=20

girl_x=-28
girl_y=110


def start_game():
    global girl_x
    global boy_x
    global winner
    
    while winner==False:
        time.sleep(0.05)
        random_move_girl=random.randint(0,20)
        random_move_boy=random.randint(0,20)
        #updare the x positions of the horses
        girl_x+=random_move_girl
        boy_x+=random_move_boy
        
        move_horses(random_move_boy,random_move_girl)
        main_screen.update()
        winner=check_winner()
        
    if winner =='Tie':
        Label(main_screen,text=winner,font=('calibri',20),fg='green').place(x=200,y=450)
    else:
        Label(main_screen,text=winner+'Wins!!!',font=('calibri',20),fg='green').place(x=200,y=450)
        
    
def move_horses(boy_random_move,girl_random_move):
    canvas.move(boy,boy_random_move,0)
    canvas.move(girl,girl_random_move,0)
    
    
def check_winner():
    if girl_x >=550 and boy_x >=550:
        return  "Tie"
    if girl_x >=550:
        return "Girl  "
    if boy_x >=550:
        return "Boy  "
    return False
    


main_screen=Tk()
main_screen.title('kyzkuumai')
main_screen.geometry('600x500')
main_screen.config(background='white')


#set up the canvas
canvas=Canvas(main_screen,width=600,height=300,bg='white')
canvas.pack(pady=20)

#import the img
boy_img=PhotoImage(file='./boy.png')
girl_img=PhotoImage(file='./girl.png')


#resizing the img
boy_img=boy_img.zoom(15)
boy_img=boy_img.subsample(50)
girl_img=girl_img.zoom(15)
girl_img=girl_img.subsample(90)


#add img to canvas
boy=canvas.create_image(boy_x,boy_y,anchor=NW,image=boy_img)
girl=canvas.create_image(girl_x,girl_y,anchor=NW,image=girl_img)


#add labels to screen
l1=Label(main_screen,text='Select your horse',font=('calibri',20),bg='white')
l1.place(x=230,y=280)
l2=Label(main_screen,text='Click play when ready!',font=('calibri',20),bg='white')
l2.place(x=200,y=330)

b1=Button(main_screen,text='Play',height=2,width=15,bg='white',font=('calibri',10),command=start_game)
b1.place(x=250,y=390)





main_screen.mainloop()