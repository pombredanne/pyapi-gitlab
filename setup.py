# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
setup(
    name = "pyapi-gitlab",
    version = "develop",
    packages = find_packages(),
    install_requires = ['requests', 'markdown'],
    # metadata for upload to PyPI
    author = "Itxaka Serrano Garcia",
    author_email = "itxakaserrano@gmail.com",
    description = "Gitlab API wrapper for Gitlab X.X",
    license = "GPL3",
    keywords = "gitlab git wrapper",
    url = "http://github.com/itxaka/pyapi-gitlab/",
)
