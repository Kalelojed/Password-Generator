import sys
import os
import tkinter as tk
from tkinter import *
import customtkinter as ctk
from PIL import *
import pyglet
import generator
from generator import Generator

#To Import Images/Fonts
def resourse_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

#Aesthetic Settings
MainFont = 'Clash Grotesk'
MainBackgroundColor = '#131218'
MainFontColor = '#E4E3E9'
MainButtonColor = '#a6cfff'
SecondaryBackgroundColor = "#2C2B35"
SecondaryFontColor = "#747380"
SecondaryButtonColor = '#87adda'
SecondaryButtonHoverColor = "#6c92bf"
MainFontFile = resourse_path('Assets/ClashGrotesk-Regular.ttf')
pyglet.options['win32_gdi_font'] = True
pyglet.font.add_file(MainFontFile)

genComponent = Generator()

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.title('Password Generator')
app.geometry('300x400')
app.iconbitmap(resourse_path('Assets/icon.ico'))
app.resizable(False, False)

def updateCharCount(val):
    charsLabel.configure(text=f'Characters: {charCount.get()}')

def Generate():
    PassResult.set(genComponent.GeneratePass(charCount.get(), IncludeUpper.get(), IncludeLower.get(), IncludeNums.get(), IncludeSymbols.get()))

def canGenerate():
    GenButton.configure(state='disabled' if IncludeUpper.get() | IncludeLower.get() | IncludeNums.get() | IncludeSymbols.get() == False else 'normal')

def copyPassword():
    app.clipboard_clear()
    app.clipboard_append(PassResult.get())

#Background
BackgroundFrame = ctk.CTkFrame(app, width=300, height=400, corner_radius=0, fg_color=MainBackgroundColor)
BackgroundFrame.pack(fill='both')
BackgroundFrame.pack_propagate(False)

#App Title
Title = ctk.CTkLabel(BackgroundFrame, text='Password Generator', text_color=MainFontColor, font=(MainFont, 17))
Title.pack(pady=15)

#Generated Password Result
PassResult = tk.StringVar(value='')
PassResultFrame = ctk.CTkEntry(BackgroundFrame, fg_color=SecondaryBackgroundColor, width=250, height=45, corner_radius=0, border_width=0, font=(MainFont, 18), state='disabled', text_color=MainFontColor, textvariable=PassResult)
PassResultFrame.pack()
PassResultFrame.pack_propagate(False)
CopyImg = Image.open(resourse_path('Assets/copy.png'))
CopyIcon = ctk.CTkImage(dark_image=CopyImg, light_image=CopyImg)
PassResultCopy = ctk.CTkButton(PassResultFrame, text='', fg_color='transparent', height=40, width=40, corner_radius=0, image=CopyIcon, hover_color=MainBackgroundColor, command=copyPassword)
PassResultCopy.place(x=205, y=2)

#Options
charCount = tk.IntVar(value=10)
IncludeUpper = tk.BooleanVar(value=True)
IncludeLower = tk.BooleanVar(value=True)
IncludeNums = tk.BooleanVar(value=True)
IncludeSymbols = tk.BooleanVar(value=True)

#Options GUI
OptionsFrame = ctk.CTkFrame(BackgroundFrame, fg_color=SecondaryBackgroundColor, width=250, height=250, corner_radius=0, border_width=0)
OptionsFrame.pack(pady=10)
OptionsFrame.pack_propagate(False)
charsLabel = ctk.CTkLabel(OptionsFrame, text=f'Characters: {charCount.get()}', font=(MainFont, 15))
charsLabel.place(x=22, y=10)
charsSlider = ctk.CTkSlider(OptionsFrame, variable=charCount, width=230, height=10, border_width=0, from_=8, to=20, progress_color=MainButtonColor, number_of_steps=12, corner_radius=0, command=updateCharCount)
charsSlider.place(x=10, y=40)
UppercaseCheck = ctk.CTkCheckBox(OptionsFrame, variable=IncludeUpper, onvalue=True, offvalue=False, fg_color=SecondaryButtonColor, border_color=SecondaryButtonColor, width=12, height=12, text='Include Uppercase Letters', font=(MainFont, 15), command=canGenerate)
UppercaseCheck.place(x=10, y=70)
LowercaseCheck = ctk.CTkCheckBox(OptionsFrame, variable=IncludeLower, onvalue=True, offvalue=False, fg_color=SecondaryButtonColor, border_color=SecondaryButtonColor, width=12, height=12, text='Include Lowercase Letters', font=(MainFont, 15), command=canGenerate)
LowercaseCheck.place(x=10, y=100)
NumbersCheck = ctk.CTkCheckBox(OptionsFrame, variable=IncludeNums, onvalue=True, offvalue=False, fg_color=SecondaryButtonColor, border_color=SecondaryButtonColor, width=12, height=12, text='Include Numbers', font=(MainFont, 15), command=canGenerate)
NumbersCheck.place(x=10, y=130)
SymbolCheck = ctk.CTkCheckBox(OptionsFrame, variable=IncludeSymbols, onvalue=True, offvalue=False, fg_color=SecondaryButtonColor, border_color=SecondaryButtonColor, width=12, height=12, text='Include Symbols', font=(MainFont, 15), command=canGenerate)
SymbolCheck.place(x=10, y=160)

#Generate Button
GenButton = ctk.CTkButton(OptionsFrame, text='Generate Password', font=(MainFont, 20), fg_color=SecondaryButtonColor, hover_color=SecondaryButtonHoverColor, text_color=MainFontColor, width=240, height=50, command=Generate)
GenButton.place(x=5, y=195)

app.mainloop()