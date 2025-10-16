from setuptools import setup, find_packages

setup(
    name="ACIT4420_Assignment2_MaiVu",
    version="0.1",
    packages=find_packages(),
    py_modules=['main'],
    include_package_data=True,
    description="ACIT4420 - Assignment 2",
    author="Mai Vu",
    install_requires=[
        "schedule"
    ],
    entry_points={
        'console_scripts': [
            'study-reminders=main:main',
        ],
    },
)