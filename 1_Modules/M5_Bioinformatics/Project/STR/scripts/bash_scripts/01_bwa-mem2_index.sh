#!/usr/bin/env bash
set -euo pipefail

# Before we can align the reads to the reference with bwa-mem2, we need 
# to generate an index for the reference sequence
bwa-mem2 index ../../data/reference/APC.fa
