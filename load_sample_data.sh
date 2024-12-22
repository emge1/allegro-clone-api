#!/usr/bin/env bash

DB_FILE="./config/db.sqlite3"
SQL_SAMPLE_DATA_DIR="./sample_data"

if [ ! -d "$SQL_SAMPLE_DATA_DIR" ]; then
  echo "Error: $SQL_SAMPLE_DATA_DIR does not exist."
  exit 1
fi

if [ ! -f "$DB_FILE" ]; then
  echo "Error: $DB_FILE does not exist."
  exit 1
fi

for file in "$SQL_SAMPLE_DATA_DIR"/*.sql; do
  [ -e "$file" ] || { echo "No .sql files in '$SQL_SAMPLE_DATA_DIR'"; exit 1; }

  table_name=$(basename "$file" .sql)
  echo "Checking table: '$table_name'"

  row_count=$(sqlite3 "$DB_FILE" "SELECT COUNT(*) FROM $table_name;" 2>/dev/null)
  if [ $? -ne 0 ]; then
    echo "Table '$table_name' does not exist. Skipping import for '$file'."
    continue
  fi

  if [ "$row_count" -eq 0 ]; then
    echo "The table '$table_name' is empty. Importing data from '$file'..."
    sqlite3 "$DB_FILE" < "$file"
    if [ $? -eq 0 ]; then
      echo "Data successfully imported to '$table_name'."
    else
      echo "Error while importing data from '$file' to '$table_name'."
    fi
  else
    echo "The table '$table_name' is not empty. Skipping import."
  fi
done

echo "Sample data import finished."
