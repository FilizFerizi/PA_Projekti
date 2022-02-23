from asyncio.windows_events import NULL
from fileinput import filename
import multiprocessing
from multiprocessing import pool
import os
from pathlib import Path
from random import random
from time import sleep,ctime
import time
from turtle import width
from unicodedata import name
from PIL import Image
from urllib import response
from numpy import where
import requests
from scipy.__config__ import show
from tabulate import tabulate
from functools import partial
from multiprocessing.dummy import Pool, Process
from ast import arg

from controllers.Controller import Cotroller


def download_multi(url,name, path):
         
    response = requests.get(url, stream=True)
    file_name = url.split('/')[-1]
    filename=name
    r=random()
    file = open(path+filename+".jpg", "wb")
    file.write(response.content)

    file.close()
    print(file_name, "DONE!" +" MULTIPROCCESING")
    print("Shkarkimi për linkun  përfundoi në", ctime())
    
    
def thumbnail(url,name,resize,resizeName, path):

        response = requests.get(url, stream=True)
        file_name = url.split('/')[-1]
        filename=name
        file = open(path+filename+".jpg", "wb")
        
        file.write(response.content)
        file.close()
        # print(file)
        image = Image.open(path+filename+".jpg")
        
        image.show()
        width=int(resize)
        h=int(resize)
        imageName=name
      
        img=image.resize((int(image.width/width),int(image.height/h)))
        nameR=resizeName
        r=random()
        img.save(f"{path}{imageName}{nameR}{r}.jpg")
        print(img.width,img.height)
        img.show()
        print("Shkarkimi për linkun  përfundoi në", ctime())

def thumb(name,resize,resizeName, path):

        im = Image.open(path+name+".jpg")
        im.show()
        width=int(resize)
        # print(width)
        # h=int(resize)
        # print(h)
        imageName=resizeName
        print(imageName)
        # //mi cek sa her don mi zvoglu foton
        img=im.resize((int(im.width/width),int(im.height/width)))
        img.save(f"{path}{imageName}.jpg")
        print("Shkarkimi për linkun  përfundoi në", ctime())


class ImageController(Cotroller):
    task_number = 0

    def create_new(self, action):
        max_links= int(10)

        while True:
            task_number = int(input(f"Sa foto deshironi ti shkarkoni? Maximum  {max_links}: "))
            if task_number and 1 <= task_number <= max_links:
                break
            else:
                print("Vlera qe keni dhene nuk eshte valide. Ju lutem provoni perseri!")

        path = input("Shkruani lokacionin e folderit ku deshironi ti ruani fotot: ")
        while not os.path.isdir(path):
            path = input("Lokacioni i dhene nuk egziston! Shkruani lokacionin e folderit ku doni ti ruani fotot: ")

        print("Fotot do te ruhen ne lokacionin {} ".format(path))
        dics = {}
        task_index: int = 0
        for task in range(task_number):
            while True:
                if action==1:
                    images_link= str(input(f"Shkruaj linkun e fotos: "))
                    iamges_name= str(input(f"Shkruaj emrin e fotos se si deshironi ta ruani: "))
                    resize_number=0
                    resize_name=NULL
                elif( action==3):
                    images_link= str(input(f"Shkruaj linkun e fotos: "))
                    iamges_name= str(input(f"Shkruaj emrin e fotos se si deshironi ta ruani: "))
                    resize_number= int(input(f"Shkruaj sa here deshironi ta zvogeloni foton: "))
                    resize_name=input(f"shrkuaj emrin e fotos se zvogeluar")
                elif(action==2):
                    images_link=NULL
                    iamges_name= str(input(f"Shkruaj emrin e fotos qe deshironi ta zvogeloni: "))
                    resize_number= int(input(f"Shkruaj sa here deshironi ta zvogeloni foton: "))
                    resize_name=input(f"shrkuaj emrin e fotos se zvogeluar")
               
                if images_link and iamges_name:
                    dics[task_index] = {
                        "url": images_link,
                        "name": iamges_name,
                        "resize": resize_number,
                        "resizeName":resize_name,
                    }
                    task_index = task_index + 1
                    break
                else:
                    print(f"Shkruaj nje vlere valide per taskun {task_index}")

        headers = ["Indeksi i Taskut", "Informatat e dhena"]
        print(tabulate(dics.items(), headers=headers,tablefmt="fancy_grid"))
        print("Filloi marrja e fotove...")
       
        processes=[]
        for i in range(0, task_number):
            if action == 1:
                # print(i)
                # print("MULTIPROCESING PROCESSES")
                p=multiprocessing.Process(target=download_multi, args=(dics[i]['url'], dics[i]['name'],path))
            
                processes.append(p)
                
                
            elif action == 2:
                p=multiprocessing.Process(target=thumb, args=(dics[i]['name'],dics[i]['resize'],dics[i]['resizeName'],path))
                processes.append(p)
                
                
            elif action == 3:     
                p=multiprocessing.Process(target=thumbnail, args=(dics[i]['url'], dics[i]['name'],dics[i]['resize'],dics[i]['resizeName'],path))
                processes.append(p)
                
                
                
            
            # print(toc-tic)
            print("Shkarkimi filloi për linkun ", i + 1, " koha: ", ctime(), )
            processes[i].start()   
            
        for i in range(0, task_number):
            processes[i].join()
            print("Shkarkimi filloi për linkun " + str(toc-tic))
        # for process in processes:
        #     process.join()
        print("Ruajtja e Fotove perfundoi.")       
               
               

#TODO: shtohet foto