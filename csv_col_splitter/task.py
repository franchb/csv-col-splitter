from dataclasses import dataclass, field
from pathlib import Path
from typing import List


@dataclass
class Task:
    """Store metadata for a task.

    A task is supposed to be a folder with several files
    with calculated features for a one features base.

    Several tasks in job are supposed to be equal dimensions,
    rows and columns also supposed to be in equal order.
    """

    path: Path
    files: List[Path] = field(init=False, repr=False)
    features: List[str] = field(init=False, repr=False)
    sep: str = ','
    ext: str = '.csv'
    encoding: str = 'utf8'

    def __post_init__(self):
        self.files = list(Path(self.path).glob(self.sep))
