from setuptools import setup


setup(
  name='m42pl-encoders',
  author='@jpclipffel',
  url='https://github.com/jpclipffel/m42pl-encoders',
  version='1.0.0',
  packages=['m42pl_encoders',],
  install_requires=[
    'msgpack>=1.0.3',
    'msgpack-numpy>=0.4.7.1'
  ]
)
