import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AdvertsAPI",
    version="0.0.1",
    author="Ahmed Hamed Aly",
    author_email="hamedala@tcd.ie",
    description="An unofficial API for the community based Irish marketplace, adverts.ie",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ahmedhamedaly/Adverts-API",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)