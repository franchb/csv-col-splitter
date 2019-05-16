from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import threading
import queue

from .source_reader import SourceReader
from .cols_writer import ColsWriter
from .task import Task
from pathlib import Path


def a(path: str):
    path = Path(path)
    writer = ColsWriter(path.parent / "output")
    reader = SourceReader(path=path, buffer_size=300)

    for p in reader.base_path.glob('**/'):
        reader.add_task(Task(p))
    features = reader.load_tasks_headers()
    writer.prepare_output(features)
    for buf in reader.chunks():
        writer.write(buf)
    # {p.stem: Task(p, self._sep) for p in self._base_path.glob('**/')}


# class ThreadUrl(threading.Thread):
#     def __init__(self,queue):
#         threading.Thread.__init__(self)
#         self.queue = queue
#
#     def run(self):
#         while True:
#             inpfile, outfile = self.queue.get()
#             workermethod(inpfile, outfile)
#
#
# q = queue.Queue
# threadpool = [ThreadUrl(q) for i in range(poolsize)]
# q.put((inpfile, outfile))