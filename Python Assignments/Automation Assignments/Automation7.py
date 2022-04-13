import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

email_username = input('What is your username?\n')
email_password = input('What is your password?\n')
email_recipient = input('Who would you like to send an email to?\n')
email_subject = input('What is the subject of the email?\n')
email_body = input('What would you like to say?\n')

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(30)
browser.get('http://mail.google.com')
login_elem = browser.find_element_by_id('identifierId')
login_elem.send_keys(email_username)
next_elem = browser.find_element_by_id('identifierNext')
next_elem.click()
time.sleep(3)
password_elem = browser.find_element_by_name('password')
password_elem.send_keys(email_password)
pw_next_elem = browser.find_element_by_id('passwordNext')
pw_next_elem.click()
time.sleep(3)

html_elem = browser.find_element_by_tag_name('html')
html_elem.send_keys('c')
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_recipient)
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_subject)
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_body)
html_elem.send_keys(Keys.ENTER)

print('Email was sent.')



# Image Site Downloader :-


def main():
    import requests, os, bs4
    from selenium import webdriver, common

    # Open Browser to photo-sharing site
    url = "https://www.flickr.com/search/?text="
    os.makedirs("images", exist_ok=True)

    browser = webdriver.Firefox()
    browser.implicitly_wait(10)

    browser.get(url + "Cats")

    try:
        imageElems = browser.find_elements_by_css_selector("a.overlay")
        for element in imageElems:
            downloadUrl = element.get_attribute("href") + "sizes/o/"
            res = requests.get(downloadUrl)
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, "lxml")

            imageElem = soup.select("img")  # FIXME: Last few images are not of the category

            if not imageElem:
                print("Could not find image.")
            else:
                imageUrl = imageElem[2].get("src")

                res = requests.get(imageUrl)
                res.raise_for_status()

                imageFile = open(os.path.join("images", os.path.basename(imageUrl)), "wb")
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()

    except common.exceptions.NoSuchElementException as err:
        print("Unable to locate element: %s" % err)

    browser.close()



if __name__ == '__main__':
    main()



# 2048 :-

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('body')
exitPoint = browser.find_element_by_class_name('game-message')

while exitPoint.text == '':

    htmlElem.send_keys(Keys.RIGHT)
    time.sleep(2)
    htmlElem.send_keys(Keys.UP)
    time.sleep(2)
    htmlElem.send_keys(Keys.DOWN)
    time.sleep(2)
    htmlElem.send_keys(Keys.LEFT)
    time.sleep(2)

Score = browser.find_element_by_class_name('score-container')

print('Your Score: %s' % (Score.text))

print('GAME OVER!!!')

browser.quit()


# Link Verification :-

def main():
    import requests, bs4, os
    from urllib.request import urlretrieve

    # Fetch page
    res = requests.get("http://JoseALerma.com")
    res.raise_for_status()  # raise error if nothing fetched

    soup = bs4.BeautifulSoup(res.text, "lxml")

    anchors = soup.find_all('a')
    links = []

    for anchor in anchors:
        link = anchor.get("href")
        if str(link).startswith("http"):
            links.append(link)

    links.append("http://JoseALerma.com/potato")
    links.append("http://JoseALerma.com/carrot")

    os.makedirs("pages", exist_ok=True)  # Save in ./pages

    for link in links:
        try:
            res = requests.head(link)  # Only fetch head tag for speed
            if res.status_code == 404:
                # Print code 404 pages
                print("Page not found: %s" % link)
            else:
                filepath = os.path.join("pages", os.path.basename(link + ".html"))
                urlretrieve(link, filepath)
        except requests.exceptions.ConnectionError:
            print("Unable to connect to: %s" % link)



if __name__ == '__main__':
    main()