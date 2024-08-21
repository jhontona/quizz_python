import tkinter as tk
from tkinter import messagebox

quiz_data = {
    1: {
        "question": "¿Cuál es la salida de 'print(2 ** 3)'?",
        "options": ["6", "8", "9", "16"],
        "answer": "8"
    },
    2: {
        "question": "¿Cuáles de las siguientes son tipos de datos en Python?",
        "options": ["int", "float", "list", "integer", "array"],
        "answer": ["int", "float", "list"]
    },
    3: {
        "question": "¿Qué función se usa para obtener la longitud de una lista?",
        "options": ["len()", "length()", "size()", "count()"],
        "answer": "len()"
    }
}

root = tk.Tk()
root.title("Quizz de Python")

var1 = tk.StringVar(value=quiz_data[1]["options"][0])
var2 = [tk.BooleanVar(value=False) for _ in range(5)]
var3 = tk.StringVar(value=quiz_data[3]["options"][0])

def check_answers():
    score = 0

    if var1.get() == quiz_data[1]["answer"]:
        score += 1

    select_options = [quiz_data[2]["options"][i] for i in range(5) if var2[i].get()]
    if sorted(select_options) == sorted(quiz_data[2]["answer"]):
        score += 1

    if var3.get() == quiz_data[3]["answer"]:
        score += 1

    messagebox.showinfo("Resultado", f"Puntaje {score}/3")

tk.Label(root, text=quiz_data[1]["question"], font=('Helvetica', 14)).pack(anchor='w')
for option in quiz_data[1]["options"]:
    tk.Radiobutton(root, text=option, variable=var1, value=option, font=('Helvetica', 12)).pack(anchor='w')

tk.Label(root, text=quiz_data[2]["question"], font=('Helvetica', 14)).pack(anchor='w')
for i, option in enumerate(quiz_data[2]["options"]):
    tk.Checkbutton(root, text=option, variable=var2[i], font=('Helvetica', 12)).pack(anchor='w')

tk.Label(root, text=quiz_data[3]["question"], font=('Helvetica', 14)).pack(anchor='w')
select = tk.OptionMenu(root, var3, *quiz_data[3]["options"])
select.config(width=30, font=('Helvetica', 12))
select.pack(anchor='w')

tk.Button(root, text='Enviar', command=check_answers, font=('Helvetica', 14)).pack()
root.mainloop()