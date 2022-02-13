import os
from time import sleep

from tabulate import tabulate

class ImageController:
    task_number = 0

    def create_new(self, action):
        max_links: int = 5

        while True:
            task_number = int(input(f"Sa foto deshironi te downloadoni? Maximum  {max_links}: "))
            if task_number and 1 <= task_number <= max_links:
                break
            else:
                print("Vlera qe keni dhene nuk eshte valide. Ju lutem provoni perseri!")

        path = input("Shkruani lokacionin e folderit ku deshironi ti ruani fotot: ")
        while not os.path.isdir(path):
            path = input("Lokacioni i dhene nuk egziston! Shkruani lokacionin e folderit ku doni ti ruani fotot: ")

        print("Fotot do te ruhen ne lokacionin {} ".format(path))
        tasks = {}
        task_index: int = 0
        for task in range(task_number):
            while True:
                video_link: str = input(f"Shkruaj linkun e fotos: ")
                video_name: str = input(f"Shkruaj emrin e fotos se si deshironi ta ruani: ")
                resize_number: str = input(f"Shkruaj sa here deshironi ta zvogeloni foton: ")
                if video_link and video_name:
                    tasks[task_index] = {
                        "url": video_link,
                        "name": video_name,
                        "resize": resize_number,
                    }
                    task_index = task_index + 1
                    break
                else:
                    print(f"Shkruaj nje vlere valide per taskun {task_index}")

        headers = ['Indeksi i Taskut', 'URL']
        print(tabulate(tasks.items()))
        print("Filloi marrja e fotove...")
        sleep(1)

#TODO: shtohet foto

        print("Ruajtja e Fotove perfundoi.")
