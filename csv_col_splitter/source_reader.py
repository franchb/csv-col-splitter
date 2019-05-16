from pathlib import Path
import queue
from concurrent.futures import ThreadPoolExecutor
from typing import List, Optional

from .task import Task

THREAD_LIMIT = 5


class SourceReader:
    """Reads source files."""
    _features: List[str]

    def __init__(self, path: str, buffer_size: int = 300, task: Optional[Task] = None):
        """Prepare reader metadata.

        :param path:
            a full path to a folder with tasks
        :param buffer_size:
            number of rows to be read in one bulk operation.
        """
        self._buffer_size = buffer_size
        self.splits_in_task = 0
        self.base_path = Path(path)
        self.tasks = {}
        if task:
            self.add_task(task)
        self._q = queue.Queue()

    def add_task(self, task: Task):
        """Add task and load features names from header.

        :param task:
            prepared task containing metadata
        :return:
        """
        name = task.path.stem
        if len(task.files) == 0:
            raise ValueError(f"Task {name} contains no files to process.")
        if self.splits_in_task == 0:
            self.splits_in_task = len(task.files)
        else:
            if self.splits_in_task != len(task.files):
                raise ValueError(f"Task {name} contains {len(task.files)} "
                                 f"files to process, but {self.splits_in_task} were expected.")
        self.tasks[name] = task
        with task.files[0].open() as f:
            self.tasks[name].features = f.readline().split(self.tasks[name].ext)[1:]

    def load_tasks_headers(self) -> List[str]:
        """Read first line of a task file and parse features names.

        :return:
            a list with features names in the same order as in task files
        """
        self._features = [t.features for t in self.tasks.values()]
        return self._features

    def _prepare_queue(self):
        """Put task's files in buckets and arrange a queue for processing."""
        for i in range(self.splits_in_task):
            # Each queue item contains one file per task
            block = {k: v.files[i] for k, v in self.tasks.values()}
            self._q.put(block)

    def chunks(self):
        """Yield chunks of rows of `buffer_size`

        :return:
            a generator of pared rows with features values.
        """
        if not self._features:
            raise ValueError("Features list is empty")
        self._prepare_queue()

        while not self._q.empty():
            block = self._q.get()
            descriptors = {t: f.open(encoding=self.tasks[t].encoding)
                           for t, f in block.items()}
            for f in descriptors.values():
                f.readline()  # skip header

            eof = False

            while not eof:
                values = {t: [] for t in self.tasks}
                check_dims = []
                for t, f in descriptors.items():
                    for i in range(self._buffer_size):
                        line = f.readline()
                        if line == '':
                            eof = True
                            break
                        values[t].append(line.split(self.tasks[t].sep)[1:])
                        check_dims.append(i)
                if len(set(check_dims)) > 1:
                    raise RuntimeError("Dataset dimensions mismatched during pre-processing.")
                yield values
            for f in descriptors.values():
                f.close()

    def run(self):
        with ThreadPoolExecutor(max_workers=THREAD_LIMIT) as executor:
            pass
