import setuptools

version = None
with open('jinja2-gcp-secret-manager/__init__.py', 'r') as f:
    for line in f.readlines():
        if '__version__' in line:
            version = line.split('=')[1].replace('\'', '').strip()

setuptools.setup(
    name="jinja2-gcp-secret-manager",
    version=version,
    author="Yash Mehrotra",
    author_email="yashmehrotra95@gmail.com",
    description="Jinja2 extension for fetching secrets GCP Secret Manager",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yashmehrotra/jinja2-gcp-secret-manager",
    packages=setuptools.find_packages(),
    license='Apache 2.0',
    install_requires=[
        'google-cloud-secret-manager>=2.0.0',
        'Jinja2>=2.11.2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
