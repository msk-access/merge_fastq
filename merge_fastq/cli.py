# -*- coding: utf-8 -*-

import os
import sys
import logging
import time
import pathlib
try:
    import click
except ImportError as e:
    print(
        "cli: click is not installed, please install click as it is one of the requirements. \n", e
    )
    exit(1)
try:
    import click_log
except ImportError as e:
    print(
        "cli: click-log is not installed, please install click_log as it is one of the requirements.\n", e
    )
    exit(1)
try:
    import merge_fastq.merge_fastq as mf
except ImportError as e:
    print(
        "cli: merge_fastq module could not be loaded, please install package correctly to get this running. \n", e
    )
    exit(1)

"""
cli
~~~~~~~~~~~~~~~
:Description: console script for running merge_fastq
"""
"""
Created on October 10, 2019
Description: console script for running merge_fastq
@author: Ronak H Shah
"""

version = None
scriptpath = os.path.realpath(__file__)
p_scriptpath = pathlib.Path(scriptpath)
with open(os.path.join(p_scriptpath.parent, "__init__.py"), "r") as f:
    for line in f.readlines():
        line = line.strip()
        if line.startswith("__version__"):
            version = line.split("=")[-1].strip()
__all__ = []
__version__ = version
__date__ = "2019-10-21"
__updated__ = "2019-10-21"
# Making logging possible
logger = logging.getLogger("merge_fastq")
click_log.basic_config(logger)
click_log.ColorFormatter.colors["info"] = dict(fg="green")


@click.command()
@click.option(
    "--fastq1",
    "-fp1",
    required=True,
    multiple=True,
    type=click.Path(exists=True),
    help="Full path to gziped READ1 fastq files, can be specified multiple times for example: --fastq1 test_part1_R1.fastq.gz --fastq1 test_part2_R1.fastq.gz",
)
@click.option(
    "--fastq2",
    "-fp2",
    required=True,
    multiple=True,
    type=click.Path(exists=True),
    help="Full path to gziped READ2 fastq files, can be specified multiple times for example: --fastq2 test_part1_R2.fastq.gz --fastq2 test_part2_R2.fastq.gz",
)
@click.option(
    "--output-path",
    "-op",
    required=False,
    default=os.getcwd(),
    type=click.Path(exists=True),
    help="Full path to write the output files (default: Current working directory)",
)
@click.option(
    "--out-fastq1",
    "-of1",
    required=False,
    default="merged_fastq_R1.fastq.gz",
    type=click.STRING,
    help="Name of the merged output READ1 fastq file (default: merged_fastq_R1.fastq.gz)",
)
@click.option(
    "--out-fastq2",
    "-of2",
    required=False,
    default="merged_fastq_R2.fastq.gz",
    type=click.STRING,
    help="Name of the merged output READ2 fastq file (default: merged_fastq_R2.fastq.gz)",
)
def main(fastq1, fastq2, output_path, out_fastq1, out_fastq2):
    """Console script for merge_fastq."""
    logger_output = os.path.join(output_path, "merge_fastq.log")
    fh = logging.FileHandler(logger_output)
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info("==================================================")
    logger.info(">>> Running merge_fastq for <<<")
    logger.info("==================================================")
    t1_start = time.perf_counter()
    t2_start = time.process_time()
    mf.run(fastq1, fastq2, output_path, out_fastq1, out_fastq2)
    t1_stop = time.perf_counter()
    t2_stop = time.process_time()
    logger.info("--------------------------------------------------")
    logger.info("Elapsed time: %.1f [min]" % ((t1_stop - t1_start) / 60))
    logger.info("CPU process time: %.1f [min]" % ((t2_stop - t2_start) / 60))
    logger.info("--------------------------------------------------")
    return 0


if __name__ == "__main__":
    sys.exit(main())
