from re import search
from django.conf.urls import url
import selenium
from django.shortcuts import render,redirect,HttpResponse
from selenium import webdriver  #install webdriver-manager
from selenium.webdriver.common.keys import Keys  
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
# Create your views here.



def cardekho(request):
    #search=request.POST['search']
    search="Hyundai"
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    url="https://www.cardekho.com/" 
    #url='https://www.cardekho.com/cars/Mahindra'
    driver.get(url)
    #driver.implicitly_wait(10) # seconds
   # wait=WebDriverWait(driver, 10)
   # wait.until(EC.presence_of_element_located((By.ID, 'cardekhosearchtext')))
    # driver.find_element_by_id('cardekhosearchtext').send_keys()
    # time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="rf01"]/header/div[1]/div/div/div[2]/div/div/form/button').click()
    driver.find_element_by_xpath('//*[@id="rf01"]/header/div[2]/div/div/nav/ul/li[1]/a').click()
    # curl=driver.current_url
    # print('current_url============-----gggggggggg----gsc_col-lg-2----::',curl)
    print("===================start1===============")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="brands"]/div/div[2]/div[1]/div/span').click()
    time.sleep(5)
    cars=driver.find_element_by_class_name('listing')
    #print(type(cars),"--",cars.text,"-")
    li=cars.find_elements_by_tag_name('li')
    #print("====li=====",li)
    car_names=[]
    car_price=[]
    car_f=[]
    car_image=[]
    for i in li:
        if i.text==search:
            i.click()
            time.sleep(10)
            carss=driver.find_elements_by_class_name('shadowWPadding')
            print("total cars:",len(carss))
            
            for car in carss:
                try:
                   
                    price=car.find_element_by_class_name('price')
                    p=price.text.split('*')
                    car_name=car.find_element_by_tag_name('a')
                    c=car_name.text
                    image=car.find_element_by_tag_name('img').get_attribute('src')
                    features=car.find_element_by_class_name('clearfix')
                    f=features.text
                            # append data
                    car_names.append(c)
                    car_price.append(p[0])
                    car_f.append(f)
                    car_image.append(image)
                   
                    print("price",p[0],"name",car_name.text,"featuress",features.text,image)
                except:
                    print("except====================")
            
            print("make data frame data")
            df=pd.DataFrame({"name":car_names,"price":car_price,"img":car_image,"featuress":car_f})
            print("***********************data frame:",df)
            df.to_csv(f'{search}_data.csv')
           
            driver.close() 
            return HttpResponse("data scrap successfully")    
       
    























































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
        curl=driver.current_url
        print('current_url============-----gggggggggg--------::',curl)
        time.sleep(15)
          # for get total page
        # page=driver.find_element_by_class_name('a-pagination')
        # page=page.find_element_by_xpath('')
        # tp=page.text
        #print("total page===========================",tp)
        data = driver.find_elements_by_class_name('s-asin')
        print("total",len(data))
        name=[]
        price=[]
        image=[]
        tp=driver.find_elements_by_class_name('a-disabled')
        print('========page=====',tp[-1].text)
        pages=int(tp[-1].text)
        for page in range(1,pages):
            print("page====================",page)
            for data in driver.find_elements_by_class_name('s-asin'):
                try:
                
                    n=data.find_element_by_class_name('a-size-medium ')
                    n=n.text
                    p=data.find_element_by_class_name('a-price-whole')
                    ps=p.text
                    img=data.find_element_by_tag_name('img').get_attribute('src')
                    print('===',n)
                    print(type(n))
                    name.append(n) 
                    #l=n.split('-')
                    #color.append(l[1])
                    price.append(ps)
                    image.append(img)
                except:
                    print("not avalaible")
            
            driver.find_element_by_partial_link_text('Next').click()
            time.sleep(2)




        df=pd.DataFrame({"name":name,"price":price,"img":image})
        print(df)
        df.to_csv(f'{sr}.csv')
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
    driver.find_elements_by_class_name('cntanr')

    #driver.close() 
