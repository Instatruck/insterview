from .base import BaseJobHandler


class JobHandler(BaseJobHandler):
    def get_queues(self):
        return ['assigned', 'data']
