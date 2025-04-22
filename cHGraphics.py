from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import countingHoursTest as cH

def on_calculate_button_click():
    filename = filename_path.get()
    hours_required_value, hours_worked_value, hours_value = cH.process_csv(filename, root)

    hours_required.set(hours_required_value)
    hours_worked.set(hours_worked_value)
    hours.set(hours_value)

def on_button_click():
    selected_file = filedialog.askopenfilename()

    file_entry.delete(0, END)
    file_entry.insert(0, filename_path)

    filename_path.set(selected_file)


root = Tk()
root.title("Counting Hours")
root.geometry("400x350")


filename_path = StringVar()
name = StringVar(value="Jules")
hours_required = StringVar()
hours_worked = StringVar()
hours = StringVar()


mainframe = ttk.Frame(root, padding=10, width=500, height=300)
file_entry = ttk.Entry(mainframe, width=50, textvariable=filename_path)
button_file = ttk.Button(mainframe, text="File", command=on_button_click)
button = ttk.Button(mainframe, text="Calculate", command=on_calculate_button_click)


ttk.Label(mainframe, text="Nome do Arquivo:").grid(column=0, row=0, columnspan=2)
ttk.Label(mainframe, text="Nome:").grid(column=0, row=2, sticky=E)
ttk.Label(mainframe, textvariable=name).grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Horas Necessárias:").grid(column=0, row=3, sticky=E)
ttk.Label(mainframe, textvariable=hours_required).grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Horas Trabalhadas:").grid(column=0, row=4, sticky=E)
ttk.Label(mainframe, textvariable=hours_worked).grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="Saldo:").grid(column=0, row=5, sticky=E)
ttk.Label(mainframe, textvariable=hours).grid(column=1, row=5, sticky=W)


mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
file_entry.grid(column=0, row=1, columnspan=2, sticky=(W, E))
button_file.grid(column=2, row=1, sticky=W)
button.grid(column=0, row=6, columnspan=2)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure((0,1), weight=1)
mainframe.rowconfigure((0,1,2,3,4,5,6), weight=1)

root.mainloop()