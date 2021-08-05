#!/bin/bash

LOG_DIR='log'
LOG_FILE="${LOG_DIR}/run.log"

mkdir -p "${LOG_DIR}"

python -m scraper.app >> $LOG_FILE 2>&1
