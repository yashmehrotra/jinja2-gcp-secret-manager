# jinja2-gcp-secret-manager

Jinja2 extension for fetching secrets GCP Secret Manager

## Install

```sh
pip install jinja2-gcp-secret-manager
```

## Usage

```jinja2
# template.j2
Secret is {% gcp_secret "secret-name" %}


# By default, the latest version is fetched, for specific version use:
2nd version of secret is {% gcp_secret "secret-name" version=2 %}

# If you are using Application default credentials or want to explicitly specify
the project where the secrets should be found, add the `project` term:
3rd version of secret is {% gcp_secret "secret-name" version=2 project="abc123" %}
```

## GCP Setup

For this to work, make sure you either setup the `GOOGLE_APPLICATION_CREDENTIALS` environment variable set to the correct file path or use Application default credentials.  See [https://google-auth.readthedocs.io/en/latest/user-guide.html](https://google-auth.readthedocs.io/en/latest/user-guide.html) for more details.

Note: If you use Application default credentials, you will need to specify project in all `gcp_secret` tags as default project cannot be determined as it can with a service account.
