#!/usr/bin/env python
"""Tests for `dotdash` package."""

import pytest
import re

from click.testing import CliRunner

from dotdash import cli, __version__


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    del response

def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'dotdash' in result.output

    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help     Show this message and exit.' in help_result.output

    version_result = runner.invoke(cli.main, ['--version'])
    assert version_result.exit_code == 0
    assert f'main, version {__version__}' in version_result.output

def test_commands_exists():
    """Test existence of each command"""
    commands = [
        "adopt",
        "archive",
        "check",
        "evict",
        "init",
        "mv",
        "reset",
        "sync",
    ]

    for cmd in commands:
        runner = CliRunner()
        result = runner.invoke(cli.main, [cmd, "--help"])
        assert result.exit_code == 0, \
            f"Command {cmd}, expected exit code 0, got {result.exit_code}"

