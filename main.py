#joke generator from ~/shortjokes.csv
import pandas as pd
import random
#GUI with tkinter
import tkinter as tk
from PIL import Image, ImageTk


jokes = []
def load_jokes():

    df = pd.read_csv('shortjokes.csv')
    #print(df)

    #remove id column
    df.drop(df.columns[0], axis=1, inplace=True)

    #append joke column to jokes list
    for i in range(len(df)):
        jokes.append(df.iloc[i][0])
    return jokes

def get_joke():
    print(random.choice(jokes))

load_jokes()



#create window
root = tk.Tk()
root.title('Joke Generator')
root.geometry('1920x1080')

#show image
logo = Image.open('lol.png')
logo = logo.resize((400, 400), Image.ANTIALIAS)
img = ImageTk.PhotoImage(logo)
label1 = tk.Label(root, image=img)
label1.pack()

#create label
label = tk.Label(root, text='Joke Generator\nClick button to get a joke\n***', font=('Helvetica', 20))
label.pack()





label2 = tk.Label(root, text='', font=('Helvetica', 14))
label2.pack()

#function to put joke on label on click
def on_click():
    label2.config(text=random.choice(jokes))

#create button
button = tk.Button(root, text='Get Joke', command=on_click)
button.pack()






#loop
root.mainloop()
