from .base import BaseQueueHandler


class QueueHandler(BaseQueueHandler):
    def build_path(self):
        return f'/jobs_suspended/{self.job_object.id}/'
