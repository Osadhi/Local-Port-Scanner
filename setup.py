from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='local-port-scanner',
    version='0.0.2',
    packages=find_packages(),
    url='https://github.com/Osadhi/Local-Port-Scanner',
    license='',
    author='Osadhi Virochana',
    author_email='virochana.osadhi@gmail.com',
    description='Simple local port scanner',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
