#!/bin/bash
set -e

echo "Configuring PostgreSQL SSL settings..."

cat >> ${PGDATA}/pg_hba.conf <<EOF
# Require SSL for all remote connections
hostssl all all all scram-sha-256
EOF