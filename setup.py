from setuptools import setup
from pathlib import Path
from bcml.__version__ import VERSION

with open("docs/README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="bcml",
    version=VERSION,
    author="NiceneNerd",
    author_email="macadamiadaze@gmail.com",
    description="A mod manager for The Legend of Zelda: Breath of the Wild on Cemu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NiceneNerd/BCML",
    include_package_data=True,
    packages=["bcml"],
    entry_points={"gui_scripts": ["bcml = bcml.__main__:main"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.7",
    install_requires=[
        "aamp>=1.4.1",
        "byml>=2.3.1",
        "cefpython3>=66.0",
        "oead>=1.1.1",
        "pywebview>=3.2,<4.0",
        "pyYaml>=5.3.1",
        "rstb>=1.2.0",
        "xxhash>=1.4.3",
    ],
    zip_safe=False,
)
