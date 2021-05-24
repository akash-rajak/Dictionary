# data we got from data.json file

# -----------------------------------------------------------------------------------------------------
import io # used for printing the output in textarea
import json  # imported json, because our data is in json form
from difflib import get_close_matches  # imported get close matches from difflib
import tkinter as tk  # imported tkinter
from tkinter import *
# ----------------------------------------------------------------------------------------------------


# first loads the data of json file in variable data.json
data = json.load(open("data.json"))

# def clear_text():
#     word = inputtxt.get("1.0", "end-1c")
#     print(type(word))

# ----------------------------------------------------------------------------------------------------
# defined function for translating
def translate():
    word = inputtxt.get("1.0", "end-1c")
    # print(word)
    word = word.lower()
    if word == "":
        # lbl.config(text="You Entered Nothing! Please Enter Some Text.")

        buffer = io.StringIO()
        print("You Entered Nothing! Please Enter Some Text.", file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)
        buffer.flush()

    elif word in data:  # is word is not present it will print None
        str = ""
        cnt = 0
        for i in data[word]:
            cnt = cnt + 1
            str_cnt = f'{cnt}'
            str+=(str_cnt + ".) ")
            str+=i
            str+="\n\n"
        # lbl.config(text = str)

        buffer = io.StringIO()
        print("Meaning of closest word \"" + word + "\" : \n\n" + str, file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)
        buffer.flush()

    elif word.title() in data:  # when word entered is title
        str = ""
        cnt = 0
        for i in data[word.title()]:
            cnt = cnt + 1
            str_cnt = f'{cnt}'
            str += (str_cnt + ".) ")
            str += i
            str += "\n\n"
        # lbl.config(text = str)

        buffer = io.StringIO()
        print("Meaning of closest word \"" + word + "\" : \n\n" + str, file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)
        buffer.flush()

    elif word.upper() in data:
        str = ""
        cnt = 0
        for i in data[word.upper()]:
            cnt = cnt + 1
            str_cnt = f'{cnt}'
            str += (str_cnt + ".) ")
            str += i
            str += "\n\n"
        # lbl.config(text = str)

        buffer = io.StringIO()
        print("Meaning of closest word \"" + word + "\" : \n\n" + str, file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)
        buffer.flush()

    elif len(get_close_matches(word, data.keys())) > 0:  # case of close matches
        suggested_word = ""
        for i in get_close_matches(word, data.keys())[0]:
            suggested_word += i
        suggested_meaning = ""
        cnt = 0
        for i in data[get_close_matches(word, data.keys())[0]]:
            cnt = cnt + 1
            str_cnt = f'{cnt}'
            suggested_meaning += (str_cnt + ".) ")
            suggested_meaning += i
            suggested_meaning += "\n\n"

        # lbl.config(text="Meaning of closest word \"" + suggested_word + "\" : " + suggested_meaning)

        buffer = io.StringIO()
        print("Meaning of closest word \"" + suggested_word + "\" : \n\n" + suggested_meaning, file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)
        buffer.flush()


        # print("Did you mean %s instead " % get_close_matches(word, data.keys())[0])
        # decide = input("Press y for yes and n for no : ")
        # if decide == "y":  # if pressed y, it will give meaning of suggested word
        #     print(data[get_close_matches(word, data.keys())[0]])
        # elif decide == "n":
        #     lbl.config(text="Meaning : " + data[word])
        #     print("None")
        # else:
        #     lbl.config(text="Meaning : " + data[word])
        #     print("You have entered wrong word!")
    else:
        # lbl.config(text = "You have entered wrong word!")

        buffer = io.StringIO()
        print("You have entered some wrong word!", file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)

        buffer.flush()

# ----------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------
# Top level window
frame = tk.Tk()
frame.title("Dictionary")
frame.geometry('1000x500')
frame.state('zoomed') # for default maximize way
# frame.configure(background='grey') # for background color of gui window

# bg image part ----------------------------------------------------------
# # Add image file
# bg = PhotoImage(file="bg_image.png")
#
# # Show image using label
# label1 = Label(root, image=bg)
# label1.place(x=0, y=0)
# Add image file
# bg = PhotoImage(file="bg_image.png")
#
# # Create Canvas
# canvas1 = Canvas(root, width=400,
#                  height=400)
#
# canvas1.pack(fill="both", expand=True)
#
# # Display image
# canvas1.create_image(0, 0, image=bg,
#                      anchor="nw")
# ----------------------------------------------------------------------

dic = tk.Label(text = "DICTIONARY", font=("Arial", 50), fg="magenta",underline=0) # same way bg
dic.pack()

start = tk.Label(text = "Enter the word you want to search : ", font=("Arial", 30), fg="red")
start.pack(padx=6, pady=20)

# Input TextBox Creation
inputtxt = tk.Text(frame,height = 5, width = 60, font=("Arial", 15), bg = "light yellow",fg = "brown")
inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,text="Find",command= lambda: translate(),font=("Arial", 20), bg = "light green", fg = "blue")
printButton.pack(padx=6, pady=20)

# printButton = tk.Button(frame,text="Clear",command= lambda: clear_text(),font=("Arial", 20), bg = "light green", fg = "blue")
# printButton.pack()

# Label Creation
# lbl = tk.Label(frame, text = "Find Meaning Here!",font=("Arial", 20), fg = "brown")
# lbl.pack(padx=6, pady=20)

# lbl1 = tk.Label(frame, text = "Next Line!",font=("Arial", 20), fg = "brown")
# lbl1.pack(padx=6, pady=20)

# Output TextBox Creation
outputtxt = tk.Text(frame,height = 15, width = 100, font=("Arial", 15), bg = "light yellow", fg = "brown")
outputtxt.pack()

frame.mainloop()

# ----------------------------------------------------------------------------------------------------

'''
# code only when working with console
# data we got from data.json file

import json # imported json, because our data is in json form
from difflib import get_close_matches # imported close matches from difflib

# first loads the data of json file in variable data.json
data = json.load(open("data.json"))

# # printing the read data on console
# print(data)
#
# # printing for particular word
# print(data["smog"])
# print(data["access road"])
# # print(data["SMOG"])

# defined function for translating
def translate(word):
    word = word.lower()
    if word in data: # is word is not present it will print None
        return data[word]
    elif word.title() in data: # when word entered is title
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:  # case of close matches
        print("Did you mean %s instead "  %get_close_matches(word,data.keys())[0])
        decide = input("Press y for yes and n for no : ")
        if decide == "y": # if pressed y, it will give meaning of suggested word
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == "n":
            return None
        else:
            return "You have entered wrong word!"
    else:
        return "You have entered wrong word!"

word = input("Enter the word you want to search : ")
# word_meaning = data[word]
word_meaning = translate(word)

# print(word_meaning) # incase of interface it will print the output in list format
cnt = 0
if type(word_meaning) == list:
    for item in word_meaning:
        cnt = cnt + 1
        print(cnt,"->", item)
else:
    print(word_meaning)

'''