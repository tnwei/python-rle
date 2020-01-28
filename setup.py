import setuptools

with open('README.md', "r") as f:
    long_description = f.read()

setuptools.setup(
    name='python-rle', 
    version="0.0.3",
    author="Tan Nian Wei",
    author_email="tannianwei@aggienetwork.com",
    description="Run-length encoding for data analysis in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tnwei/pyrle",
    packages=setuptools.find_packages(),
    install_requires=[
          "tqdm",
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)