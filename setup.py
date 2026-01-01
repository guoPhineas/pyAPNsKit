import setuptools

with open("./docs/pypi.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def parse_requirements(filename):
    with open(filename, "r", encoding="utf-8") as f:
        requirements = []
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if line.startswith("-e"):
                requirements.append(line.split("#egg=")[1])
            else:
                requirements.append(line)
    return requirements

setuptools.setup(
    name="pyAPNsKit",
    version="0.1.3",
    author="Zonglin Phineas Guo",
    description="Send requests to Apple Push Notification service (APNs) to push notifications to users.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.12',
    license = "Apache",
    project_urls={
        
        "Source": "https://github.com/guoPhineas/pyAPNsKit/",
        "Tracker": "https://github.com/guoPhineas/pyAPNsKit/issues/",
    },
    classifiers=[
        "Topic :: Software Development",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 3",
    ],
    install_requires=parse_requirements("requirements.txt"),
)