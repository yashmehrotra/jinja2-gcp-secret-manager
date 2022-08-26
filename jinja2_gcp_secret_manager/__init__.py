__version__ = '1.2.0'
__author__ = 'Yash Mehrotra'
__license__ = 'Apache 2.0'

import json
import os

from jinja2 import nodes
from jinja2.ext import Extension
import google.auth
from google.cloud import secretmanager


class GoogleSecretManager(Extension):
    tags = {'gcp_secret'}

    def __init__(self, environment):
        _, self.project_id = google.auth.default()
        self.client = secretmanager.SecretManagerServiceClient()

        super().__init__(environment)

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        name = parser.parse_expression()

        parser.stream.skip_if('comma')
        version = nodes.Const('latest')
        project = nodes.Const(self.project_id)

        if parser.stream.skip_if('name:version'):
            parser.stream.skip(1)
            version = parser.parse_expression()

        if parser.stream.skip_if('name:project'):
            parser.stream.skip(1)
            project = parser.parse_expression()

        if (not isinstance(project, nodes.Const)) or (not project.value):
            parser.fail("Project not specified", lineno=lineno)

        args = (name, version, project)

        return nodes.Output(
            [self.call_method('_access_secret', args)], lineno=lineno
        )

    def _access_secret(self, name, version, project):
        return self.client.access_secret_version(request={
            'name': f'projects/{project}/secrets/{name}/versions/{version}'
        }).payload.data.decode('utf-8')
