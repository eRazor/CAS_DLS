#!/bin/env/bash
set -euo pipefail

# ENSG00000134982 is the Ensembl ID of the human APC gene
grep "ENSG00000134982" ../../../../data/genome_annotations/gencode.v22.annotation.gtf > APC.gtf

head -n 1 APC.gtf > canonical_transcript.gtf #This should get the 'gene' entry for APC
grep "ENST00000257430" APC.gtf >> canonical_transcript.gtf #ENST00000257430 is the Ensembl ID of the canonical transcript

# The APC sequence that is used as reference for this project starts at chr5 position 112702498 (includes 5kb upstream as promoter sequence)
# Therefore: subtract 112702498 from start and end positions, and sort GTF entries by start position
awk 'BEGIN { OFS = "\t"} { $4-=112702498; $5-=112702498; print $0}' < canonical_transcript.gtf | sort -n -k 4 > APC_canonical_relative_coordinates.gtf

# bgzip and index gtf file for use in the IGV web app
bgzip APC_canonical_relative_coordinates.gtf
tabix APC_canonical_relative_coordinates.gtf.gz