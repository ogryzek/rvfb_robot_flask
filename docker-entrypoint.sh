#!/usr/bin/env bash
set -e

echo "$(netstat -nr | grep '^0\.0\.0\.0' | awk '{print $2}') dockerhost" >> /etc/hosts

exec "$@"

