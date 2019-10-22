===========
merge_fastq
===========

.. image:: https://img.shields.io/pypi/v/merge_fastq.svg
        :target: https://pypi.python.org/pypi/merge_fastq

.. image:: https://travis-ci.com/msk-access/merge_fastq.svg?branch=master
    :target: https://travis-ci.com/msk-access/merge_fastq

.. image:: https://readthedocs.org/projects/merge-fastq/badge/?version=latest
        :target: https://merge-fastq.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/msk-access/merge_fastq/shield.svg
     :target: https://pyup.io/repos/github/msk-access/merge_fastq/
     :alt: Updates



Package to merge multiple pair of pair-end fastq data


* Free software: Apache Software License 2.0
* Documentation: https://merge-fastq.readthedocs.io.


Features
--------

* Given multiple pair-end fastq data merge them into single pair-end fastq w.r.t each READ1 and READ2 

Usage
-----

> merge_fastq --help

Usage: merge_fastq [OPTIONS]

  Console script for merge_fastq.

Options:
  -fp1, --fastq1 PATH      Full path to gziped READ1 fastq files, can be
                           specified multiple times for example: --fastq1
                           test_part1_R1.fastq.gz --fastq1
                           test_part2_R1.fastq.gz  [required]
  -fp2, --fastq2 PATH      Full path to gziped READ2 fastq files, can be
                           specified multiple times for example: --fastq2
                           test_part1_R2.fastq.gz --fastq2
                           test_part2_R2.fastq.gz  [required]
  -op, --output-path PATH  Full path to write the output files (default:
                           Current working directory)
  -of1, --out-fastq1 TEXT  Name of the merged output READ1 fastq file
                           (default: merged_fastq_R1.fastq.gz)
  -of2, --out-fastq2 TEXT  Name of the merged output READ2 fastq file
                           (default: merged_fastq_R2.fastq.gz)
  --help                   Show this message and exit.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
