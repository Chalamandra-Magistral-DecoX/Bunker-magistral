#!/bin/bash
DB_PATH=~/microcosmos_elite/boveda.db
BACKUP_PATH=~/microcosmos_elite/vault/boveda_$(date +%Y%m%d_%H%M%S).bak
cp $DB_PATH $BACKUP_PATH
echo "📦 Respaldo de seguridad creado en: $BACKUP_PATH"
