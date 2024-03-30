from tkinter import *
import random

print("---------------------------------7,UP or DOWN---------------------------------")
print("Rules of the game:")
print("1.This is a betting game.")
print("2.There are 3 slots where you can place  your money .")    
print("Slot 1:7 DOWN")
print("Slot 2:EXACT 7")
print("Slot 3:7 UP")
print("3.After placing your money on any of these slots ,2 dice are rolled.If the sum of the 2 numbers on the face of the dice satisfies the condtion on which you had")
print("kept your money ,then you win and get respective awards,else you lose your money.")
print()
print("AWARDS:")
print("a. 7 down: 2x your money")
print("b. Exact 7: 4x your money")
print("c. 7 up: 2x your money")  
print() 


def get_number(x):
    if x =='\u2680':
        return(1)
    elif x =='\u2681':
        return(2)
    elif x =='\u2682':
        return(3)
    elif x =='\u2683':
        return(4)
    elif x =='\u2684':
        return(5)
    elif x =='\u2685':
        return(6)

name=input("Please enter your name:")
slot=input("Please choose your slot:")
money=int(input("Please set the amount of money you want to bet on your respective slot:₹"))  

root =Tk()
root.title('Roll the dice')
root.geometry("500x500")

def roll_dice():
    
    d1 =random.choice(my_dice)
    d2 = random.choice(my_dice)

    sd1 =get_number(d1)
    sd2 =get_number(d2)

    dice_label1.config(text=d1)
    dice_label2.config(text=d2)

    sub_dice_label1.config(text =sd1)
    sub_dice_label2.config(text =sd2)

    total =sd1+sd2
    total_label.config(text =f"Sum : {total}")

    if total<7 and slot.upper().strip()=="7 DOWN":
        
        print(name," YOU WIN!")
        print("CASH PRIZE WON:₹",2*money)    
    else:
        if total==7 and slot.upper().strip=="EXACT 7": 
            print(name," YOU WIN!")
            print("CASH PRIZE WON:₹",4*money)
            
        elif total>7 and slot.upper().strip()=="7 UP":
            print(name," YOU WIN!")
            print("CASH PRIZE WON:₹",2*money)

        else:
            print(name,",sorry you didn't win.Better luck next time!")


my_dice =['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']

my_frame =Frame(root)
my_frame.pack(pady =20)

dice_label1 =Label(my_frame,text ='',font=("Helvetica",100) ,fg ="black")
dice_label1.grid(row=0,column=0,padx=5)
sub_dice_label1 =Label(my_frame,text="")
sub_dice_label1.grid(row =1, column=0)

dice_label2 =Label(my_frame,text ='',font=("Helvetica",100) ,fg ="black")
dice_label2.grid(row=0,column=1,padx=5)
sub_dice_label2 =Label(my_frame,text="")
sub_dice_label2.grid(row =1, column=1)

my_button =Button(root,text ='Roll Dice', command =roll_dice, font =("Helvetica",24))
my_button.pack(pady =20)

total_label =Label(root,text ="",font =("Helvetica",24))
total_label.pack(pady=40)

root.mainloop()
