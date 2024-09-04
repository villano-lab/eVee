from setuptools import setup

setup(
    name = 'eVee',
    version = '0.1',
    description = 'A package for yield models',
    url = 'https://github.com/villano-lab/eVee',
    author = 'A.N. Villano; Kitty C. Mickelson',
    author_email = 'kathryn.harris@ucdenver.edu',
    license = 'MIT',
    packages = ['lindhard'],
    install_requires = [],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
