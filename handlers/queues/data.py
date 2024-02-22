from .base import BaseQueueHandler


class QueueHandler(BaseQueueHandler):
    def build_path(self):
        return f'/job_data/{self.job_object.id}/'
