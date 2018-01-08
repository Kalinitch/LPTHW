try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Anna',
    'url': 'https://github.com/Kalinitch/LPTHW',
    'download_url': 'https://github.com/Kalinitch/LPTHW',
    'author_email': 'Anna.Kalinina',
    'version':'0.1',
    'install_requires': ['nose'],
    'packages': ['Ex47'],
    'scripts': [],
    'name': 'Ex47'
}

setup(**config)
