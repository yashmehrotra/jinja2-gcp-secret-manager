import setuptools

version = None
with open('jinja2_gcp_secret_manager/__init__.py', 'r') as f:
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
        'Jinja2 < 4',
        'google-cloud-secret-manager < 3',
        # These are dependencies of secret-manager package, had to put
        # them here to make it work
        'google-api-core[grpc] < 2',
        'grpc-google-iam-v1 < 1',
        'proto-plus < 2',
        'libcst >= 0.2.5',
        'protobuf < 4',
        'googleapis-common-protos < 2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
