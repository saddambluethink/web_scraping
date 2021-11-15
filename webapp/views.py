import selenium
from django.shortcuts import render,redirect,HttpResponse
from selenium import webdriver  #install webdriver-manager
from selenium.webdriver.common.keys import Keys  
import time
from webdriver_manager.chrome import ChromeDriverManager
# Create your views here.



# def whatsapp(request):
#     driver = webdriver.Chrome(ChromeDriverManager().install()) 
#     #  get url
#     driver.get("https://web.whatsapp.com/")
#     input("please scan QR code and press any key to continue:")
#     sehzad=driver.find_element_by_css_selector('span[title="Owesh BCA"]')
#     sehzad.click()
#         # find x path
#     ti=driver.find_element_by_xpath("/html/body")
#     for i in range(1,100):
#         time.sleep(1)
#         ti.send_keys("hello bro")
#         ti.send_keys(Keys.ENTER)











def webscrap(request):
    driver = webdriver.Chrome(ChromeDriverManager().install()) 

    driver.get("https://www.google.com/")  
    #time.sleep(5)
    driver.find_element_by_name("q").send_keys("javatpoint")
    # driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
    driver.find_element_by_name("btnK").click() 

    # driver.find_element_by_name("q").send_keys("javatpoint" + Keys.RETURN)
    # driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a/h3" + Keys.RETURN)
    #driver.find_element_by_name("q").send_keys(Keys.RETURN)
     
    time.sleep(5)
    # driver.close()  
    return HttpResponse('done')









def amazon(request):
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    url="https://www.amazon.in/"    
    driver.get(url) 
    time.sleep(2)
    driver.find_element_by_id('twotabsearchtextbox').send_keys("apple mobile" + Keys.RETURN)


   # item_to_search = "apple mobile"
   # search_box = driver.find_element_by_id('twotabsearchtextbox')
    #search_box.clear()
    #search_box.send_keys(item_to_search)
    #search_box.send_keys(Keys.RETURN)
    #driver.close() 
    time.sleep(10)










def justdial(request):
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    url="https://www.justdial.com/"    
    driver.get(url) 
    time.sleep(20)

    #driver.close() 