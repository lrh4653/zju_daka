import time
import schedule
import ddddocr
from selenium import webdriver
import yaml
def job(user,pasw,cont,prof):
        count=0
        while True:
                count=count+1
                options=webdriver.FirefoxOptions()
                #options.add_argument("--headless")
                #browser=webdriver.Firefox(firefox_options=options)
                browser=webdriver.Firefox(firefox_profile=prof,firefox_options=options)
                browser.get("https://zjuam.zju.edu.cn/cas/login?service=https%3A%2F%2Fhealthreport.zju.edu.cn%2Fa_zju%2Fapi%2Fsso%2Findex%3Fredirect%3Dhttps%253A%252F%252Fhealthreport.zju.edu.cn%252Fncov%252Fwap%252Fdefault%252Findex%26from%3Dwap"
                )
                time.sleep(1)
                elem = browser.find_element_by_id("username")
                elem.send_keys(user)##xuehao
                elem = browser.find_element_by_id("password")
                elem.send_keys(pasw)##password
                browser.find_element_by_xpath("//*[@id='dl']").click()
                time.sleep(1)
                # elem=browser.find_element_by_xpath("//*[@class='text']/span/img")
                # ocr=ddddocr.DdddOcr()
                # img=elem.screenshot_as_png
                # yanzheng=ocr.classification(img).upper()
                # yanzheng=yanzheng.replace('1','I')
                # yanzheng=yanzheng.replace('0','O')
                # elem=browser.find_element_by_name("verifyCode")
                # elem.send_keys(yanzheng)
                # elem=browser.find_elements_by_xpath("//*[@class='wapat-btn wapat-btn-ok']")[0].click()
                # browser.execute_script("document.getElementsByName('ip')[0].style.display = 'inline';") 
                # elem=browser.find_element_by_xpath("//*[@class='hcqbtn hcqbtn-danger']/option[13]").click()
                # elem=browser.find_element_by_xpath("//*[@class='hcqbtn hcqbtn-warning']/option[2]").click()
                # time.sleep(2)
                # elem=browser.find_element_by_xpath("//*[@class='hcqbtn hcqbtn-primary']/option[6]").click()
                elem=browser.find_elements_by_xpath("//*[@name='sfzx']/div/div/span")[0].click()
                elem=browser.find_elements_by_xpath("//*[@name='sfqrxxss']/div/div/span")[0].click()
                elem=browser.find_elements_by_xpath("//*[@name='internship']/div/div")[2].click()
                # elem=browser.find_elements_by_xpath("//*[@name='sfymqjczrj']/div/div/span")[2].click()
                time.sleep(1)
                elem=browser.find_element_by_xpath("//*[@name='area']/input[@type='text']").click()
                time.sleep(1)
                elem=browser.find_elements_by_xpath("//*[@class='footers']/a")[0].click()
                time.sleep(2)
                elem=browser.find_elements_by_xpath("//*[@class='wapcf-btn wapcf-btn-ok']")[0].click()
                try:
                        elem=browser.find_element_by_xpath("//*[@class='wapat-title']")
                        browser.quit()
                        if (count==10):
                                print("尝试达到10次 依然没有成功 可能版本更新了 请手动打卡 更新将及时发布(如果可以的话)")
                                break
                        else:
                                print("当前尝试失败 自动再来一次")
                except:
                        browser.quit()
                        break
        print(cont)
        ss=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(ss) 

with open('config.yaml',encoding='utf-8') as f:
        fil=yaml.load(f,Loader=yaml.FullLoader)
        user=fil['user']
        pasw=fil['pass']
        shij=fil['time']
        cont=fil['cont']
        prof=fil['prof']
schedule.every().day.at(shij).do(job,user=user,pasw=pasw,cont=cont,prof=prof)
#job(user,pasw,cont,prof)
while True:
    schedule.run_pending()
    time.sleep(1)

