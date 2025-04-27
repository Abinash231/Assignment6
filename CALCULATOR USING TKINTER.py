import tkinter as tk
from tkinter import messagebox

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            entry.delete(0, tk.END)
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief="ridge", justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]
for row in buttons:
    btn_row = tk.Frame(button_frame)
    btn_row.pack(expand=True, fill="both")
    for btn_text in row:
        button = tk.Button(
            btn_row, text=btn_text, font="Arial 18", relief="groove",
            border=1, width=5, height=2
        )
        button.pack(side="left", expand=True, fill="both")
        button.bind("<Button-1>", click)
root.mainloop()
