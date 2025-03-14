#!/usr/bin/env bash

export $(grep -v '^#' .env | xargs)
echo "Debug: ENVIRONMENT='$ENVIRONMENT'"

if [ -z "$ENVIRONMENT" ]; then
  echo "Error: ENVIRONMENT is not set in .env file."
  exit 1
fi

if [ "$ENVIRONMENT" = "local" ]; then
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

elif [ "$ENVIRONMENT" = "production" ] || [ "$ENVIRONMENT" = "development" ]; then
  python manage.py loaddata v1/accounts/fixtures/profiles.json
  python manage.py loaddata v1/accounts/fixtures/users.json
  python manage.py loaddata v1/user_roles/fixtures/merchants.json
  python manage.py loaddata v1/user_roles/fixtures/customers.json
  python manage.py loaddata v1/categories/fixtures/categories.json
  python manage.py loaddata v1/subcategories/fixtures/subcategories.json
  python manage.py loaddata v1/products/fixtures/products.json
  python manage.py loaddata v1/product_abouts/fixtures/product_abouts.json
  python manage.py loaddata v1/product_details/fixtures/product_details.json
  python manage.py loaddata v1/product_medias/fixtures/product_medias.json
  python manage.py loaddata v1/product_questions/fixtures/product_questions.json
  python manage.py loaddata v1/product_reviews/fixtures/product_reviews.json
  python manage.py loaddata v1/product_review_votings/fixtures/product_review_votings.json
  python manage.py loaddata v1/product_tags/fixtures/product_tags.json
  python manage.py loaddata v1/product_variants/fixtures/product_variants.json
  python manage.py loaddata v1/product_variant_items/fixtures/product_variant_items.json
  echo "Sample data import for $ENVIRONMENT environment finished."

else
  echo "Error: Unsupported ENVIRONMENT value '$ENVIRONMENT'."
  exit 1
fi

echo "Sample data import finished."