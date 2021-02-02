__version__ = '1.1.0'
__author__ = 'Yash Mehrotra'
__license__ = 'Apache 2.0'

import json
import os

from jinja2 import nodes
from jinja2.ext import Extension
import google.auth
from google.cloud import secretmanager

credentials, PROJECT_ID = google.auth.default()
CLIENT = secretmanager.SecretManagerServiceClient()


class GoogleSecretManager(Extension):
    tags = {'gcp_secret'}

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        name = parser.parse_expression()

        parser.stream.skip_if('comma')
        version = nodes.Const('latest')
        if not PROJECT_ID:
            parser.fail("Project not specified", lineno=lineno)
        project = nodes.Const(PROJECT_ID)

        if parser.stream.skip_if('name:version'):
            parser.stream.skip(1)
            version = parser.parse_expression()

        if parser.stream.skip_if('name:project'):
            parser.stream.skip(1)
            project = parser.parse_expression()


        args = (name, version, project)

        return nodes.Output(
            [self.call_method('_access_secret', args)], lineno=lineno
        )

    def _access_secret(self, name, version, project):
        return CLIENT.access_secret_version(request={
            'name': f'projects/{project}/secrets/{name}/versions/{version}'
        }).payload.data.decode('utf-8')
