import csv
import os
import threading
import time
from urllib.parse import urlparse

from bs4 import BeautifulSoup
import datetime
import requests


def downloader(
        title,
        base_url,
        element,
        current_visit_data,
        saved_filename=None):


    res = requests.get(base_url)
    res.raise_for_status()


    soup = BeautifulSoup(res.text, "lxml")
    comic_elem = soup.select(element)

    if comic_elem == []:

        print(f"Could not find current comic for {title}.")
        return None
    else:
        comic_url = comic_elem[0].get("src")
        comic_filename = os.path.basename(comic_url)

        if saved_filename and comic_filename.lower() == saved_filename.lower():

            print(f"No updates for {title}.")
            return None
        else:
            print(f"Downloading latest comic from {title}...")

            if not urlparse(comic_url).netloc:

                comic_url = f"{base_url}/{comic_url}"

            res = requests.get(comic_url)
            res.raise_for_status()

            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            folder = f"C:{os.path.join(os.environ['HOMEPATH'], 'Desktop')}\\{current_date} Web Comics"
            os.makedirs(folder, exist_ok=True)

            with open(f"{folder}\{comic_filename}", "wb") as comic_file:
                for part in res.iter_content(100000):
                    comic_file.write(part)


            current_visit_data[title] = comic_filename

def main():

    print(f"\n{'Scheduled Web Comic Downloader':>42}")
    print(f"{'********* *** ***** **********':>42}\n")
    print("The following web comics will be checked for updates:\n\n"
          ":: Left-handed Toons\t\t"
          ":: Buttersafe\n"
          ":: Two Guys and Guy\t\t"
          ":: Savage Chickens\n"
          ":: Channelate\t\t\t"
          ":: Extra Ordinary\n"
          ":: Wonderella\t\t\t"
          ":: Moonbeard\n"
          ":: Happle Tea\t\t\t"
          ":: Saturday Morning Breakfast Cereal\n"),
    print("Comics will be saved on your Desktop under 'Updated Web Comics'.\n")

    try:
        with open("schedComicDown.csv") as last_visit_file:
            last_visit_reader = csv.reader(last_visit_file)

            last_visit_data = {}
            for row in last_visit_reader:
                last_visit_data[row[0]] = row[1]

    except FileNotFoundError:
        last_visit_data = {}

    current_visit_data = {"Last Checked:": time.time()}

    comics = [
        ["Left-handed Toons", "http://www.lefthandedtoons.com/", ".comicimage"],
        ["Buttersafe", "http://buttersafe.com/", "#comic img"],
        ["Two Guys and Guy", "http://www.twogag.com/", "div#comic div a img"],
        ["Savage Chickens", "http://www.savagechickens.com/", "div.entry_content p img"],
        ["Channelate", "http://www.channelate.com/", "div#comic img"],
        ["Extra Ordinary", "http://www.exocomics.com/", "a.comic img"],
        ["Wonderella", "http://nonadventures.com/", "div#comic img"],
        ["Moonbeard", "http://moonbeard.com/", "div#comic div a img"],
        ["Happle Tea", "http://www.happletea.com/", "div#comic img"],
        ["Saturday Morning Breakfast Cereal", "https://www.smbc-comics.com/", "img#cc-comic"],
    ]

    downloads = []
    for comic in comics:
        comic.append(current_visit_data)
        if comic[0] in last_visit_data.keys():
            comic.append(last_visit_data[comic[0]])

        download = threading.Thread(target=downloader, args=comic)
        downloads.append(download)
        download.start()

    for download in downloads:
        download.join()

    updated_data = {**last_visit_data, **current_visit_data}

    with open("schedComicDown.csv", "w", newline="") as current_visit_file:
        current_visit_writer = csv.writer(current_visit_file)

        for key, value in updated_data.items():
            current_visit_writer.writerow([key, value])

    print("All done!")

if __name__ == '__main__':
    main()