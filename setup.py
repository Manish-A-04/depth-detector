from setuptools import setup,find_packages

__version__ = "0.0.1"

AUTHOR_USERNAME = "Manish-A-04"
AUTHOR_EMAIL = "manishprofessional04@gmail.com"
SOURCE_REPO = "depth-detector"

with open("README.md","r",encoding="utf-8") as r:
    description = r.read()

setup(
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    version=__version__,
    name=SOURCE_REPO,
    description="This is a python packege for detecting depth from images.",
    long_description=description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{SOURCE_REPO}",
    package_dir={"":"src"},
    packages=find_packages(where="src")
)
