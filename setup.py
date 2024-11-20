import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


with open("setup/requirements.txt") as f:
    req_paths = f.read().splitlines()
requirements = []
for req_path in req_paths:
    if req_path.startswith("#"):
        continue
    req_path = req_path.replace("-r ", "")
    req_path = os.path.join("setup", req_path)
    with open(req_path) as f:
        requirements += f.read().splitlines()


def get_dirlist(_rootdir):
    dirlist = []

    with os.scandir(_rootdir) as rit:
        for entry in rit:
            if not entry.name.startswith(".") and entry.is_dir():
                dirlist.append(entry.path)
                dirlist += get_dirlist(entry.path)

    return dirlist


# Get subfolders recursively
rootdir = "python-sdk"
packages = [
    d.replace("/", ".").replace("{}.".format(rootdir), "") for d in get_dirlist(rootdir)
]

# Filter out Python cache folders and package info
packages = [
    p for p in packages if not p.endswith("__pycache__") and not p.endswith("egg-info")
]

setuptools.setup(
    name="vod-devkit",
    version="1.0.2",
    author="Hidde Boekema",
    author_email="h.j.boekema@tudelft.nl",
    description="The official devkit of the View-of-Delft Prediction dataset.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tudelft-iv/vod-devkit",
    python_requires=">=3.6",
    install_requires=requirements,
    packages=packages,
    package_dir={"": "python-sdk"},
    package_data={"": ["*.json"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "License :: Free for non-commercial use",
    ],
    license="apache-2.0",
)
