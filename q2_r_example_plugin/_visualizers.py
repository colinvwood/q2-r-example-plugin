# ----------------------------------------------------------------------------
# Copyright (c) 2024, A QIIME 2 Plugin Developer.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ---------------------------------------------------------------------------
import importlib.resources
from pathlib import Path
import shutil
import subprocess
import tempfile

import pandas as pd


def plot_sorted_samples(output_dir: str, table: pd.DataFrame) -> None:
    with tempfile.TemporaryDirectory() as tempdir:
        input_fp = Path(tempdir) / 'input-table.csv'
        visualization_fp = Path(tempdir) / 'figure.svg'

        table.reset_index(inplace=True, names='id')
        table.to_csv(input_fp, index=False)

        subprocess.run(['barplot.R', str(input_fp), str(visualization_fp)])

        index = importlib.resources.files(__package__) / 'assets' / 'index.html'
        shutil.copy(index, output_dir)
        shutil.copy(visualization_fp, output_dir)
