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
#import selecting
# obtain audio from the microphone
def func():
        r = sr.Recognizer()
        isl_gif=['tienes preguntas', 'estás molesto', 'estás ocupada', 'tienes hambre', 'estás enfermo', 'ten cuidado',
                'nos podemos encontrar mañana', 'ya compraste los boletos', 'terminaste tus asignaciones', 'fuiste a la oficina', 'tienes dinero',
                'deseas algo para beber', 'deseas té o café', 'ves televisión', 'no te preocupes', 'la flor es bella',
                'buenas tardes', 'buenas noches', 'buenos días', 'felicidades', 'buena pregunta', 'comiste almuerzo', 'buen viaje',
                'hola, ¿cuál es tu nombre?', 'cuántas personas tienes en tu familia', 'trabajo en la oficina', 'estoy aburrido', 
                'estoy bien', 'perdón', 'estoy pensando', 'estoy cansado', 'no entiendo nada', 'voy al cine', 'me gusta ir a las tiendas',
                'tuve que decir algo pero se me olvidó', 'tengo dolor de cabeza', 'me gusta el color rosa', 'vivo en Nagpur', 'vamos a almorzar', 'mi madre es ama de casa',
                'me llamo Johnny', 'mucho gusto en conocerte', 'por favor no fumar', 'abre la puerta', 'llámame después',
                'por favor limpia la habitación', 'por favor dame tu bolígrafo', 'por favor usa el bote de basura, no tires basura', 'por favor espera un momento', 'puedo ayudarte?',
                'podemos ir juntos mañana?', 'intérprete de lenguaje de señas', 'siéntate', 'levántate', 'cuídate', 'hubo un atasco de tráfico', 'espera, estoy pensando',
                'qué estás haciendo?', 'cuál es el problema?', 'cuál es la fecha de hoy?', 'qué hace tu padre?', 'cuál es tu trabajo?',
                'cuál es tu número de móvil?', 'cuál es tu nombre?', 'qué tal?', 'cuándo es tu entrevista?', 'cuándo iremos?', 'dónde vives?',
                'dónde está el baño?', 'dónde está la comisaría?', 'estás equivocado','dirección','agra','ahemdabad', 'todo', 'abril', 'assam', 'agosto', 'australia', 'badoda', 'plátano', 'banaras', 'banglore',
                'bihar','bihar','puente','gato', 'chandigarh', 'chennai', 'navidad', 'iglesia', 'clínica', 'coco', 'cocodrilo','dasara',
                'sordo', 'diciembre', 'ciervo', 'delhi', 'dólar', 'pato', 'febrero', 'viernes', 'frutas', 'vaso', 'uvas', 'gujarat', 'hola',
                'hindú', 'hyderabad', 'india', 'enero', 'jesús', 'trabajo', 'julio', 'julio', 'karnataka', 'kerala', 'krishna', 'litro', 'mango',
                'mayo', 'milla', 'lunes', 'mumbai', 'museo', 'musulmán', 'nagpur', 'octubre', 'naranja', 'pakistan', 'pase', 'comisaría de policía',
                'oficina de correos', 'pune', 'punjab', 'rajastán', 'ram', 'restaurante', 'sábado', 'septiembre', 'tienda', 'dormir', 'sudáfrica',
                'historia', 'domingo', 'tamil nadu', 'temperatura', 'templo', 'jueves', 'baño', 'tomate', 'ciudad', 'martes', 'ee.uu.', 'pueblo',
                'voz', 'miércoles', 'peso','por favor espera un momento','cuál es tu número de móvil','qué estás haciendo','estás ocupado']
        
        
        arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z']
        with sr.Microphone() as source:
                # image   = "signlang.png"
                # msg="HEARING IMPAIRMENT ASSISTANT"
                # choices = ["Live Voice","All Done!"] 
                # reply   = buttonbox(msg,image=image,choices=choices)
                r.adjust_for_ambient_noise(source) 
                i=0
                while True:
                        print("I am Listening")
                        audio = r.listen(source)
                        # recognize speech using Sphinx
                        try:
                                a=r.recognize_google(audio)
                                a = a.lower()
                                print('You Said: ' + a.lower())
                                
                                for c in string.punctuation:
                                    a= a.replace(c,"")
                                    
                                if(a.lower()=='goodbye' or a.lower()=='good bye' or a.lower()=='bye'):
                                        print("oops!Time To say good bye")
                                        break
                                
                                elif(a.lower() in isl_gif):
                                    
                                    class ImageLabel(tk.Label):
                                            """a label that displays images, and plays them if they are gifs"""
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
                                    lbl = ImageLabel(root)
                                    lbl.pack()
                                    lbl.load(r'ISL_Gifs/{0}.gif'.format(a.lower()))
                                    root.mainloop()
                                else:
                                    for i in range(len(a)):
                                                    if(a[i] in arr):
                                            
                                                            ImageAddress = 'letters/'+a[i]+'.jpg'
                                                            ImageItself = Image.open(ImageAddress)
                                                            ImageNumpyFormat = np.asarray(ImageItself)
                                                            plt.imshow(ImageNumpyFormat)
                                                            plt.draw()
                                                            plt.pause(0.8)
                                                    else:
                                                            continue

                        except:
                               print(" ")
                        plt.close()
while 1:
  image   = "signlang.png"
  msg="HEARING IMPAIRMENT ASSISTANT"
  choices = ["Live Voice","All Done!"] 
  reply   = buttonbox(msg,image=image,choices=choices)
  if reply ==choices[0]:
        func()
  if reply == choices[1]:
        quit()
