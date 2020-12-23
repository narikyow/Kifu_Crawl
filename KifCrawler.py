from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class Crawler:
    def __init__(self,address,bt_form):
        self.address=address

        self.kif_url_list=[]

        self.output_kif=""

        self.battle_form=bt_form

        self.counter=0

        self.options = Options()
        
        self.options.binary_location = "C:/Users/享市/AppData/Local/Google/Chrome/Application/chrome.exe"
        
        self.driver = webdriver.Chrome(chrome_options=self.options, executable_path="driver/chromedriver.exe")

        self.read()


    def read(self):
        with open(self.address,mode="r") as f:
            self.kif_url_list=list(f)
            self.counter=len(self.kif_url_list)
            #urlをlistで格納

    def get_kif(self):
        
        for i in range(self.counter):
            
            if "https:" not in self.kif_url_list[i].split("/"):
                break
            
            self.driver.get(self.kif_url_list[i])
            
            time.sleep(2)
            
            battle_form_elem_text=self.driver.find_element_by_xpath("/html/body/div[@class='container-fluid']/div[@id='app']/div/div[@class='row'][2]/div[@class='col-12 col-md-3 py-2'][1]/div/table[@class='table table-bordered table-hover table-sm']/tbody/tr[10]/td/a").text
            
            teaiwari=self.driver.find_element_by_xpath("/html/body/div[@class='container-fluid']/div[@id='app']/div/div[@class='row'][2]/div[@class='col-12 col-md-3 py-2'][1]/div/table[@class='table table-bordered table-hover table-sm']/tbody/tr[6]/td").text
            
            if self.battle_form in battle_form_elem_text and "平手" in teaiwari:
            
                self.driver.find_element_by_id("kif-export").click()
                time.sleep(1)
                kif_elem=self.driver.find_element_by_class_name("control-group")

                kif_text=kif_elem.find_element_by_tag_name("textarea").text
                
                with open("".join(["Kif_DB_Files/",str(i+1),".kif"]),mode="w")as f:
                    f.write(kif_text)
                    print(kif_text)
                    print("".join([str(i+1)," / ",str(self.counter)," Finished"]))

            
if __name__ == "__main__":
    address = "DataBaseLinks.txt"
    #urlを格納したファイル名
    battle_form="三間飛車"
    #戦型名
    Cr = Crawler(address,battle_form)
    Cr.get_kif()

