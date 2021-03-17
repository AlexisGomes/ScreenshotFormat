import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ScreenshotFormat',
    version='1',
    packages=setuptools.find_packages(),
    author="Gomes Alexis",
    author_email="alexis.gomes19@gmail.com",
    description="Python package to help create screenshot to upload on stores",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexisGomes/ScreenshotFormat",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)