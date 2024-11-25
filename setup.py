from setuptools import setup, find_packages

setup(
    name="python-datetimehelper",
    version="0.0.3",
    description="A utility library for working with dates and timezones",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Kiran Ingale",
    author_email="kiraningale012@gmail.com",
    url="https://github.com/kiraningale012/python-datetimehelper",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pytz"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
