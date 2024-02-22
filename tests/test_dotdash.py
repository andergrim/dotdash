#!/usr/bin/env python
"""Tests for `dotdash` package."""
import pytest
import os

from click.testing import CliRunner

from dotdash import cli, __version__

""" Helpers """
@pytest.fixture(scope="session")
def temp_home(tmp_path_factory):
    """Create a home directory in temp dir."""
    return tmp_path_factory.mktemp("home") / "user"

@pytest.fixture(scope="session")
def temp_dotfiles(temp_home):
    """Create a dotfiles dir in the home directory."""
    conf_dir = temp_home / "dotfiles"
    conf_dir.mkdir(parents=True, exist_ok=True)
    return conf_dir

""" CLI sanity checks """
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

""" Configuration """
def test_no_config_return_empty_config():
    """With no config pointed out, config should be empty."""
    cfg = cli.get_config()
    assert len(cfg) == 0

def test_correct_config_finds_dotfiles_dir(temp_dotfiles):
    """With config set, should be retrievable."""
    dotfiles_dir = str(temp_dotfiles)
    os.environ["DOTFILES"] = dotfiles_dir

    cfg = cli.get_config()
    assert cfg["DOTFILES"] == dotfiles_dir
    os.environ["DOTFILES"] = ""

