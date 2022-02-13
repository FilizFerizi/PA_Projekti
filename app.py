def download(url: str, link_number: int, video_path: str):
    ydl_opts = {
        "download_archive": video_path + "/downloaded_videos.txt",
        'outtmpl': os.path.expanduser(video_path + '/%(title)s-Linku numer {}.%(ext)s'.format(link_number)),
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
        print("Shkarkimi për linkun ", str(link_number), " përfundoi në", ctime(),
              "----------------------------------------END-------------------------------------")


def run():
    threads: List[Thread] = []
    path = input("Shkruani lokacionin e folderit ku doni ti ruani videot: ")
    while not os.path.isdir(path):
        path = input("Lokacioni i dhene nuk egziston! Shkruani lokacionin e folderit ku doni ti ruani videot: ")

    print("Videot e meposhtme do te ruhen ne lokacionin {} ".format(path))

    n = int(input("Sa video dëshironi të shkarkoni? "))

    for i in range(0, n):
        print("Shkruaj linkun numër ", str(i + 1), " :")
        ele = input()
        url_list.append([ele])
    number_of_links = len(url_list)

    for i in range(0, number_of_links):
        t = threading.Thread(target=download, args=(url_list[i], i + 1, path))
        threads.append(t)

    for i in range(0, number_of_links):
        threads[i].start()
        print("Shkarkimi filloi për linkun ", i + 1, " koha: ", ctime(), )

    for i in range(0, number_of_links):
        threads[i].join()

    # kur te jene imput te gjitha url-s te ndara me presje
    # url_list = [n for n in input("Vendosni linqet qe deshironi te downloadoni: ").split(",")]

    print('Program Finished at time: ', ctime())


if __name__ == '__main__':
    print('starting program at time: ', ctime())
    run()
