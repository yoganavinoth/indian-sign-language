import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string

def func():
    r = sr.Recognizer()
    isl_gif = [
        'any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
        'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office',
        'do you have money', 'do you want something to drink', 'do you want tea or coffee', 'do you watch TV',
        'dont worry', 'flower is beautiful', 'good afternoon', 'good evening', 'good morning', 'good night',
        'good question', 'had your lunch', 'happy journey', 'hello what is your name',
        'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing', 'i am fine',
        'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre',
        'i love to shop', 'i had to say something but i forgot', 'i have headache', 'i like pink colour',
        'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker', 'my name is john',
        'nice to meet you', 'no smoking please', 'open the door', 'please call me later', 'please clean the room',
        'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime',
        'shall I help you', 'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up',
        'take care', 'there was traffic jam', 'wait I am thinking', 'what are you doing', 'what is the problem',
        'what is todays date', 'what is your father do', 'what is your job', 'what is your mobile number',
        'what is your name', 'whats up', 'when is your interview', 'when we will go', 'where do you stay',
        'where is the bathroom', 'where is the police station', 'you are wrong', 'address', 'agra', 'ahemdabad',
        'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore', 'bihar',
        'bridge', 'cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile', 'dasara',
        'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes',
        'gujrat', 'hello', 'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'karnataka', 'kerala',
        'krishna', 'litre', 'mango', 'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october',
        'orange', 'pakistan', 'pass', 'police station', 'post office', 'pune', 'punjab', 'rajasthan', 'ram',
        'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica', 'story', 'sunday', 'tamil nadu',
        'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village', 'voice',
        'wednesday', 'weight'
    ]

    arr = list(string.ascii_lowercase)

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True:
            print("I am Listening")
            audio = r.listen(source)
            try:
                a = r.recognize_google(audio)
                a = a.lower()
                print('You Said: ' + a)

                for c in string.punctuation:
                    a = a.replace(c, "")

                if a in ['goodbye', 'good bye', 'bye']:
                    print("Oops! Time to say goodbye")
                    break

                elif a in isl_gif:
                    class ImageLabel(tk.Label):
                        def load(self, im):
                            if isinstance(im, str):
                                im = Image.open(im)
                            self.loc = 0
                            self.frames = []

                            try:
                                for i in count(1):
                                    self.frames.append(ImageTk.PhotoImage(im.copy()))
                                    im.seek(i)
                            except EOFError:
                                pass

                            try:
                                self.delay = im.info['duration']
                            except:
                                self.delay = 100

                            if len(self.frames) == 1:
                                self.config(image=self.frames[0])
                            else:
                                self.next_frame()

                        def unload(self):
                            self.config(image=None)
                            self.frames = None

                        def next_frame(self):
                            if self.frames:
                                self.loc += 1
                                self.loc %= len(self.frames)
                                self.config(image=self.frames[self.loc])
                                self.after(self.delay, self.next_frame)

                    root = tk.Tk()
                    root.title("ISL GIF Viewer")
                    root.state('zoomed')  # Maximize the window (title bar will be visible)
                    root.bind("<Escape>", lambda e: root.destroy())  # Close on Esc key

                    lbl = ImageLabel(root)
                    lbl.pack()
                    gif_path = f'ISL_Gifs/{a}.gif'
                    if os.path.exists(gif_path):
                        lbl.load(gif_path)
                        root.mainloop()
                    else:
                        print("GIF file not found:", gif_path)
                else:
                    for char in a:
                        if char in arr:
                            image_path = f'letters/{char}.jpg'
                            if os.path.exists(image_path):
                                img = Image.open(image_path)
                                plt.imshow(np.asarray(img))
                                plt.axis('off')
                                plt.draw()
                                plt.pause(0.8)
                            else:
                                print("Letter image not found:", image_path)
                    plt.close()

            except Exception as e:
                print("Could not understand, please speak again.")

while True:
    image = "signlang.png"
    msg = "HEARING IMPAIRMENT ASSISTANT"
    choices = ["Live Voice", "All Done!"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == choices[0]:
        func()
    if reply == choices[1]:
        break