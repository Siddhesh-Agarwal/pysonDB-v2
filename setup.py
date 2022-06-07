from setuptools import setup, find_packages


setup(
    name="pysondb-v2",
    version="2.1.0",
    author="Adwaith Rajesh",
    author_email="adwaithrajesh3180@gmail.com",
    description="A Simple, Lightweight, Efficent JSON based database for Python.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pysonDB/pysonDB-v2",
    icense="MIT",
    classifiers =[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(),
)
