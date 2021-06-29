#! python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 13:40:22 2021

@author: Mr. Shark Spam Bot
"""
import tkinter

while True:
    try:

        # Create the window.
        window = tkinter.Tk()
        window.title('''''')
        WINDOW_HEIGHT = ''
        WINDOW_WIDTH = ''
        window.geometry(WINDOW_HEIGHT + 'x' + WINDOW_WIDTH)

        # Add the text.
        TEXT = ''''''
        hacked_letter = tkinter.Text(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
        hacked_letter.pack()
        hacked_letter.insert(tkinter.END, TEXT)
        hacked_letter.config(state='disabled')
        tkinter.mainloop()

    except KeyboardInterrupt:
        continue
