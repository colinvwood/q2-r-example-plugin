# ----------------------------------------------------------------------------
# Copyright (c) 2024, Colin Wood.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
from pathlib import Path
import subprocess
import tempfile

import pandas as pd


def randomize_frequencies(table: pd.DataFrame) -> pd.DataFrame:
    with tempfile.TemporaryDirectory() as tempdir:
        input_fp = Path(tempdir) / 'input-table.csv'
        output_fp = Path(tempdir) / 'output-table.csv'

        table.reset_index(inplace=True, names='id')
        table.to_csv(input_fp, index=False)

        subprocess.run(['randomize.R', str(input_fp), str(output_fp)])

        table = pd.read_csv(output_fp, index_col='id')

    return table
