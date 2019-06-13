from selenium import webdriver

def Taoyuan():
    target_url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Taoyuan_City.htm'
    driver = webdriver.PhantomJS(executable_path=r'C:\Users\lltin\.PyCharm2019.1\phantomjs.exe')#導入PhantomJS路徑
    driver.get(target_url)
    text = driver.find_element_by_xpath('//*[@id="ftext"]').text
    t = text.splitlines()
    return t[2]

print(Taoyuan())
