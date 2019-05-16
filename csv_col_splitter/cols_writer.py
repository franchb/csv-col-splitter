from pathlib import Path
from typing import List


class ColsWriter:
    """Writes each column in separate `csv` file."""
    features: List[str]

    def __init__(self, path: Path, output: str = 'output', ext: str = '.csv', sep: str = ','):
        self._ext = ext
        self._sep = sep
        self._output = path / output

        if self._output.is_dir():
            is_empty = False if sorted(self._output.rglob('*')) else True
            if not is_empty:
                raise OSError(f"Output path is not empty: {str(self._output)}")
        else:
            self._output.mkdir()

    def prepare_output(self, features):
        """Create empty file for each feature in tasks."""
        self.features = features
        for f in features:
            open(self._output / (f + self._ext), 'w').close()

    def write(self, values: List[List[str]]):
        #for base in values:
        pass

    def _put_fields_by_chunks(self, buffer: List[str]):
#        for i in range(len(files)):
#            line = ','.join([b[i] for b in buffer]) + last
#            with open(OUTPUT + files[i] + '.csv', 'a') as f:
#                f.write(line)
        pass