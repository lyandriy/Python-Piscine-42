from setuptools import setup, find_packages

setup(
    name="my_minipack",
    version="1.0.0",
    author="lyandriy",
    author_email="lyandriy@student.42madrid.com",
    description="Howto create a package in python.",
    long_description=open("README.md").read(),
    url=None,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Students",
        "Topic :: Education",
        "Topic :: HowTo",
        "Topic :: Package",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3",
    license="GPLv3",
)