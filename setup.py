from setuptools import setup 

setup(
    name="HANK",
    version="1.0",
    py_modules=['hank'],
    install_requires=[
        'Click',
        'math',
        'googlesearch',
        'datetime',
        'tqdm',
        'progressbar',
        'time',
        'random'
    ],
    entry_points='''
        [console_scripts]
        hank=hank:cli
    ''',
)
