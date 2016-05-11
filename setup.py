from setuptools import setup

setup(
    name='jumpdir',
    version='0.7.5',
    description='A command line tool for quickly navigating your home directory.',
    author='cgmcintyr',
    author_email='me@cgmcintyre.com',
    url='http://github.com/chrsintyre/jumpdir',
    zip_safe=False,
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
    ],
    keywords='commandline navigation',
    packages=['jumpdir'],
    scripts=['scripts/jumpdir', 'scripts/jumpdir-search'],
    install_requires=[
        'pychalk',
    ],
    test_suite='tests',
)
