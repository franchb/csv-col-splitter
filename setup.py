# -*- coding: utf-8 -*-
from setuptools import setup

install_requires = [
    ]

dev_requires = [
            "pytest",
            "pytest-benchmark",
            "click",
        ]

setup(
    name="csv_col_splitter",
    version="0.0.1",
    packages=["csv_col_splitter"],
    install_requires=install_requires,
    extras_require={
        "dev": dev_requires
    },
    description="Split CSV by columns with optional callbacks.",
    long_description="Split CSV by columns with optional applying per-row callback function.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: MIT ",
        "Natural Language :: Russian",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="csv etl column",
    url="https://gitlab.com/scorista/data_science/stop_factor_search",
    include_package_data=True,
    author="Ilya Rusin",
    author_email="ilya.rusin@protonmail.com",
    license="MIT",
)
