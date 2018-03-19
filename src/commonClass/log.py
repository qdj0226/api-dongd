__author__ = "dongd"

import logging,threading,configparser,os,time
from config.configFile import logconfig,logfile

class Log(object):
    '''
    日志类,封装日志方法
    '''
    def __init__(self,log_config):
        pass

    def __new__(cls, log_config):
        thread = threading.Lock()
        thread.acquire()    #上锁,防止多线程下出现问题
        if not hasattr(cls,"instance"):     #判断对象是否存在"instance"属性
                                                #不存在该熟悉便进行初始化
            cls.instance = super(Log, cls).__new__(cls)

            # 获取log的配置信息
            config = configparser.ConfigParser()
            config.read(log_config, encoding='utf-8')
            cls.instance.fmt = config.get("LOGGING","fmt")
            cls.instance.stream_log_on = int(config.get("LOGGING","stream_log_on"))
            cls.instance.file_log_on = int(config.get("LOGGING","file_log_on"))
            cls.instance.log_level_in_stream = int(config.get('LOGGING', 'log_level_in_stream'))
            cls.instance.log_level_in_file = int(config.get('LOGGING', 'log_level_in_file'))
            # 实例化getlogger
            cls.instance.logger = logging.getLogger()
            cls.instance.__config_logger()
        thread.release()
        return cls.instance

    def get_logger(self):
        # 返回log 实例
        return self.logger

    def __config_logger(self):
        # 设置log格式
        fmt = self.fmt.replace('|', '%')
        formatter = logging.Formatter(fmt)

        if self.instance.stream_log_on == 1: #开启控制台日志
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)
            self.logger.setLevel(self.log_level_in_stream)

        if self.instance.file_log_on == 1:#开启文件日志

            log_name = time.strftime("%Y%m%d")
            log_path_name = os.path.join(logfile,"{}.log".format(log_name))
            fh = logging.FileHandler(log_path_name,encoding="utf-8")
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
            self.logger.setLevel(self.log_level_in_file)


log = Log(logconfig)
logger = log.get_logger()
