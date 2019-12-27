# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
"""Methods for CLI publish functionality."""

import os
import click
import tarfile

from shutil import copyfile
from typing import Dict

from aea.cli.common import logger
from aea.cli.registry.utils import (
    clean_tarfiles, load_yaml, request_api, get_item_target_path
)
from aea.configurations.base import DEFAULT_AEA_CONFIG_FILE


def _compress(output_filename: str, *filepaths):
    """Compare the output file."""
    with tarfile.open(output_filename, "w:gz") as f:
        for filepath in filepaths:
            f.add(filepath, arcname=os.path.basename(filepath))


def _load_agent_config(agent_config_path: str) -> Dict:
    if not os.path.exists(agent_config_path):
        raise click.ClickException(
            'Agent config not found. Make sure you run push command '
            'from a correct folder.'
        )
    return load_yaml(agent_config_path)


@clean_tarfiles
def publish_agent():
    """Publish an agent."""
    cwd = os.getcwd()
    agent_config_path = os.path.join(cwd, DEFAULT_AEA_CONFIG_FILE)
    agent_config = _load_agent_config(agent_config_path)
    name = agent_config['agent_name']
    output_tar = os.path.join(cwd, '{}.tar.gz'.format(name))
    _compress(output_tar, agent_config_path)

    data = {
        'name': name,
        'description': agent_config['description'],
        'version': agent_config['version']
    }
    path = '/agents/create'
    logger.debug('Publishing agent {} to Registry ...'.format(name))
    resp = request_api(
        'POST', path, data=data, auth=True, filepath=output_tar
    )
    click.echo(
        'Successfully published agent {} to the Registry. Public ID: {}'.format(
            name, resp['public_id']
        )
    )


def save_agent_locally() -> None:
    """
    Save agent to local packages.

    :return: None
    """
    item_type_plural = 'agents'
    cwd = os.getcwd()

    agent_config_path = os.path.join(cwd, DEFAULT_AEA_CONFIG_FILE)
    agent_config = _load_agent_config(agent_config_path)
    name = agent_config['agent_name']

    target_dir = get_item_target_path(item_type_plural, name)
    # TODO: now - copy only config file. Change to copy whole agent.
    source_path = os.path.join(cwd, DEFAULT_AEA_CONFIG_FILE)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)

    target_file = os.path.join(target_dir, DEFAULT_AEA_CONFIG_FILE)
    copyfile(source_path, target_file)
    click.echo(
        'Agent "{}" successfully saved in packages folder.'.format(name)
    )
