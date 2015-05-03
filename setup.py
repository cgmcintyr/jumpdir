from setuptools import setup

setup(name='jumpdir',
      version='0.1',
      description='A command line tool for quickly navigating your home directory.',
      url='http://github.com/chrsintyre/jumpdir',
      author='chrsintyre',
      author_email='chrsintyre@gmail.com',
      license='MIT',
      packages=['jumpdir'],
      scripts=['scripts/jumpdir'],
      zip_safe=False
      )

