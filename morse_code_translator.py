from tkinter import *

morse_alphabet = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e",
                  "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j",
                  "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o",
                  ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
                  "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z"}


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Text in morse')
        self.lbl2 = Label(win, text='Translation')
        self.t1 = Entry(bd=3)
        self.t2 = Entry()
        self.btn1 = Button(win, text='Translate!')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.b1 = Button(win, text='Translate!', command=self.translate)
        self.b1.place(x=100, y=150)
        self.lbl2.place(x=100, y=200)
        self.t2.place(x=200, y=200)

    def translate(self):
        self.t2.delete(0, 'end')
        text = self.t1.get()
        translated_message = []
        words_in_morse_to_translate = text.split(" | ")

        for word in words_in_morse_to_translate:
            current_word = ""
            for letter in word.split():
                if letter in morse_alphabet:
                    current_word += morse_alphabet[letter]
            translated_message.append(current_word)

        self.t2.insert(END, str(' '.join(translated_message).upper()))


window = Tk()
mywin = MyWindow(window)
window.title('Morse translator')
window.geometry("500x500+10+10")
window.mainloop()

# the following lines represent the logic I used that should be then implemented to the GUI

# words_in_morse_to_translate = input().split(" | ")
#
# translated_message = []
# morse_alphabet = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e",
#                   "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j",
#                   "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o",
#                   ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
#                   "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z"}
# for word in words_in_morse_to_translate:
#     current_word = ""
#     for letter in word.split():
#         if letter in morse_alphabet:
#             current_word += morse_alphabet[letter]
#     translated_message.append(current_word)
#
# print(' '.join(translated_message).upper())
# input examples:
# .. | -- .- -.. . |  -.-- --- ..- | .-- .-. .. - . | .- | .-.. --- -. --. | -.-. --- -.. .
# this should result in the output I MADE YOU WRITE A LONG CODE
# input
# .. | .... --- .--. . | -.-- --- ..- | .- .-. . | -. --- - | -- .- -..
# output
# I HOPE YOU ARE NOT MAD