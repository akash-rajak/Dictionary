# data we got from data.json file

import json  # imported json, because our data is in json form
from difflib import get_close_matches  # imported get close matches from difflib
import tkinter as tk  # imported tkinter

# first loads the data of json file in variable data.json
data = json.load(open("data.json"))

# def clear_text():
#     word = inputtxt.get("1.0", "end-1c")
#     print(type(word))

# defined function for translating
def translate():
    word = inputtxt.get("1.0", "end-1c")
    # print(word)
    word = word.lower()
    if word == "":
        lbl.config(text = "You Entered Nothing! Please Enter Some Text.")
    elif word in data:  # is word is not present it will print None
        str = ""
        for i in data[word]:
            str+=i
        lbl.config(text = str)
    elif word.title() in data:  # when word entered is title
        str = ""
        for i in data[word.title()]:
            str += i
        lbl.config(text = str)
    elif word.upper() in data:
        str = ""
        for i in data[word.upper()]:
            str += i
        lbl.config(text = str)
    elif len(get_close_matches(word, data.keys())) > 0:  # case of close matches
        suggested_word = ""
        for i in get_close_matches(word, data.keys())[0]:
            suggested_word += i
        suggested_meaning = ""
        for i in data[get_close_matches(word, data.keys())[0]]:
            suggested_meaning += i

        lbl.config(text="Meaning of closest word " + suggested_word + " : " + suggested_meaning)
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
        lbl.config(text = "You have entered wrong word!")

# Top level window
frame = tk.Tk()
frame.title("Dictionary")
frame.geometry('1000x500')

dic = tk.Label(text = "DICTIONARY", font=("Arial", 50), fg="magenta") # same way bg
dic.pack()

start = tk.Label(text = "Enter the word you want to search : ", font=("Arial", 30), fg="red")
start.pack()

# TextBox Creation
inputtxt = tk.Text(frame,height = 5, width = 60, font=("Arial", 15), bg = "light yellow")
inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,text="Find",command= lambda: translate(),font=("Arial", 20), bg = "light green", fg = "blue")
printButton.pack()

# printButton = tk.Button(frame,text="Clear",command= lambda: clear_text(),font=("Arial", 20), bg = "light green", fg = "blue")
# printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "Find Meaning Here!",font=("Arial", 20), fg = "brown")
lbl.pack()
frame.mainloop()

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