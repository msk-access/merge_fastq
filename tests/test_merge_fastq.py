#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `merge_fastq` package."""

import os
import pytest
import subprocess
from click.testing import CliRunner
from merge_fastq import merge_fastq
from merge_fastq import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    #result = runner.invoke(cli.main)
    #assert result.exit_code == 0
    #assert 'merge_fastq.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0


def test_multi_fastq():
    cmd = [
        "merge_fastq",
        "--fastq1",
        "data/test/test_R1_001.fastq.gz",
        "--fastq1",
        "data/test/test_R1_002.fastq.gz",
        "--fastq1",
        "data/test/test_R1_003.fastq.gz",
        "--fastq2",
        "data/test/test_R2_001.fastq.gz",
        "--fastq2",
        "data/test/test_R2_002.fastq.gz",
        "--fastq2",
        "data/test/test_R2_003.fastq.gz",
        "--out-fastq1",
        "test_R1_merged.fastq.gz",
        "--out-fastq2",
        "test_R2_merged.fastq.gz"

    ]
    ret_code = run_cmd(cmd)
    assert ret_code == 0
    assert os.path.isfile("test_R1_merged.fastq.gz") is True
    assert os.path.isfile("test_R2_merged.fastq.gz") is True


def test_single_fastq():
    cmd = [
        "merge_fastq",
        "--fastq1",
        "data/test/test_R1_001.fastq.gz",
        "--fastq2",
        "data/test/test_R2_001.fastq.gz",
    ]
    ret_code = run_cmd(cmd)
    assert ret_code == 0
    assert os.path.isfile("merged_fastq_R1.fastq.gz") is True
    assert os.path.isfile("merged_fastq_R2.fastq.gz") is True
    


def run_cmd(cmd):
    print("Command:", cmd)
    process = subprocess.Popen(
        cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output, errors = process.communicate()
    ret_code = process.wait()
    return ret_code
