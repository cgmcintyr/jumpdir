from setuptools import setup

setup(
    name='jumpdir',
    version='0.1',
    description='A command line tool for quickly navigating your home directory.',
    author='chrsintyre',
    author_email='chrsintyre@gmail.com',
    url='http://github.com/chrsintyre/jumpdir',
    zip_safe=False,

    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='commandline navigation',

    packages=['jumpdir'],
    scripts=['scripts/jumpdir'],
)
