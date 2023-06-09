from setuptools import find_packages, setup

root_package = "datastructures"
setup(
    name='datastructuresLionelEric',
    packages=([root_package] + [f"{root_package}.{item}" for item in find_packages(where=root_package)]),
    version='2.44',
    description='My first Python library',
    author='Me',
    license='MIT',
     package_dir={
        "": ".",
        "Linear": "./datastructures/Linear",
        "nodes": "./datastructures/nodes",
        "trees": "./datastructures/trees",
    },
)


