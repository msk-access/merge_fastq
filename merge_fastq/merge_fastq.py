# -*- coding: utf-8 -*-

import os
import logging
import shutil

"""
merge_fastq
~~~~~~~~~~~~~~~
:Description: main module for merge_fastq
"""
"""
Created on October 21, 2019
Description: main module for merge_fastq
@author: Ronak H Shah
"""

# Making logging possible
logger = logging.getLogger("merge_fastq")


def run(fastq1, fastq2, output_path, out_fastq1, out_fastq2):
    out_file1 = os.path.join(output_path, out_fastq1)
    out_file2 = os.path.join(output_path, out_fastq2)
    if(len(fastq1) == len(fastq2)):
        if len(fastq1) == 1:
            logging.info(
                "As there is only single pair of fastq files we will copy them to new name.")
            try:
                shutil.copyfile(fastq1[0], out_file1)
            except shutil.Error as e:
                logging.error(
                    "Could not copy file %s to %s, please see the execution error. \n %s \n", fastq1[0], out_file1, e)
                exit(1)
            try:
                shutil.copyfile(fastq2[0], out_file2)
            except shutil.Error as e:
                logging.error(
                    "Could not copy file %s to %s, please see the execution error. \n %s \n", fastq2[0], out_file2, e)
                exit(1)
            logging.info("Done merging fastq file to %s and %s",
                         out_file1, out_file2)
        else:
            merge_fastq(fastq1, fastq2, out_file1, out_file2)
            logging.info("Done merging fastq file to %s and %s",
                         out_file1, out_file2)

    else:
        logger.error("The program expects that the same number of fastq are provided for READ1 and READ2, current they dont match. \n\n ### READ1 ### \n %s \n ### READ2 ### \n %s \n", fastq1, fastq2)
        exit(1)


def merge_fastq(fastq_list_R1, fastq_list_R2, out_file1, out_file2):
    # READ1
    with open(out_file1, 'wb') as outfile1:
        for fq1 in fastq_list_R1:
            with open(fq1, 'rb') as infile1:
                shutil.copyfileobj(infile1, outfile1)
    # READ2
    with open(out_file2, 'wb') as outfile2:
        for fq2 in fastq_list_R2:
            with open(fq2, 'rb') as infile2:
                shutil.copyfileobj(infile2, outfile2)
    return
