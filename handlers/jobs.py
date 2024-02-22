from abc import ABC, abstractmethod

from . import queues as queue_handlers


class JobHandler(ABC):
    def __init__(self, job_object, db_writer, local_db):
        self.job_object = job_object
        self.db_writer = db_writer
        self.local_db = local_db

    def sync_db(self):
        # Get current queues from local db
        current_queues = self.local_db.get(self.job_object.id, {}).get('queues', {})

        # Get user-defined queues
        queues = self.get_queues()

        # Remove from queues which are not valid for the current state
        for k, v in current_queues.items():
            if k not in queues:
                self.db_writer.remove_object_from_path(v['path'], None)

        # Put to queues which are valid for the current state
        queues_data = {}
        for q in queues:
            queue_handler = getattr(queue_handlers, f'QueueHandler{q}')(self.job_object)
            path = queue_handler.build_path()
            self.db_writer.write_object_to_path(path, self.job_object)

            queues_data[q] = {
                'path': path
            }

        # Update local db
        self.local_db.update({
            self.job_object.id: {
                'queues': queues_data,
            }
        })

    @abstractmethod
    def get_queues(self):
        pass

class JobHandlerN(JobHandler):
    def get_queues(self):
        return ['New', 'Data']

class JobHandlerM(JobHandler):
    def get_queues(self):
        return ['Assigned', 'Data']

class JobHandlerA(JobHandler):
    def get_queues(self):
        return ['Assigned', 'Data']

class JobHandlerF(JobHandler):
    def get_queues(self):
        return []

class JobHandlerC(JobHandler):
    def get_queues(self):
        return []

# Implement new state "Suspended"
class JobHandlerS(JobHandler):
    def get_queues(self):
        return ['Suspended', 'Assigned', 'Data']
