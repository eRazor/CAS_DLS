#!/usr/bin/env bash
set -euo pipefail

# create a directory to store our alignments in
ALIGN_DIR="../../data/alignments/"
if [ ! -d ${ALIGN_DIR} ]; then
  mkdir ${ALIGN_DIR}
fi


# Perform the alignment for the reads against the reference sequence
bwa-mem2 mem \
-R '@RG\tID:sim20230508\tPL:wgsim\tSM:mut' \
-t 4 ../../data/reference/APC.fa ../../data/reads/APC_mut_out1.fq.gz ../../data/reads/APC_mut_out2.fq.gz \
> ../../data/alignments/APC_mut.sam
