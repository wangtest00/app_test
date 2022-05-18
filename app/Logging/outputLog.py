# -*- coding:utf-8 -*-
# __author__ = "Cc"
import logging
import time


class OutputLog:
    critical = logging.CRITICAL  # 级别最高，什么也不输出
    fatal = logging.FATAL
    error = logging.ERROR
    warning = logging.WARNING
    info = logging.INFO
    debug = logging.DEBUG
    @classmethod
    def output_log(cls, log_level=debug):
        my_logging = logging.getLogger(__name__)
        my_logging.setLevel(log_level)
        if not my_logging.handlers:
            local_time = time.localtime()
            file_name1 = time.strftime('%Y-%m-%d', local_time)
            file_name2 = r"Logging\\"
            file_name = file_name2 + file_name1 + ".log"
            file_handler = logging.FileHandler(file_name, "a", encoding="utf-8")  # 输出日志到磁盘文件
            file_handler.setLevel(log_level)
            formatter = logging.Formatter("%(asctime)s--%(levelname)s--%(process)d--"
                                        "%(thread)d--%(threadName)s--%(funcName)s--%(lineno)d--%(lineno)d : %(message)s")
            file_handler.setFormatter(formatter)
            my_logging.addHandler(file_handler)
        return my_logging