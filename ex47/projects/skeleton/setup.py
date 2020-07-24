
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    "description": "My project",
    "author": "zheng jia",
    "url": "URL to get it at.",
    "download_url": "where to download it.",
    "author_email": "604573679@qq.com",
    "version": "0.0.1",
    "install_requires": ["nose"],
    "packages": ["ex47"],
    "scripts": [],
    "name": "projectname"
}

setup(**config)
