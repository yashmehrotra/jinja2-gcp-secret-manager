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
        'Jinja2==2.11.3',
        'google-cloud-secret-manager==2.2.0',
        # These are dependencies of secret-manager package, had to put
        # them here to make it work
        'google-api-core[grpc]==1.25.1',
        'grpc-google-iam-v1==0.12.3',
        'proto-plus==1.13.0',
        'libcst >= 0.2.5',
        'protobuf==3.14.0',
        'googleapis-common-protos==1.52.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
