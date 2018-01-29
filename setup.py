try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This package is used for scraping sports analytics data from the foot-data API to provide football'
                   'data of all major european in a machine-readable way.',
    'author': 'Devante Wilson',
    'author_email': 'devante.wilson@outlook.com',
    'version': '0.0.1',
    'packages': find_packages(),
    'name': 'soccer_package'
}

setup(**config)