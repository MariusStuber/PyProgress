import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyprogress",
    version="0.0.1",
    author="Marius Stuber",
    description="Simple progress indicators for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MariusStuber/PyProgress",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)