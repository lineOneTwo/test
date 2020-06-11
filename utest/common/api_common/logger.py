# encoding: utf-8
import logging
import os
import time
from common.api_common.conf import project_path


class Log(object):
    """
    《日志添加说明》
    api文件：
    （1）import后实例化，logger = Loge()
    （2）定义的api中，return前加入logger.info('url=%s，request=%s，response=%s' % (url, data, r.text))
    注：主要记录url、请求数据、返回数据
    case文件：
    （1）第一条用例说明后，添加
        logger.info('############%s############' % self.__class__.__name__)
        logger.info('执行测试用例：%s，file：%s，line：%s' % (get_function_name(), sys._getframe().f_code.co_filename,
                                                   sys._getframe().f_lineno))
    （2）其他用例说明后，添加
        logger.info('执行测试用例：%s，file：%s，line：%s' % (get_function_name(), sys._getframe().f_code.co_filename,
                                                   sys._getframe().f_lineno))
    注：主要记录测试用例类名、用例方法名、用例文件名、用例行号
    """
    def __init__(self):
        # 文件的命名
        log_path = project_path + '/logs'
        if not os.path.exists(log_path):                # 如果不存在这个logs文件夹，就自动创建一个
            os.mkdir(log_path)
        self.logname = os.path.join(log_path, "log_%s.log" % time.strftime("%Y%m%d"))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, "a", encoding='utf-8')     # 追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == "info":
            self.logger.info(message)
        elif level == "debug":
            self.logger.debug(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console("debug", message)

    def info(self, message):
        self.__console("info", message)

    def warning(self, message):
        self.__console("warning", message)

    def error(self, message):
        self.__console("error", message)


logger = Log()

if __name__ == "__main__":
    log = Log()
    log.info("--测试开始--")
    log.info("操作步骤1，2,3")
    log.warning("--测试结束--")
