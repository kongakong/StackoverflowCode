#!/bin/bash
set -eo pipefail

echo "Setting traps..."
trap 'cleanup_term' TERM
trap 'cleanup_kill' KILL

cleanup_term() {
    echo "Sending term to `jobs -p`..."
    kill -TERM `jobs -p`
    kill -USR1 `jobs -p`
}

cleanup_kill() {
    echo "Received kill..."
    kill -TERM `jobs -p`
}


service ntp start

cd /app
python -m greatapp &

wait

