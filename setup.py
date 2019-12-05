"""
SL_ds_resources - A collection of DS resources I keep finding my way back to!
"""
import setuptools

REQUIRED = [
    "numpy",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    setuptools.setup(
        name="SL_ds_resources",
        version="0.0.1",
        author="SLightfoot",
        author_email="ScottLightfoot@users.noreply.github.com",
        description="A collection of DS resources I keep finding my way back to!",
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        url="https://github.com/ScottLightfoot/SL_ds_resources.git",
        packages=setuptools.find_packages(),
        python_requires=">=3.5",
        install_requires=REQUIRED,
        classifiers=["Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                     ]
    )
