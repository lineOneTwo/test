from selenium.webdriver.support.wait import WebDriverWait
from common.appium_common.read_config import read_ini
from config.appium_conf.load_file import load_file


def exist(driver, ini_file_path, name, value):  # 判断是否存在此元素
    """ini_name:配置文件的路径"""
    ele = read_ini(ini_file_path=ini_file_path, name=name, value=value)
    source = driver.section_name_source
    if ele in source:
        return True
    else:
        return False


def looking_for_element(driver, elements_name, section_name, name):  # 根据元素类型进行不同的元素定位
    """elements_name:元素类型"""
    try:
        if elements_name == 1:  # class_name
            the_name = read_ini(ini_file_path=load_file(1), name=section_name, value=name)
            print(the_name)
            return WebDriverWait(driver, 30).until(lambda x: x.find_element_by_class_name(the_name))
        if elements_name == 2:  # id
            the_name1 = read_ini(ini_file_path=load_file(2), name=section_name, value=name)
            print(the_name1)
            return WebDriverWait(driver, 30).until(lambda x: x.find_element_by_id(the_name1))
        if elements_name == 3:  # tap
            the_name2 = read_ini(ini_file_path=load_file(3), name=section_name, value=name)
            print(the_name2)
            return WebDriverWait(driver, 30).until(lambda x: x.tap(the_name2, 1000))
        if elements_name == 4:  # xpath
            the_name4 = read_ini(ini_file_path=load_file(4), name=section_name, value=name)
            print(the_name4)
            return WebDriverWait(driver, 25).until(lambda x: x.find_element_by_xpath(the_name4))
    except TypeError:
        print("抱歉，找不到元素")
    except TimeoutError:
        print("超时，请检查代码")


def clicking(driver, elements_name, section_name, name):  # 点击
    looking_for_element(driver=driver, elements_name=elements_name, section_name=section_name, name=name).click()


def inputting(driver, elements_name, section_name, name, txt):  # 输入内容
    looking_for_element(driver=driver, elements_name=elements_name, section_name=section_name, name=name).send_keys(txt)


def taping(driver, elements_name, section_name, name):  # 点击
    looking_for_element(driver=driver, elements_name=elements_name, section_name=section_name, name=name)
