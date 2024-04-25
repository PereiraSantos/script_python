import tkinter as tk
import os
from tkinter import ttk
from tkinter import filedialog
from tkinter import StringVar
from tkinter import IntVar
from tkinter.filedialog import askopenfilename

window = tk.Tk()

emuladors = []
devices = []
projectList = []
databaseList = []
sharedList = []
typeTask = [("Enviar para download", 1),("Enviar para database", 2), ("Enviar para shared preference", 3), ("Puxa para pasta local", 4)]

checkbuttonValue = tk.BooleanVar(value=True)

task = IntVar()

selectProjectUser = StringVar()
selectDatabaseUser = StringVar()
selectSharedUser = StringVar()
device = StringVar()

folder = StringVar(value="Nenhum arquivo selecionado.")
buttonSelect = StringVar(value="Selecionar pasta")
buttonConclud = StringVar(value="Concluir")
buttonReset = StringVar(value="Resetar")


def init_view():
    window.geometry('550x240')
    window.resizable(False, False)
    window.iconbitmap(r'icon\icon.ico')
    window.title('Manipular arquivo')

    label = ttk.Label(window, text='Selecione o aparelho')
    label.place(x=10, y=10)

    combo = ttk.Combobox(values=devices)
    combo.bind("<<ComboboxSelected>>", selection_changed)
    combo.place(x=10, y=30, width=200)   

    ckeck_type_arquive =  ttk.Label(window, text="Selecione a acão")
    ckeck_type_arquive.place(x=10, y=60)

    i = 60
    for tasklist, val in typeTask:
        i = i + 20
        project_radio = ttk.Radiobutton(window, 
            text=tasklist,
            variable=task, 
            command=select_task,
            value=val)
        project_radio.place(x=10, y=i)

    change_button = ttk.Button(textvariable=buttonSelect,command=open_folder)
    change_button.place(x=10, y=170)

    label_folder = ttk.Label(window, textvariable=folder)
    label_folder.place(x=10, y=195)

    change_button = ttk.Button(textvariable=buttonConclud, command=load_database_device)
    change_button.place(x=445, y=170)

    change_button = ttk.Button(textvariable=buttonReset, command=reset)
    change_button.place(x=350, y=170)

    window.mainloop()

def reset():
    folder.set('Nenhum arquivo selecionado.')
    buttonReset.set("Resetado")
    buttonConclud.set("Concluir")

def build_combo_database(disabled):
    ckeck_database =  ttk.Label(window, text="Selecione o banco")
    ckeck_database.place(x=220, y=55)
    
    combo_database = ttk.Combobox(values=databaseList, state=disabled)
    combo_database.bind("<<ComboboxSelected>>", selection_database)
    combo_database.place(x=220, y=75, width=300)

def build_combo_shared(disabled):
    ckeck_database =  ttk.Label(window, text="Selecione o shared")
    ckeck_database.place(x=220, y=100)
    
    combo_database = ttk.Combobox(values=sharedList, state=disabled)
    combo_database.bind("<<ComboboxSelected>>", selection_shared)
    combo_database.place(x=220, y=120, width=300)

def select_task():
    buttonSelect.set("Selecionar arquivo")
    folder.set('Nenhum arquivo selecionado.')

    if task.get() == 1:
        show_select_project('disabled')
        build_combo_database('disabled')
        build_combo_shared('disabled')
    elif task.get() == 2:
        show_select_project('normal')
        build_combo_database('disabled')
        build_combo_shared('disabled')
    elif task.get() == 3:
        show_select_project('normal')
        build_combo_database('disabled')
        build_combo_shared('disabled')
    else:
        buttonSelect.set("Selecionar pasta")
        folder.set('Nenhum arquivo selecionado.')
        show_select_project('normal')

def show_select_project(disabled):
    ckeck_project =  ttk.Label(window, text="Selecione o projeto")
    ckeck_project.place(x=220, y=10)
    
    combo_project = ttk.Combobox(values=projectList, state=disabled)
    combo_project.bind("<<ComboboxSelected>>", selection_project)
    combo_project.place(x=220, y=30, width=300)

def open_folder():
    buttonReset.set("Resetar")
    if task.get() != 4:
        filename = askopenfilename() 
        folder.set('Enviar '+filename)
    else:
        filepath = filedialog.askdirectory(parent=window, initialdir="/",title ='Selecione a pasta')
        folder.set('Salvar em '+filepath)

    clean_log()

def checkbutton_clicked():
    checkbuttonValue.get()

def selection_changed(event):
    connect_device(event.widget.get())

def selection_project(event):
    selectProjectUser.set(event.widget.get())
    if task.get() == 4:
        list_database_project()
        list_shared_project()        

def selection_database(event):
    selectDatabaseUser.set(event.widget.get())

def selection_shared(event):
    selectSharedUser.set(event.widget.get())

def load_database_device():
    clean_log()

    if checkbuttonValue.get() == True and task.get() == 4:
        if device.get() == '': 
            folder.set("SEM DEVICE SELECIONADO!!!!!!!!!!!!!!!!!!")
            return
        
        if selectProjectUser.get() == '': 
            folder.set("SEM PROJETO SELECIONADO!!!!!!!!!!!!!!!!!!")
            return
        
        if folder.get().count('Salvar') == 0: 
            folder.set("SEM PASTA SELECIONADO!!!!!!!!!!!!!!!!!!")
            return
        
        if selectDatabaseUser.get() != '': 
            cmd = 'comm\command.bat 3 '+device.get() +' '+selectProjectUser.get()+' '+selectDatabaseUser.get() +' '+folder.get().replace('Salvar em ','') + ''
            os.system(cmd)
        
        if selectSharedUser.get() != '': 
            cmdShared = 'comm\command.bat 8 '+device.get() +' '+selectProjectUser.get()+' '+selectSharedUser.get() +' '+folder.get().replace('Salvar em ','') + ''
            os.system(cmdShared)
    elif checkbuttonValue.get() == True and task.get() == 1:
        if device.get() != '' and folder.get().count('Enviar'):
            cmd = 'comm\command.bat 5 '+device.get() +' '+folder.get().replace('Enviar ','') +''
            os.system(cmd)
        else:
            if device.get() == '':  
                folder.set("SEM DEVICE SELECIONADO!!!!!!!!!!!!!!!!!!")
            if folder.get().count('Enviar') == 0: 
                folder.set("SEM PASTA!!!!!!!!!!!!!!!!!!")
            
            return
    elif checkbuttonValue.get() == True and task.get() == 2:
        if selectProjectUser.get() != '' and device.get() != '' and folder.get().count('Enviar'):
            cmd = 'comm\command.bat 9 '+device.get() +' '+folder.get().replace('Enviar ','') +' '+selectProjectUser.get() +''
            os.system(cmd)
        else:
            setMessageUser()
            return
    elif checkbuttonValue.get() == True and task.get() == 3:
        if selectProjectUser.get() != '' and device.get() != '' and folder.get().count('Enviar'):
            cmd = 'comm\command.bat 10 '+device.get() +' '+folder.get().replace('Enviar ','') +' '+selectProjectUser.get() +''
            os.system(cmd)
        else:
            setMessageUser()
            return

    buttonConclud.set('Finalisado')
    get_log()

def setMessageUser():
    if device.get() == '':  
        folder.set("SEM DEVICE SELECIONADO!!!!!!!!!!!!!!!!!!")
        return
     
    if selectProjectUser.get() == '': 
        folder.set("SEM PROJETO SELECIONADO!!!!!!!!!!!!!!!!!!")
        return
   
    if folder.get().count('Enviar') == 0: 
        folder.set("SEM PASTA!!!!!!!!!!!!!!!!!!")
    
def get_log():
    with open("text/log.txt", "r") as arquivo:
        logs = arquivo.read()

    folder.set(logs)

def clean_log():
    with open("text\log.txt", "w") as f:
        pass

def list_database_project():
    cmd = 'comm\command.bat 4 '+device.get() +' '+selectProjectUser.get()+''
    os.system(cmd)
    build_database()

def list_shared_project():
    cmd = 'comm\command.bat 7 '+device.get() +' '+selectProjectUser.get()+''
    os.system(cmd)
    build_shared()

def open_adb():
    clean_log()
    cmd = 'comm\command.bat 1'
    os.system(cmd)

    with open("text/temp.txt", "r") as arquivo:
        device = arquivo.read().replace('List of devices attached','').replace('unauthorized','').replace('device','')
        
    for item in device.split():
        devices.append(item)

    if len(devices) == 0:
        folder.set("SEM DEVICE CONECTADO, CONECTE UM DEVICE!!!!!!!!!!!!!!!!!!")
    else:
        cmd = 'adb root'
        os.system(cmd)

def open_project():
    if len(devices) == 0:
        folder.set("SEM DEVICE CONECTADO, CONECTE UM DEVICE!!!!!!!!!!!!!!!!!!")
    else:
        cmd = 'comm\command.bat 2 '+device.get() +' '
        os.system(cmd)

        with open("text/folder.txt", "r") as arquivo:
            project = arquivo.read()
            
        for item in project.split():
            projectList.append(item)

def build_database():
    databaseList.clear()
    with open("text/database.txt", "r") as arquivo:
        database = arquivo.read()
        
    for item in database.split():
        databaseList.append(item)
    
    build_combo_database('normal')
    
def build_shared():
    sharedList.clear()
    with open("text/shared.txt", "r") as arquivo:
        shared = arquivo.read()
        
    for item in shared.split():
        sharedList.append(item)
    
    build_combo_shared('normal')

def connect_device(d):
    cmd = 'adb -s '+ d +' root'
    device.set(d)
    os.system(cmd)
    open_project()

def valid_emulador():
    if len(devices) == 0:
        get_emulator()

def get_emulator():
    cmd = 'comm\emulator.bat 1 '
    os.system(cmd)

    with open("text/emulator.txt", "r") as arquivo:
        emulator = arquivo.read()
            
    for item in emulator.split():
        emuladors.append(item)


open_adb()
valid_emulador()
init_view()
