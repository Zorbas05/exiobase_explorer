from setuptools import setup, find_packages

setup(
    name="exiobase_explorer",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "exiobase_explorer": [
            "config/*",
            "data/*",
        ]
    },
    include_package_data=True,
    install_requires=[
        "pandas",
        "matplotlib",
        "numpy",
        "geopandas",
        "mapclassify",
        "tk",
    ],
    python_requires=">=3.8",
)
