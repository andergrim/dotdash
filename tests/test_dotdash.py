#!/usr/bin/env python
"""Tests for `dotdash` package."""
import pytest
import os
import shutil
from pathlib import Path

from click.testing import CliRunner

from dotdash import cli, __version__

""" Helpers """
@pytest.fixture(scope="session")
def temp_home(tmp_path_factory):
    return tmp_path_factory.mktemp("home") / "user"

@pytest.fixture(scope="session")
def temp_dotfiles(temp_home):
    conf_dir = temp_home / "dotfiles"
    conf_dir.mkdir(parents=True, exist_ok=True)
    return conf_dir

@pytest.fixture(autouse=True)
def mock_dotfiles_location(monkeypatch, temp_dotfiles):
    os.environ["DOTFILES"] = str(temp_dotfiles)
    monkeypatch.setenv("DOTFILES", str(temp_dotfiles))


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
def test_no_config_shows_not_initialized_notice():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert "No dotfiles directory initialized, use dotdash init" in result.output

def test_correct_config_shows_dirname():
    env = os.environ.copy()
    env["DOTFILES"] = str(temp_dotfiles)
    runner = CliRunner(env=env)
    result = runner.invoke(cli.main)

    assert f"Dotfiles directory is {str(temp_dotfiles)}" in result.output

def test_bad_config_shows_does_not_exists():
    # monkeypatch.setenv("DOTFILES", "~/notfiles")
    os.environ["DOTFILES"] = str(temp_dotfiles)

    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert "Configured directory ~/notfiles does not exist" in result.output
    # monkeypatch.delenv("DOTFILES")
