from xml.etree.ElementTree import ElementTree as ET

class ConfigureEntity:
    def __init__(self,path):
        self.path=path
    
    def parse(self):
        tree=ET()
        tree.parse(self.path)
        print(tree.getroot())
        list=[]
        for account in tree.getroot().getchildren():
            print(account.find("name").text)
            print(account.find("account").text)
            print(account.find("mobile").text)
            print(account.find("id").text)

def main():
    ce=ConfigureEntity("account.xml")
    ce.parse()

if __name__=='__main__':
    main()