import tkinter.messagebox
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import time
from mutagen.mp3 import MP3

from pygame import mixer

mixer.init()


class MusicPlayer:
    def __init__(self, Tk):
        self.window = Tk
        self.window.title('Music Player')
        self.window.geometry('400x500')
        self.window.resizable(0, 0)

        # menu bar
        def changeImg():
            image = Image.open('images/music2.jpg')
            image = image.resize((400, 210), Image.Resampling.LANCZOS)
            self.musicImage = ImageTk.PhotoImage(image)
            (Label(self.window, image=self.musicImage, width=300, height=200)
             .place(x=50, y=80))

        def currMusic():
            self.heading['text'] = '🎵Current track: ' + os.path.basename(fileName)

        def openFile():
            global fileName
            fileName = filedialog.askopenfilename()
            currMusic()
            changeImg()

        def saveFile():
            pass

        self.menubar = Menu(self.window, tearoff=False)
        self.window.config(menu=self.menubar)

        self.submenu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label='File', menu=self.submenu)
        self.submenu.add_command(label='Open', command=openFile)
        self.submenu.add_command(label='Save', command=saveFile)

        self.submenu2 = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='About', menu=self.submenu2)
        self.submenu2.add_command(label='Help')

        # label
        self.topLabel = Label(self.window, text='Play your favourite tracks from downloads',
                              font=('Arial', 12, 'normal')
                              , bg='black', fg='white')
        self.topLabel.pack(side=TOP, fill=X)

        # self.topLabel = Label(self.window, text='  ', bg='black', fg='white')
        # self.topLabel.pack(side=LEFT, fill=Y)
        # self.topLabel = Label(self.window, text='  ', bg='black', fg='white')
        # self.topLabel.pack(side=RIGHT, fill=Y)

        self.heading = Label(text='Play Your Track 🎶', font=('Arial', 15, 'bold'))
        self.heading.place(x=50, y=40)

        # bottom
        self.label1 = Label(self.window, text="Listen Your Favourite Track.", bg='black', fg='white'
                            , font=('Arial', 15, 'bold'))
        self.label1.pack(side=BOTTOM, fill=X)

        # for image
        image = Image.open('images/music.jpg')
        image = image.resize((400, 210), Image.Resampling.LANCZOS)
        self.musicImage = ImageTk.PhotoImage(image)
        (Label(self.window, image=self.musicImage, width=300, height=200, background='black')
         .place(x=50, y=80))

        # function

        def playMusic():

            try:
                paused
            except NameError:
                try:
                    lengthBar()
                    mixer.music.load(fileName)
                    mixer.music.play()
                    self.label1['text'] = 'Playing track...'

                except:
                    tkinter.messagebox.showerror('Error', 'Open the correct music file..')
            else:
                mixer.music.unpause()
                self.label1['text'] = 'Music Unpause..'

        def stopMusic():
            mixer.music.stop()
            self.label1['text'] = 'Music Stopped'

        def pauseMusic():
            global paused
            paused = TRUE
            mixer.music.pause()
            self.label1['text'] = 'Music Paused'

        def Volume(vol):
            volume = int(vol) / 100
            mixer.music.set_volume(volume)

        def mute():
            self.scale.set(0)
            mute_im = Image.open('images/mute.png')
            mute_im = mute_im.resize((25, 25), Image.Resampling.LANCZOS)
            self.muteImg = ImageTk.PhotoImage(mute_im)
            Button(self.window, image=self.muteImg, command=unMute).place(x=115, y=410)

        def unMute():
            self.scale.set(50)
            vol_im = Image.open('images/volume-up-interface-symbol.png')
            vol_im = vol_im.resize((25, 25), Image.Resampling.LANCZOS)
            self.volImg = ImageTk.PhotoImage(vol_im)
            Button(self.window, image=self.volImg, command=mute).place(x=115, y=410)

        def lengthBar():
            current_time = mixer.music.get_pos() / 1000
            convert_currTime = time.strftime('%M:%S', time.gmtime(current_time))
            song = MP3(fileName)
            song_len = song.info.length
            curr_song_len = time.strftime('%M:%S', time.gmtime(song_len))
            self.sLength.config(text=f'Song length - {convert_currTime} -> {curr_song_len}')
            self.sLength.after(1000, lengthBar)

        # Song length bar
        self.sLength = Label(self.window, text='Song length - 00:00', font=('Arial', 15, 'normal'))
        self.sLength.place(x=100, y=295)

        # play and pause button
        play_im = Image.open('images/play-button.png')
        play_im = play_im.resize((40, 40), Image.Resampling.LANCZOS)
        self.play_button = ImageTk.PhotoImage(play_im)
        (Button(self.window, image=self.play_button, bd=0, bg='white', command=playMusic)
         .place(x=110, y=340))

        pause_im = Image.open('images/video-pause-button.png')
        pause_im = pause_im.resize((40, 40), Image.Resampling.LANCZOS)
        self.pause_button = ImageTk.PhotoImage(pause_im)
        (Button(self.window, image=self.pause_button, bd=0, bg='white', command=pauseMusic)
         .place(x=180, y=340))

        stop_im = Image.open('images/stop-button.png')
        stop_im = stop_im.resize((40, 40), Image.Resampling.LANCZOS)
        self.stop_button = ImageTk.PhotoImage(stop_im)
        (Button(self.window, image=self.stop_button, bd=0, bg='white', command=stopMusic)
         .place(x=245, y=340))

        # Volume bar
        vol_im = Image.open('images/volume-up-interface-symbol.png')
        vol_im = vol_im.resize((25, 25), Image.Resampling.LANCZOS)
        self.volImg = ImageTk.PhotoImage(vol_im)
        Button(self.window, image=self.volImg, command=mute).place(x=115, y=410)

        self.scale = Scale(self.window, from_=0, to=100, orient=HORIZONTAL, length=130, command=Volume)
        self.scale.set(50)
        self.scale.place(x=150, y=400)


window = Tk()
object1 = MusicPlayer(window)

window.mainloop()
