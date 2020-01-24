import setuptools

with open("README.md", "r") as 自述文件:
    长描述 = 自述文件.read()

setuptools.setup(
    name="mulang",
    version="0.0.1",
    author="无名",
    author_email="mulanrevive@gmail.com",
    entry_points = {
        "console_scripts": ['ulang = ulang.runtime.main:main']
        },
    description="描述",
    long_description=长描述,
    long_description_content_type="text/markdown",
    url="https://github.com/MulanRevive/mulan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
)