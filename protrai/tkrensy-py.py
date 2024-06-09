# GUIで動くアプリを作ってみるよ

import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("アプリの練習")
lbl = tk.Labe(text="こんにちは世界")
lbl.pack()
lbl = tk.Labe(text="初めてのGUIアプリ")
lbl.pack()


root.mainloop()
