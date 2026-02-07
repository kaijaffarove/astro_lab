from setuptools import setup, find_packages

setup(
    name='astrolab_functions',
    version='1.0',
    description='A useful module',
    author='Kai Jaffarove',
    package_dir={"": "src"},
    packages=find_packages(where="src"), # Automatically discovers packages
    python_requires='>=3.6',
)
