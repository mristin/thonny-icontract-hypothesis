import os

import setuptools

here = os.path.abspath(os.path.dirname(__file__))  # pylint: disable=invalid-name

with open(os.path.join(here, "README.rst"), encoding="utf-8") as fid:
    long_description = fid.read()  # pylint: disable=invalid-name

with open(os.path.join(here, "requirements.txt"), encoding="utf-8") as fid:
    install_requires = [line for line in fid.read().splitlines() if line.strip()]

setuptools.setup(
    name="thonny-icontract-hypothesis",
    version="1.0.0a3",
    author="Marko Ristin",
    author_email="marko@ristin.ch",
    description="Automatically test Python code using icontract-hypothesis in Thonny.",
    long_description=long_description,
    url="https://github.com/mristin/thonny-icontract-hypothesis",
    packages=["thonnycontrib.thonny_icontract_hypothesis"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Hypothesis",
        "Development Status :: 5 - Production/Stable",
    ],
    license="License :: OSI Approved :: MIT License",
    keywords="design-by-contract contracts automatic testing property-based",
    install_requires=install_requires,
    python_requires=">=3.7",
    # fmt: off
    extras_require={
        "dev": [
            "black==20.8b1",
            "mypy==0.812",
            "pylint==2.3.1",
            "pydocstyle>=2.1.1,<3",
            "coverage>=4.5.1,<5",
            "docutils>=0.14,<1",
        ],
    },
    package_data={"thonnycontrib.thonny_icontract_hypothesis": ["py.typed"]},
    # fmt: on
    data_files=[(".", ["LICENSE", "README.rst", "requirements.txt"])],
)
