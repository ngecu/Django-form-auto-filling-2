from django.shortcuts import render
from .models import *
# Create your views here.
import json
from django.http import JsonResponse
from django.shortcuts import redirect


from string import ascii_letters
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys



options = Options()
# options.headless = True
driver = webdriver.Firefox(options=options,executable_path=GeckoDriverManager().install())

json_data = open('static/data2.json') 
data1 = json.load(json_data)

json_data = open('static/data2.json') 
data1 = json.load(json_data)

def Scrape():
       
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    driver.maximize_window()
    
    id_username = driver.find_element(By.ID,"id_username")
    id_password = driver.find_element(By.ID,"id_password")

    id_username.click()
    id_username.send_keys('ngecu')

    id_password.click()
    id_password.send_keys('d')
    

    driver.find_element(By.CSS_SELECTOR, ".submit-row > input").click()
    driver.find_element(By.LINK_TEXT, "Shoes").click()
    driver.find_element(By.CSS_SELECTOR, "li > .addlink").click()


    for item in data1:
        driver.find_element(By.ID, "id_title").click()
        driver.find_element(By.ID, "id_title").send_keys(item['Title'])
        driver.find_element(By.ID, "id_price").click()
        driver.find_element(By.ID, "id_price").send_keys(item['Price'])
        driver.find_element(By.ID, "id_image").click()
        driver.find_element(By.ID, "id_image").send_keys(item['Images'])
        driver.find_element(By.NAME, "_addanother").click() 
               
    driver.close()


def index(request):
    
    shoes = Shoe.objects.all().count()             
    context = {"data1":len(data1),'shoes':shoes}
    return render(request, 'main/index.html', context)


def add(request):
    shoes = Shoe.objects.all().count()
    if shoes == 0:
        # for x in data1:
        #     print(x['Title'])
        #     shoe,created = Shoe.objects.get_or_create(title=x['Title'],price=x['Price'],image=x['Images'])
        #     shoe.save()
        Scrape() 
        new_shoes = Shoe.objects.all().count()

        return render(request, 'main/added.html', {'shoes':new_shoes})
    else:
        return redirect('index')

def delete(request):
    shoes = Shoe.objects.all().count()
    if shoes > 0:
        Shoe.objects.all().delete()
        new_shoes = Shoe.objects.all().count()
        return render(request, 'main/delete.html', {'shoes':new_shoes})
    else:
         return redirect('index')
