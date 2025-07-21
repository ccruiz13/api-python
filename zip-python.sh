#!/bin/bash

ZIP_NAME="api-python.zip"

# Archivos y carpetas a excluir
EXCLUDES=(
  ".env"
  "dynamodb_full_access_policy.json"
  "__pycache__"
  ".pytest_cache"
)

# Elimina el zip si ya existe
if [ -f "$ZIP_NAME" ]; then
  rm "$ZIP_NAME"
fi

# Construye el comando de exclusión
EXCLUDE_ARGS=()
for exclude in "${EXCLUDES[@]}"; do
  EXCLUDE_ARGS+=(-x "$exclude")
done

# Comprimir todo excepto lo excluido
zip -r "$ZIP_NAME" . "${EXCLUDE_ARGS[@]}"

echo "Archivo comprimido creado: $ZIP_NAME"
