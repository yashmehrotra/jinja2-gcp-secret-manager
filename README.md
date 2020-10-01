# jinja2-gcp-secret-manager
Jinja2 extension for fetching secrets GCP Secret Manager

# Install

```console
pip install jinja2-gcp-secret-manager
```

## Usage

```
# template.j2
Secret is {% gcp_secret "secret-name" %}


# By default, the latest version is fetched, for specific version use:
2nd version of secret is {% gcp_secret "secret-name" version=2 %}
```

Note: Make sure `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set to the correct file path.
