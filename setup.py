# ----------------------------------------------------------------------------
# Copyright (c) 2024, Colin Wood.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import find_packages, setup

import versioneer

description = ("A template QIIME 2 plugin.")

setup(
    name="q2-r-example-plugin",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license="BSD-3-Clause",
    packages=find_packages(),
    author="Colin Wood",
    author_email="q2-dev@example.com",
    description=description,
    url="https://example.com",
    scripts=[
        'q2_r_example_plugin/assets/randomize.R',
        'q2_r_example_plugin/assets/barplot.R'
    ],
    entry_points={
        "qiime2.plugins": [
            "q2_r_example_plugin="
            "q2_r_example_plugin"
            ".plugin_setup:plugin"]
    },
    package_data={
        "q2_r_example": ["citations.bib", "assets/index.html"],
        "q2_r_example.tests": ["data/*"],
    },
    zip_safe=False,
)
