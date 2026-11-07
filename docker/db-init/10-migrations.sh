#!/bin/bash
# Apply every file in supabase/migrations, in name order. Runs only when the database volume is new.
set -e
for f in /migrations/*.sql; do
  echo "Applying $f"
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -f "$f"
done
