import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='humai_utils',
    version='0.1.0',
    author='David Nicolas',
    author_email='davidnicsamm@yahoo.com',
    description='A compilation of Humai utility functions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/davidnicsamm/humai_utils',
    project_urls = {
        "Bug Tracker": "https://github.com/davidnicsamm/humai_utils/issues"
    },
    license='MIT',
    packages=['humai_utils'],
    install_requires=['requests'],
)
