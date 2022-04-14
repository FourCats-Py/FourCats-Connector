#!/bin/bash
baseName=$(basename "$1")

if [[ "$baseName" =~ "beta" ]]; then
  version=$(echo "$baseName" | grep -E "^v[0-9]+.[0-9]+.[0-9]+-beta.[0-9]+$")
else
  version=$(echo "$baseName" | grep -E "^v[0-9]+.[0-9]+.[0-9]+$")
fi

if [[ "$version" == "" ]]; then
  echo "No version number matched."
  exit 1
fi

version=${version:1}

echo "$version"

echo "Get version $version"

sed -i '' -r "s/^__version__[[:space:]]+=[[:space:]]+[\'\"](.*)[\'\"]$/__version__ = \"$version\"/" fourcats_connector/__init__.py

cat fourcats_connector/__init__.py
