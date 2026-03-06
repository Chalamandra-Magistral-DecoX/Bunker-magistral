#!/bin/bash
# deploy_all.sh - Despliegue masivo ajustado a tus carpetas reales

REPOS=(
  "chalamandra-hub:~/microcosmos_elite/hub"                  # si tienes el Hub local
  "microcosmos-demos:~/microcosmos_elite/demos"              # demos cuánticas
  "cursos-ko-fi:~/proyectos/cursos"                          # ajusta
  "automation-scripts:~/microcosmos_elite/scripts"           # tus scripts
  "blog-amplificador:~/proyectos/blog"                       # ajusta
)

echo "⚡ Iniciando despliegue masivo - $(date '+%Y-%m-%d %H:%M:%S')"

for repo in "${REPOS[@]}"; do
  name=$(echo "$repo" | cut -d: -f1)
  path=$(echo "$repo" | cut -d: -f2)

  if [ -d "$path" ]; then
    echo -e "\n──────────────────────────────────────"
    echo -e "📦 $name → $path"
    cd "$path" || continue

    git pull origin main --quiet 2>/dev/null || echo "  (git pull: sin cambios o error)"

    if [ -f "vercel.json" ] || grep -q "vercel" package.json 2>/dev/null; then
      echo "  → vercel --prod"
      vercel --prod --yes --quiet || echo "  [WARN] vercel falló"
    fi

    cd - >/dev/null
  else
    echo "  [MISSING] $name → $path"
  fi
done

echo -e "\n──────────────────────────────────────"
echo "🚀 Despliegue masivo completado."
