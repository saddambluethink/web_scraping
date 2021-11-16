import selenium
from django.shortcuts import render,redirect,HttpResponse
from selenium import webdriver  #install webdriver-manager
from selenium.webdriver.common.keys import Keys  
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
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
    if request.method=='POST':
        sr=request.POST['data']
        driver = webdriver.Chrome(ChromeDriverManager().install()) 
        url="https://www.amazon.in/" 
        driver.get(url)
        
        driver.find_element_by_id('twotabsearchtextbox').send_keys(sr)
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input').click()
        time.sleep(15)
    
        data = driver.find_elements_by_class_name('s-asin')
        print("total",len(data))
        name=[]
        price=[]
        image=[]
    
        for data in driver.find_elements_by_class_name('s-asin'):
            if data.find_element_by_class_name('a-size-medium ') and data.find_element_by_class_name('a-price-whole'):
                    
                n=data.find_element_by_class_name('a-size-medium ')
                n=n.text
                #l=n.split('-')
                name.append(n)
                #color.append(l[1])
                p=data.find_element_by_class_name('a-price-whole')
                price.append(p.text)
                img=data.find_element_by_tag_name('img').get_attribute('src')
                image.append(img)

                #print("data======",name.text,"price",price.text,"image",img)
            else:
                print("data sorted 1")
        df=pd.DataFrame({"name":name,"price":price,"img":img})
        print(df)
        df.to_csv('myfile3.csv')
        print("----------------------------end====================")
        driver.close() 
    return render(request,'index.html')







#    # item_to_search = "apple mobile"
#    # search_box = driver.find_element_by_id('twotabsearchtextbox')
#     #search_box.clear()
#     #search_box.send_keys(item_to_search)
#     #search_box.send_keys(Keys.RETURN)
#     #driver.close() 
#     time.sleep(10)










def justdial(request):
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    url="https://www.justdial.com/"    
    driver.get(url) 
    time.sleep(20)

    #driver.close() 