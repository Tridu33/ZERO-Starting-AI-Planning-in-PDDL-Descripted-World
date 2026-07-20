#!/bin/bash
DOMAIN_NAME=${1} 
python3 ./prp-scripts/translate_policy.py > ./solutionsByPRP/fond_${DOMAIN_NAME}_human_policy.out