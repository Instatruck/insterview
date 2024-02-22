from .base import BaseQueueHandler


class QueueHandler(BaseQueueHandler):
    def build_path(self):
        return f'/jobs_assigned/{self.job_object.truck_id}/jobs/{self.job_object.id}/'
