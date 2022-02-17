from asyncio.windows_events import NULL
from fileinput import filename
import multiprocessing
from multiprocessing import pool
import os
from pathlib import Path
from time import sleep,ctime
import time
from turtle import width
from PIL import Image
from urllib import response
from numpy import where
import requests
from tabulate import tabulate
from functools import partial
from multiprocessing.dummy import Pool, Process
from ast import arg


def download_multi(dics, path):
    print(len(dics))
    
    for p_id, p_info in dics.items():

        
        # print ("filloj metodat")
        # print("dics id", p_id)
        # print("prinotohet emri i fotos")
        # print(dics[p_id]['name'])
        # for key in p_info:
        #     print(key +":",p_info[key])

        response = requests.get(dics[p_id]['url'], stream=True)
        file_name = dics[p_id]['url'].split('/')[-1]
        filename=dics[p_id]['name']
        file = open(path+filename+".jpg", "wb")
        
        file.write(response.content)
        file.close()


        # image = Image.open(path+filename+'.jpg')
        # # # image = image.convert('L')
        # image.save(path+filename+".jpg")
        print(file_name, "DONE!" +" MULTIPROCCESING")
    
        # thumbnail()








def thumbnail(dics, path):
  for p_id, p_info in dics.items():
        response = requests.get(dics[p_id]['url'])
        file_name = dics[p_id]['url'].split('/')[-1]
        filename=dics[p_id]['name']
        file = open(path+file_name, "wb")
        file.write(response.content)
        file.close()
        # print(file)

        
        
            
        image = Image.open(path+file_name)
        
        image.show()
        width=int(dics[p_id]['resize'])
        h=int(dics[p_id]['resize'])
        imageName=dics[p_id]['name']
        # //mi cek sa her don mi zvoglu foton
        img=image.resize((int(image.width/width),int(image.height/h)))
        img.save(f"{path}{imageName}.jpg")
        print(img.width,img.height)
        img.show()

def thumb(dics, path):
    for p_id, p_info in dics.items():
        im = Image.open(dics[p_id]['url'])
        im.thumbnail(dics[p_id]['resize'])
        im.save(dics[p_id]['name'], ".JPEG")


class ImageController:
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
                images_link= str(input(f"Shkruaj linkun e fotos: "))
                iamges_name= str(input(f"Shkruaj emrin e fotos se si deshironi ta ruani: "))
                if(action==2 or action==3):
                    resize_number= int(input(f"Shkruaj sa here deshironi ta zvogeloni foton: "))
                else:
                    resize_number=0
                
                if images_link and iamges_name:
                    dics[task_index] = {
                        "url": images_link,
                        "name": iamges_name,
                        "resize": resize_number,
                    }
                    task_index = task_index + 1
                    break
                else:
                    print(f"Shkruaj nje vlere valide per taskun {task_index}")

        headers = ['Indeksi i Taskut', 'URL']
        print(tabulate(dics.items()))
        print("Filloi marrja e fotove...")
       
        processes=[]
        for i in range(0, task_number):
            if action == 1:
                print(i)
                print("MULTIPROCESING PROCESSES")
                tic=time.time()
                p=multiprocessing.Process(target=download_multi, args=(dics,path))
                processes.append(p)
                toc=time.time()
                # print("Koha: " str(toc-tic))
            elif action == 2:
                thumb(dics,path)
            elif action == 3:      
                p=multiprocessing.Process(target=thumbnail, args=(dics,path))
                processes.append(p)
            print("Shkarkimi filloi për linkun ", i + 1, " koha: ", ctime(), )
            processes[i].start()   
        for i in range(0, task_number):
            processes[i].join()
        # for process in processes:
        #     process.join()
        print("Ruajtja e Fotove perfundoi.")       
               
               

#TODO: shtohet foto