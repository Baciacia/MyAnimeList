import socket,time
import tkinter as tk
import pickle
import json
import requests


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",1234))
    

def ShowWatched(event):
    command = 'tabW'
    command_bytes = command.encode('utf-8')
    s.send(command_bytes)
    win2 = tk.Toplevel()
    win2.title('Watched Animes')
    win2.geometry('450x450')
    txt = tk.Text(master = win2, width= 42, height= 22)
    deleteBt = tk.Button(master=win2, text= 'Delete List')
    ans = s.recv(10000).decode('utf-8')
    print(ans)
    txt.delete('1.0', tk.END)
    txt.insert('1.0',ans)
    txt.pack(pady = 10)
    deleteBt.pack(pady = 10)
    deleteBt.bind('<Button-1>', lambda event: deleteListW(event, txt))
    
def ShowLater(event):
    command = 'tabL'
    command_bytes = command.encode('utf-8')
    s.send(command_bytes)
    win2 = tk.Toplevel()
    win2.title('Watch Later Animes')
    win2.geometry('450x450')
    deleteBt = tk.Button(master=win2, text= 'Delete List')
    txt = tk.Text(master = win2, width= 42, height= 22)
    ans = s.recv(10000).decode('utf-8')
    print(ans)
    txt.delete('1.0', tk.END)
    txt.insert('1.0',ans)
    txt.pack(pady = 10)
    deleteBt.pack(pady = 10)
    deleteBt.bind('<Button-1>', lambda event: deleteListL(event, txt))

def deleteListW(event,txt):
    command = 'deleteW'
    command_bytes = command.encode('utf-8')
    s.send(command_bytes)
    ans = s.recv(10000).decode('utf-8')
    txt.delete('1.0', tk.END)
    txt.insert('1.0',ans)
    print('delte')

def deleteListL(event,txt):
    command = 'deleteL'
    command_bytes = command.encode('utf-8')
    s.send(command_bytes)
    ans = s.recv(10000).decode('utf-8')
    txt.delete('1.0', tk.END)
    txt.insert('1.0',ans)
    print('delte')


def IdToNames(event):
    pass

def BackButton(event):
    pass

def FilterButton(event):
    pass

def printAnswer2(response):
    AnswerAction.delete('0', tk.END)
    AnswerAction.insert(0, response)

def AddToWatched(event):
    info = responseText.get("1.0","end-1c")
    if len(info) > 30:
        info_data = info + "addW"
        info_data_bytes = info_data.encode('utf-8')
        s.send(info_data_bytes)
        time.sleep(0.5)
        serverResponse = s.recv(1000).decode('utf-8')
        printAnswer2(serverResponse)
    else: pass

def AddToWatchLater(event):
    info = responseText.get("1.0","end-1c")
    if len(info) > 30:
        info_data = info + "addL"
        info_data_bytes = info_data.encode('utf-8')
        s.send(info_data_bytes)
        time.sleep(0.5)
        serverResponse = s.recv(1000).decode('utf-8')
        printAnswer2(serverResponse)
    else:pass

def AddToPref(event):
    info = responseText.get("1.0","end-1c")
    if len(info) > 30:
        info_data = info + "addP"
        info_data_bytes = info_data.encode('utf-8')
        s.send(info_data_bytes)
        time.sleep(0.5)
        serverResponse = s.recv(1000).decode('utf-8')
        printAnswer2(serverResponse)
    else:pass

def ButtonClick(event):
    text = searchBar.get()
    if text == 'exit':
        s.close()
    text_bytes = text.encode('utf-8')
    s.send(text_bytes)
    time.sleep(1)
    serverResponse = s.recv(10000).decode("UTF-8")
    printAnswer(serverResponse)
    if len(serverResponse) < 30:
        addButton['state'] = tk.DISABLED
        laterButton['state'] = tk.DISABLED
        favButton['state'] = tk.DISABLED
    else:
        addButton['state'] = tk.NORMAL
        laterButton['state'] = tk.NORMAL
        favButton['state'] = tk.NORMAL


def printAnswer(response):
    responseText.delete("1.0",tk.END)
    responseText.insert("1.0", response)


window = tk.Tk()
window.title('MyAnimes')
window.resizable(False, False)
window.geometry("600x630")
TitleFrame = tk.Frame()
SeachFrame = tk.Frame()
ButtonFrame = tk.Frame()
ResponseFrame = tk.Frame()
BottomButtonsFrame = tk.Frame()
AnswerActionFrame = tk.Frame()
DBButtonsFrame = tk.Frame()

titleLabel = tk.Label(master = TitleFrame,text = "Search an Anime",width=300, height=5)
searchButton = tk.Button(master = ButtonFrame,text = "Search")
searchBar = tk.Entry(master = SeachFrame)
responseText = tk.Text(master = ResponseFrame, width= 60, height=18)
addButton = tk.Button(master = BottomButtonsFrame, text = "Add to watched")
laterButton = tk.Button(master = BottomButtonsFrame, text = "Watch later")
favButton = tk.Button(master = BottomButtonsFrame, text = "Add to favorites")
AnswerAction = tk.Entry(master = AnswerActionFrame,width= 70)
showWatchedButton = tk.Button(master = DBButtonsFrame, text = "Show Watched Animes")
showLaterAction = tk.Button(master = DBButtonsFrame, text = "Show watch later animes")

TitleFrame.pack()
SeachFrame.pack()
ButtonFrame.pack()
ResponseFrame.pack()
BottomButtonsFrame.pack()
AnswerActionFrame.pack()
DBButtonsFrame.pack()

searchBar.pack()
searchButton.pack(pady=10)
titleLabel.pack()
responseText.pack(pady=15)
addButton.pack(side=tk.LEFT,padx=10,pady=10)
laterButton.pack(side=tk.LEFT,padx=10,pady=10)
favButton.pack(side=tk.LEFT,padx=10,pady=10)
AnswerAction.pack(pady=10)
showWatchedButton.pack(side=tk.LEFT,pady=10,padx=10)
showLaterAction.pack(side=tk.LEFT,pady=10,padx=10)


searchButton.bind("<Button-1>", ButtonClick)
addButton.bind("<Button-1>", AddToWatched)
favButton.bind("<Button-1>", AddToPref)
laterButton.bind("<Button-1>", AddToWatchLater)
showWatchedButton.bind("<Button-1>", ShowWatched)
showLaterAction.bind("<Button-1>", ShowLater)

window.mainloop()
   