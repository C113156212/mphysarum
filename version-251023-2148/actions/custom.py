from core.base import IAction
from abc import ABC, abstractmethod

#這裡是 自訂行動 檔案

class yourActionName(IAction):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def run(self):
        raise NotImplementedError