import setuptools

with open("README.md", encoding="utf-8", mode="r") as readme:
    longDescription = readme.read()

setuptools.setup(
    name="mulang",
    version="0.0.12",
    author="无名",
    author_email="mulanrevive@gmail.com",
    entry_points = {
        "console_scripts": ['木兰 = ulang.runtime.main:main']
        },
    description="木兰编程语言演示",
    long_description=longDescription,
    long_description_content_type="text/markdown",
    url="https://github.com/MulanRevive/mulan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'codegen',
        'rply',
    ],
)