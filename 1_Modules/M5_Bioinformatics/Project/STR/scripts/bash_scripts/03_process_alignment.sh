#!/usr/bin/env bash
set -euo pipefail

# Using samtools view, we convert the alignments generated in the previous step to (binary) BAM format. 
# Then, with samtools sort, we sort the alignments by their starting coordinates.
# Finally, we generate indices for our alignments with samtools index
samtools view -b ../../data/alignments/APC_mut.sam | samtools sort > ../../data/alignments/APC_mut.bam
samtools index ../../data/alignments/APC_mut.bam

# To save space, we can now remove the uncompressed alignment file
rm ../../data/alignments/APC_mut.sam

# make results dir if it does not exist yet
RESULT_DIR="../../results/"
if [ ! -d ${RESULT_DIR} ]; then
  mkdir ${RESULT_DIR}
fi

# Finally, we generate a consensus sequence from our alignment, which we will use later
samtools consensus -l 60 ../../data/alignments/APC_mut.bam > ../../results/APC_mut_consensus.fa
