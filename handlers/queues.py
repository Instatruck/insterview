from abc import ABC, abstractmethod


class QueueHandler(ABC):
    def __init__(self, job_object):
        self.job_object = job_object

    @abstractmethod
    def build_path(self):
        pass

class QueueHandlerNew(QueueHandler):
    def build_path(self):
        return f'/jobs_new/{self.job_object.id}/'

class QueueHandlerData(QueueHandler):
    def build_path(self):
        return f'/job_data/{self.job_object.id}/'

class QueueHandlerAssigned(QueueHandler):
    def build_path(self):
        return f'/jobs_assigned/{self.job_object.truck_id}/jobs/{self.job_object.id}/'

# Implement new queue "Suspended"
class QueueHandlerSuspended(QueueHandler):
    def build_path(self):
        return f'/jobs_suspended/{self.job_object.id}/'
