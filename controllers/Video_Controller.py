import os
import threading
from time import sleep, ctime
import youtube_dl
from tabulate import tabulate

from controllers.Controller import Cotroller


def _download_video(url: str, task_number: int, name: str, path: str):
    ydl_opts = {
        'outtmpl': os.path.expanduser(path + '/{} Task {}.%(ext)s'.format(name, task_number), ),
        "index": task_number,

    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print("Shkarkimi për linkun ", str(task_number), " përfundoi në", ctime(),
              "----------------------------------------END-------------------------------------")


def _download_thumbnail(url: str, task_number: int, name: str, path: str):
    ydl_opts = {
        'outtmpl': os.path.expanduser(path + '/{} Task {}.%(ext)s'.format(name, task_number), ),
        "index": task_number,
        "skip_download": True,
        "writethumbnail": True

    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print("Shkarkimi për linkun ", str(task_number), " përfundoi në", ctime(),
              "----------------------------------------END-------------------------------------")


def _download_thumbnail_video(url: str, task_number: int, name: str, path: str):
    ydl_opts = {
        'outtmpl': os.path.expanduser(path + '/{} Task {}.%(ext)s'.format(name, task_number), ),
        "index": task_number,
        "writethumbnail": True

    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print("Shkarkimi për linkun ", str(task_number), " përfundoi në", ctime(),
              "----------------------------------------END-------------------------------------")


class VideoController(Cotroller):
    task_number = 0

    def create_new(self, action):
        max_links: int = 5

        while True:
            task_number = int(input(f"Sa video deshironi te downloadoni? Maximum  {max_links}: "))
            if task_number and 1 <= task_number <= max_links:
                break
            else:
                print("Vlera qe keni dhene nuk eshte valide. Ju lutem provoni perseri!")

        path = input("Shkruani lokacionin e folderit ku deshironi ti ruani videot: ")
        while not os.path.isdir(path):
            path = input("Lokacioni i dhene nuk egziston! Shkruani lokacionin e folderit ku doni ti ruani videot: ")

        print("Videot do te ruhen ne lokacionin {} ".format(path))
        tasks = {}
        task_index: int = 0
        for task in range(task_number):
            while True:
                video_link: str = input(f"Shkruaj linkun e videos: ")
                video_name: str = input(f"Shkruaj emrin e videos se si deshironi ta ruani: ")
                if video_link and video_name:
                    tasks[task_index] = {
                        "url": video_link,
                        "name": video_name,
                    }
                    task_index = task_index + 1
                    break
                else:
                    print(f"Shkruaj nje vlere valide per taskun {task_index}")

        headers = ["Indeksi i Taskut", "Informatat e dhena"]
        print(tabulate(tasks.items(), headers=headers,tablefmt="fancy_grid"))
        print("Filloi marrja e videove...")
        sleep(1)
        threads = []

        for i in range(0, task_number):
            if action == 1:
                thread = threading.Thread(target=_download_video, args=(tasks[i]['url'], i + 1, tasks[i]['name'], path))
                threads.append(thread)
            elif action == 2:
                thread = threading.Thread(target=_download_thumbnail,
                                          args=(tasks[i]['url'], i + 1, tasks[i]['name'], path))
                threads.append(thread)
            elif action == 3:
                thread = threading.Thread(target=_download_thumbnail_video,
                                          args=(tasks[i]['url'], i + 1, tasks[i]['name'], path))
                threads.append(thread)

            
            threads[i].start()

        for i in range(0, task_number):
            threads[i].join()

        print("Ruajtja e Videove perfundoi.")
