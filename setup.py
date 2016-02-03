from setuptools import setup

setup(
        name="JSON Generator",
        version="1.0",
        py_modules=['jg'],
        install_requires=[
                'Click',
            ],
        entry_points='''
                [console_scripts]
                jg = jg:cli
            '''
    )
