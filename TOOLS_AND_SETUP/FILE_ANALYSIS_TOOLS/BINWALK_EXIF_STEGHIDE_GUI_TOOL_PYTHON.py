#sudo apt update && sudo apt upgrade
#sudo apt install -y unzip xvfb libxi6 libgconf-2-4
#pip install selenium
#wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
#unzip chromedriver_linux64.zip
#sudo mv chromedriver /usr/bin/chromedriver
#sudo chown root:root /usr/bin/chromedriver
#sudo chmod +x /usr/bin/chromedriver

### IMPORT LIBRARIES ###

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import csv

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

REGEXP = '(freedom\w{0,10})|(soci[ea]\w{0,10})|(social\w{0,10})|(\sunivers\w{0,10})|(commun\w{0,10})|(\smulti\w{0,10})|(entire\w{0,10})|(\stogeth\w{0,10})|(\sunit\w{0,10})|(everyone\w{0,10})|(democr\w{0,10})|(equal\w{0,10})|(raci[sa][ml]\w{0,10})|(fairn\w{0,10})|(justic\w{0,10})|(empow\w{0,10})|(world\w{0,10})|(citiz\w{0,10})|(progress\w{0,10})|(archai\w{0,10})|(moder\w{0,10})|(whole\w{0,10})|(ethn?ic\w{0,10})|(pride\w{0,10})|(proud\w{0,10})|(sex\w{0,10})|(oppress\w{0,10})|(revoluti\w{0.10})'

#from definitions import DRIVER_PATH
DRIVER_PATH = "/usr/bin/chromedriver"

### IMPORT SELENIUM WEB DRIVER ####


### OPEN CSV FILES WITH W TO CLEAN THEM ###

with open('TEXT FILE FROM BODY TAG.csv', 'w', encoding='utf-8', errors='replace') as f:
    f.write('Thank you for using REGEXP FETCH AND COUNT. \n')

with open('OUTPUT MATCHES.csv', 'w', encoding='utf-8', errors='replace') as f:
    f.write('Thank you for using REGEXP FETCH AND COUNT. \n')

### INIT QT WINDOW ###


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(680, 120))
        self.setWindowTitle("QT REGEXP TOOL")

### INSERT LINK QLABEL AND QLINE EDIT ###

        self.LINKLabel = QLabel(self)
        self.LINKLabel.setText('Full Link from Web Page: ')
        self.LINKInsert = QLineEdit(self)

        self.LINKLabel.move(30, 30)
        self.LINKLabel.resize(400, 20)
        self.LINKInsert.move(250, 25)
        self.LINKInsert.resize(400, 32)

### BUTTON RATE INTEGRITI ###

        pybutton = QPushButton('FETCH AND COUNT!', self)
        pybutton.clicked.connect(self.clickMethodRate)
        pybutton.move(250, 60)
        pybutton.resize(400, 34)

### AT BUTTON CLICK ###

    def clickMethodRate(self):
        entered_LINK = self.LINKInsert.text()

### OPTIONS HEADLESS START WEB DRIVER ###
        options = Options()
        options.add_argument('--start-maximized')
        options.headless = True

        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})

### GET LINK FROM INPUT LINKINSERT AND STORE BODY TAG IN VARIABLE ###

        driver.get(str(entered_LINK))
        body = driver.find_elements_by_tag_name("body")

### GET ALL TEXT FROM BODY TAG TO CSV FILE ###

        with open('BODY_TAG_TXT.csv', 'a', encoding='utf-8', errors='replace') as f:
            for k in range(len(body)):
                f.write(body[k].text)

### OPEN THE BODY CSV FILE ###

        with open('BODY_TAG_TXT.csv', 'r', errors='replace') as f:

            ### READ BODY CSV FILE AND COUNT RE PATTERN MATCH ###

            pattern = REGEXP
            text = f.read()

            count = 1

            for match in re.finditer(pattern, text):

                ### SAVE MATCHES THEMSELVES INTO OUTPUT CSV ###

                with open('OUTPUT MATCHES.csv', 'a', encoding='utf-8', errors='replace') as f1:
                    f1.write(str(match) + "; ")
                    f1.write(str(count) + "; " + "\n")
                count += 1

### CLOSE DRIVER ###

#            driver.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
