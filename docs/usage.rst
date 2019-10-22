=====
Usage
=====

To use merge_fastq in a project::

    import merge_fastq
    merge_fastq(fastq1,fastq2)

To use merge_fastq for command line::

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

Example commandline:

* Using default option for multiple fastq1 and fastq2 files

    .. code-block:: console
    
       $ merge_fastq \
       --fastq1 test_part1_R1.fastq.gz \
       --fastq1 test_part2_R1.fastq.gz \
       --fastq2 test_part1_R2.fastq.gz \
       --fastq2 test_part2_R2.fastq.gz \    
    
    .. code

* Using custom option for multiple fastq1 and fastq2 files

    .. code-block:: console
    
       $ merge_fastq \
       --fastq1 test_part1_R1.fastq.gz \
       --fastq1 test_part2_R1.fastq.gz \
       --fastq2 test_part1_R2.fastq.gz \
       --fastq2 test_part2_R2.fastq.gz \ 
       --output-path /path/to/where/you/want/output
       --out-fastq1 test_merged_R1.fastq.gz
       --out-fastq2 test_merged_R2.fastq.gz   
    
    .. code
