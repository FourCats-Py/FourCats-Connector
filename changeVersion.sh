#!/bin/bash
baseName=$(basename "$1")

echo "$baseName"

if [[ "$baseName" =~ "beta" ]]; then
  version=$(echo "$baseName" | grep -E "^v\d+.\d+.\d+-beta.\d+$")
else
  version=$(echo "$baseName" | grep -E "^v\d+.\d+.\d+$")
fi

echo "$version"

if [[ "$version" == "" ]]; then
  echo "No version number matched."
  exit 1
fi

version=${version:1}

echo "$version"

echo "Get version $version"

sed -i '' -r "s/^__version__[[:space:]]+=[[:space:]]+[\'\"](.*)[\'\"]$/__version__ = \"$version\"/" fourcats_connector/__init__.py

cat fourcats_connector/__init__.py
