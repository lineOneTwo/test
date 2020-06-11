import os

def load_file(a):
    # 返回当前目录下目标文件的绝对文件路径
    id_ini_path = os.path.abspath(os.path.dirname(__file__))+"\id.ini"
    class_name_ini_path = os.path.abspath(os.path.dirname(__file__)) + "\class_name.ini"
    location_ini_path = os.path.abspath(os.path.dirname(__file__)) + "\location_ini.ini"
    x_path_ini_path = os.path.abspath(os.path.dirname(__file__)) +"\path.ini"
    appPadkage_path=os.path.abspath(os.path.dirname(__file__)) +r"\appPadkage_appActivity.ini"
    dict_load = {
        2: id_ini_path,
        1:class_name_ini_path,
        3:location_ini_path,
        4:x_path_ini_path,
        5:appPadkage_path
    }
    if a in dict_load.keys():
         print(dict_load[a])
         return dict_load[a]





