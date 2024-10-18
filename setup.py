from setuptools import setup, find_packages

setup(
    name='fs_store',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        fs-store=cli.fs_store:cli
    ''',
)
