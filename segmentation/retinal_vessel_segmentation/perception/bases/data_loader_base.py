
"""
Copyright (c) 2019. All rights reserved.
Created by Peng Tang on 2019/1/7
"""


class DataLoaderBase(object):
    """
    数据加载的基类
    """

    def __init__(self, config):
        self.config = config  # 设置配置信息

    def prepare_dataset(self):
        """
        将原始数据转换为hdf5格式
        """
        raise NotImplementedError

    def get_train_data(self):
        """
        获取训练数据
        """
        raise NotImplementedError

    def get_val_data(self):
        """
        获取验证数据
        """
        raise NotImplementedError
