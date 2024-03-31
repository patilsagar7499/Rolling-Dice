import tkinter as tk
import random

def get_number(x):
    if x == '\u2680':
        return 1
    elif x == '\u2681':
        return 2
    elif x == '\u2682':
        return 3
    elif x == '\u2683':
        return 4
    elif x == '\u2684':
        return 5
    elif x == '\u2685':
        return 6

def roll_dice():
    global score, total_score
    d1 = random.choice(my_dice)
    d2 = random.choice(my_dice)

    sd1 = get_number(d1)
    sd2 = get_number(d2)

    dice_label1.config(text=d1)
    dice_label2.config(text=d2)

    total = sd1 + sd2
    total_label.config(text=f"Sum : {total}")

    if total < 7 and (slot_var.get().lower().strip() == "7 down" or slot_var.get() == "1") :
        result_label.config(text=f"{name}, YOU WIN!\nCASH PRIZE WON: ₹{2*money}")
        score += 2*money
    elif total == 7 and (slot_var.get().lower().strip() == "exact 7"or slot_var.get() == "2"):
        result_label.config(text=f"{name}, YOU WIN!\nCASH PRIZE WON: ₹{4*money}")
        score += 4*money
    elif total > 7 and (slot_var.get().lower().strip() == "7 up" or slot_var.get() == "3"):
        result_label.config(text=f"{name}, YOU WIN!\nCASH PRIZE WON: ₹{2*money}")
        score += 2*money
    elif (slot_var.get().lower().strip() != "7 up" and slot_var.get() != "3") and (slot_var.get().lower().strip() != "exact 7"and slot_var.get() != "2") and (slot_var.get().lower().strip() != "7 down" and slot_var.get() != "1"):
        result_label.config(text=f"{name}, Invalid Input!")
    else:
        result_label.config(text=f"{name}, sorry you didn't win. ₹{money} subtracted from your score.")
        score -= money

    total_score += score
    score_label.config(text=f"Current Score: {score}\nTotal Score: {total_score}")

root = tk.Tk()
root.title('Roll the dice')
root.geometry("500x600")

my_dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

instruction_label = tk.Label(root, text="Instructions:", font=("Helvetica", 16, "bold"))
instruction_label.pack(pady=10)

instruction_text = """
1. Enter your name in the text box provided.
2. Choose a slot by typing '(1)7 DOWN', '(2)EXACT 7', or '(3)7 UP'.
3. Set the amount of money you want to bet on your chosen slot.
4. Click the 'Start Game' button to begin.
5. After the dice are rolled, the result will be displayed below.
6. Your current score will also be shown.
7. You can play the game again by entering new details and clicking 'Start Game'.
"""
instruction_label = tk.Label(root, text=instruction_text, justify="left")
instruction_label.pack()

name_label = tk.Label(root, text="Please enter your name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

slot_label = tk.Label(root, text="Please choose your slot:")
slot_label.pack()
slot_var = tk.StringVar()
slot_entry = tk.Entry(root, textvariable=slot_var)
slot_entry.pack()

money_label = tk.Label(root, text="Please set the amount of money you want to bet on your respective slot: ₹")
money_label.pack()
money_var = tk.IntVar()
money_entry = tk.Entry(root, textvariable=money_var)
money_entry.pack()

score = 0
total_score = 0

def start_game():
    global name, money, score
    global total_score
    name = name_entry.get()
    money = money_var.get()
    score = 0
    score_label.config(text=f"Current Score: {score}\nTotal Score: {total_score}")
    roll_dice()

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

game_frame = tk.Frame(root)
game_frame.pack(pady=20)

dice_label1 = tk.Label(game_frame, text='', font=("Helvetica", 100), fg="black")
dice_label1.grid(row=0, column=0, padx=5)
dice_label2 = tk.Label(game_frame, text='', font=("Helvetica", 100), fg="black")
dice_label2.grid(row=0, column=1, padx=5)

total_label = tk.Label(root, text="", font=("Helvetica", 24))
total_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 24))
result_label.pack(pady=10)

score_label = tk.Label(root, text="", font=("Helvetica", 24))
score_label.pack()

root.mainloop()
