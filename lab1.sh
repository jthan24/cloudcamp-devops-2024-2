#!/bin/bash

read -p "Introduce el nombre de la carpeta: " folder

if [ -d "${folder}" ]; then
  rm -rf "${folder}"
  echo "Se ha eliminado la carpeta"
fi

mkdir -p "${folder}"

for i in {1..10}
do
  fecha_hora=$(date)
  echo "Fecha y hora de creación: ${fecha_hora}" > "${folder}/archivo_${i}.txt"
done

echo "Se han creado 10 archivos dentro de la carpeta ${folder}"