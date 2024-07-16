# ----------------------------------------------------------------------------
# Copyright (c) 2024, A QIIME 2 Plugin Developer.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ---------------------------------------------------------------------------
import pandas as pd

from qiime2.plugin.testing import TestPluginBase
from qiime2 import Artifact

from q2_r_example_plugin._methods import randomize_frequencies


class TestMethods(TestPluginBase):
    package = 'q2_r_example_plugin.tests'

    def setUp(self):
        table_fp = self.get_data_path('table.qza')
        self.table = Artifact.load(table_fp)

    def tearDown(self):
        pass

    def test_randomize_frequencies(self):
        input_table = self.table.view(pd.DataFrame)
        output_table = randomize_frequencies(input_table.copy())

        self.assertEqual(output_table.shape, input_table.shape)
        self.assertEqual(set(output_table.index), set(input_table.index))
        self.assertEqual(set(output_table.columns), set(input_table.columns))

        some_feature_id = output_table.columns[0]
        comparison = (
            output_table[some_feature_id] == input_table[some_feature_id]
        )
        self.assertTrue(not comparison.all())
