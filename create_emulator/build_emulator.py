import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
import re
import subprocess

window = tk.Tk()
devices = []
emulator = []
emulatorInstall = []
selectAndroidUser = StringVar()
nameEmulator = StringVar()
nameEmulatorSelectUser = StringVar()

def open_view():
    window.geometry('500x400')
    window.resizable(False, False)
    #window.iconbitmap(r'C:\script\open_db\icon.ico')
    window.title('Manipular arquivo')

    label = ttk.Label(window, text='Selecione o android')
    label.place(x=10, y=10)

    combo = ttk.Combobox(values=devices, width=55)
    combo.bind("<<ComboboxSelected>>", selection_changed)
    combo.place(x=10, y=30) 

    labelDevice = ttk.Label(window, text="Nome do emulador")
    labelDevice.place(x=10, y=60)

    nameDevice = ttk.Entry(window, textvariable=nameEmulator, width=56)
    nameDevice.place(x=10, y=80)

    change_button = ttk.Button(text="Criar emulador", command=build_emulator)
    change_button.place(x=10, y=120)

    change_button = ttk.Button(text="Listar emulator", command=list_emulator)
    change_button.place(x=10, y=160)

    window.mainloop()

def build_emulator():
    emulator.clear()

    for item in selectAndroidUser.get().split(';'):
        emulator.append(item)

    proc = subprocess.run(["/home/user/script/create_emulator/command.sh 2 %s %s %s %s %s"% (nameEmulator.get(), emulator[0], emulator[1], emulator[2], emulator[3])], shell=True)

def selection_changed(event):
    selectAndroidUser.set(event.widget.get())

def list_emulator():
    proc = subprocess.run(["/home/user/script/create_emulator/command.sh 3"], shell=True)
    list_emulator_user()

def build_list():
    devices.clear()
    with open("/home/user/script/create_emulator/list_android.txt", "r") as arquivo:
        device = arquivo.read()

    for item in device.split():
        result = re.search("[system]+[-]+[images]+[;]+[android]+[-]+([0-9]{1,})+[;][a-z]+[;]+[x]+[0-9]{1,}", item)
        if result != None:
            devices.append(item)

def list_emulator_user():
    emulatorInstall.clear()
    with open("/home/user/script/create_emulator/emulator.txt", "r") as arquivo:
        emulator = arquivo.read()

    for item in emulator.split():
        emulatorInstall.append(item)

    create_combo_emulator()

def create_combo_emulator():
    combo = ttk.Combobox(values=emulatorInstall, width=55)
    combo.bind("<<ComboboxSelected>>", selection_changed_emulator)
    combo.place(x=10, y=200)
    create_button_delete()

def create_button_delete():
    change_button = ttk.Button(text="Deletar emulator", command=delete_emulator)
    change_button.place(x=10, y=230)

def selection_changed_emulator(event):
    nameEmulatorSelectUser.set(event.widget.get())

def delete_emulator():
    proc = subprocess.run(["/home/user/script/create_emulator/command.sh 4 %s"% (nameEmulatorSelectUser.get())], shell=True)
    

build_list()
open_view()

