import configparser


def read_ini(ini_file_path, name, value):  # 根据文件读取ini文件
	conf = configparser.ConfigParser()
	conf.read(ini_file_path, encoding="utf-8-sig")
	temp = conf.get(name, value)
	return temp
