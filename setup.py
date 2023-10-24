from setuptools import setup

description = (
    "Fractions-SSIM"
)

setup(
    name="fssim",
    version="0.1",
    description=description,
    long_description=description,
    author="Bobby Antonio",
    license="MIT",
    packages=["fssim"],
    install_requires=[
        "scipy",
        "numpy"
    ],
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
    ],
)
