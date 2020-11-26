#ZOE ENGEL, CLASS 1

from tkinter import *
from random import sample
from datetime import *
from tkinter import messagebox


window = Tk()
window.title("Ithuba lottery app")
window.geometry("640x190")
window.config(bg="orange")

# WINDOW NAME
name_lbl = Label(window, text="ITHUBA LOTTERY GAME", font=28)
name_lbl.place(x=80, y=5)

# GENERATING SIX RANDOM NUMBERS
my_numbers = []
lotto = sample(range(0, 50), 6)
lotto.sort()
print(lotto)

# ADDING THE DATE
current_date = datetime.now()
mydate_lbl = Label(window)
mydate_lbl.config(text="Today's date: " + current_date.strftime("%d-%m-%y %H:%M"))
mydate_lbl.place(x=399, y=5)

# ENTRIES LABEL
entry_lbl = Label(window, font=20, text="Please enter your lotto entries: ")
entry_lbl.place(x=30, y=5)

# CREATING ENTRIES
entry1 = Entry(window, width=4, justify='center')
entry1.place(x=40, y=40)
entry2 = Entry(window, width=4, justify='center')
entry2.place(x=80, y=40)
entry3 = Entry(window, width=4, justify='center')
entry3.place(x=120, y=40)
entry4 = Entry(window, width=4, justify='center')
entry4.place(x=160, y=40)
entry5 = Entry(window, width=4, justify='center')
entry5.place(x=200, y=40)
entry6 = Entry(window, width=4, justify='center')
entry6.place(x=240, y=40)


# CREATING A FUNCTION TO CHECK FOR MATCHES BETWEEN LOTTO NUMBERS AND ENTRIES
def check():
    my_numbers.append(int(entry1.get()))
    my_numbers.append(int(entry2.get()))
    my_numbers.append(int(entry3.get()))
    my_numbers.append(int(entry4.get()))
    my_numbers.append(int(entry5.get()))
    my_numbers.append(int(entry6.get()))

    matches = 0
    for i in my_numbers:
        if i in lotto:
            matches += 1

    if matches == 0:
        result_lbl.config(text="Better luck next time!" + "\n" + "The winning lotto numbers are: " + "\n" + str(lotto))
    elif matches == 1:
        result_lbl.config(text="Better luck next time!" + "\n" + "The winning lotto numbers are: " + "\n" + str(lotto))
    elif matches == 2:
        result_lbl.config(text="YOU WON R20.00!" + "\n" + "The winning lotto numbers are: " + "\n" + str(lotto))
    elif matches == 3:
        result_lbl.config(text="YOU WON R100.50!" + "\n" + "The winning lotto numbers are: " + "\n" + str(lotto))
    elif matches == 4:
        result_lbl.config(text="YOU WON R2 384.00!" + "\n" + "The winning lotto numbers are: " + "\n" + str(lotto))
    elif matches == 5:
        result_lbl.config(text="YOU WON R8 584.00" + "\n" + "The winning lotto numbers are: " + "\n" + str(lotto))
    elif my_numbers == lotto:
        result_lbl.config(text="YOU'VE WON THE JACKPOT of R10,000 000.00!!" + "\n" + str(lotto))

# ADDING THE TEXT INTO A FILE (FILE HANDLING)
    lotto_txt = open("Lotto.txt", "w+")
    lotto_txt.write(result_lbl.cget("text"))


# CREATING A CHECK BUTTON
check_btn = Button(window, command=check, text="Check lotto")
check_btn.place(x=500, y=100, width=99)


# EXIT FUNCTION
def exit():
    lors= messagebox.askyesno(title="Message",message= "Are you sure you want to exit?")
    if lors == True:
        window.destroy()
    else:
        return None

# CREATING A RESULT LABEL
result_lbl = Label(window)
result_lbl.place(x=46, y=100)

# CREATING AN EXIT BUTTON
ext_btn = Button(window, command=exit, text="Exit")
ext_btn.place(x=500, y=140, width=99)

window.mainloop()
