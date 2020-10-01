__version__ = '1.0.0'
__author__ = 'Yash Mehrotra'
__license__ = 'Apache 2.0'

import json
import os

from jinja2 import nodes
from jinja2.ext import Extension
from google.cloud import secretmanager

if not (credentials := os.getenv('GOOGLE_APPLICATION_CREDENTIALS')):
    raise Exception(
        'Need to set environment variable GOOGLE_APPLICATION_CREDENTIALS')

CLIENT = secretmanager.SecretManagerServiceClient()
PROJECT_ID = json.load(open(credentials))['project_id']


class GoogleSecretManager(Extension):
    tags = {'gcp_secret'}

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        name = parser.parse_expression()

        parser.stream.skip_if('comma')
        version = nodes.Const('latest')
        if parser.stream.skip_if('name:version'):
            parser.stream.skip(1)
            version = parser.parse_expression()

        args = (name, version)

        return nodes.Output([
            self.call_method('_access_secret', args)], lineno=lineno)

    def _access_secret(self, name, version):
        return CLIENT.access_secret_version(request={
            'name': f'projects/{PROJECT_ID}/secrets/{name}/versions/{version}'
        }).payload.data.decode('utf-8')
