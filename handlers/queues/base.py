from abc import ABC, abstractmethod


class BaseQueueHandler(ABC):
    def __init__(self, job_object):
        self.job_object = job_object

    @abstractmethod
    def build_path(self):
        pass
