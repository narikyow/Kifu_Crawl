from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class Browse:
    def __init__(self,count):
        self.options = Options()
        
        self.options.binary_location = "chrome.exeまでのフルパス"
        
        self.driver = webdriver.Chrome(chrome_options=self.options, executable_path="driver/chromedriver.exe")#chromedriver.exeまでの相対パス
        
        self.text=""

        self.next_url="None"

        self.count=count
        
        self.driver.get('https://shogidb2.com/search?q=%E4%B8%89%E9%96%93%E9%A3%9B%E8%BB%8A')
        #最初に遷移するページ。このページを起点にURLを取得していく
        #自分がほしい戦型で検索したときの最初のページを設定するとよい

    def get_url(self):
        element = self.driver.find_element_by_class_name('list-group')
        
        aTag    = element.find_elements_by_tag_name("a")
        print(aTag)
        url_list= [i.get_attribute("href") for i in aTag]
        print(url_list)
        for i in range(len(url_list)):
            self.text=("".join([self.text,url_list[i],"\n"]))
        
        
    
    def change_page(self):
        confirm=0

        confirm_text=0

        self.next_url="None"#初期化

        next_element = self.driver.find_element_by_class_name('pagination')

        next_aTag = next_element.find_elements_by_tag_name("a")
        
        next_text = [i.text for i in next_aTag]

        self.count=str(int(self.count)+1)

        for i in range(len(next_text)):

            if self.count == next_text[i]:
                self.next_url= next_aTag[i].get_attribute("href")#1度にそのページにある全ての対局のURLを取得する
                confirm +=1
                if int(self.count) >400:#目安のページ数。これを設定しないと無限ループに陥る
                    confirm=0
                break
        
        if confirm == 0:
            confirm_text=1
            return confirm_text

        self.driver.get(self.next_url)
        time.sleep(3)
        return confirm_text
    

    def auto(self):

        confirm_return=0
        
        while confirm_return==0:
            self.get_url()
            print(self.text)
            confirm_return = self.change_page()
        
        with open("DataBaseLinks.txt",mode="w") as f:
            f.write(self.text)

        print_text="all done"

        return print_text



if __name__=="__main__":

    count_num="1"
    browse=Browse(count_num)#最初に__init__内で設定したページに遷移
    time.sleep(3)
    do = browse.auto()
    print(do)