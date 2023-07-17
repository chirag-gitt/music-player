import tkinter as tk
import fnmatch
import os
from pygame import mixer
canvas=tk.Tk()
canvas.title("music player")
canvas.geometry("500x500")
canvas.config(bg='black')
root="C:\\music"
pattern="*.mp3"
mixer.init()
prev_b=tk.PhotoImage(file="prev_img.png")
stop_b=tk.PhotoImage(file="stop_img.png")
play_b=tk.PhotoImage(file="play_img.png")
pause_b=tk.PhotoImage(file="pause_img.png")
next_b=tk.PhotoImage(file="next_img.png")
def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(root+"\\"+listBox.get("anchor"))
    mixer.music.play()    
def stop():
    mixer.music.stop()
    listBox.select_clear('active')
def play_next():
    next_song=listBox.curselection()
    next_song=next_song[0]+1
    next_song_name=listBox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(root+"\\"+next_song_name)
    mixer.music.play()   
    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)
def play_prev():
    next_song=listBox.curselection()
    next_song=next_song[0]-1
    next_song_name=listBox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(root+"\\"+next_song_name)
    mixer.music.play()   
    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)
def pause_song():
    if pause["text"]=="pause":
        mixer.music.pause()
        pause["text"]="play"
    else:
        mixer.music.unpause()
        pause["text"]="pause"

listBox=tk.Listbox(canvas,fg="cyan",bg="black",width=100,font=('ds-digital',18));
listBox.pack(padx=15,pady=15)
label=tk.Label(canvas,text='',bg='black',fg='red',font=('ds-digital',18))
label.pack(pady=15)
top=tk.Frame(canvas,bg="black")
top.pack(padx=10,pady=5,anchor='center')
prev=tk.Button(canvas,text="previous",image=prev_b,bg='black',borderwidth=0,command=play_prev)
prev.pack(pady=15,in_=top,side='left')
stop=tk.Button(canvas,text="stop",image=stop_b,bg='black',borderwidth=0,command=stop)
stop.pack(pady=15,in_=top,side="left")
play=tk.Button(canvas,text="previous",image=play_b,bg='black',borderwidth=0,command=select)
play.pack(pady=15,in_=top,side='left')
pause=tk.Button(canvas,text="previous",image=pause_b,bg='black',borderwidth=0,command=pause_song)
pause.pack(pady=15,in_=top,side='left')
next=tk.Button(canvas,text="previous",image=next_b,bg='black',borderwidth=0,command=play_next)
next.pack(pady=15,in_=top,side='left')
for root,dirs,files in os.walk(root):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert('end',filename)
 

canvas.mainloop()


