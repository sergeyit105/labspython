import xml.etree.ElementTree as etree
from urllib.request import urlopen
import sys

class XMLParse():
    def __init__(self):
        try:
                self.url = urlopen("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange")
        except:
            print("URL ERROR")
  
    def getXMLdata(self):
        self.tree = etree.parse(self.url)
    
    def result(self):
        print(self.tree)
        root = self.tree.getroot()
        entries = root.findall("currency")
        print(len(entries))
        a = []
        for i in range (len(entries)):
      		a.append(entries[i].find('.txt').text)
        print(a)

xmlParse = XMLParse()
xmlParse.getXMLdata()
xmlParse.result()
