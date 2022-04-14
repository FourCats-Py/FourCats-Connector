#!/bin/bash
baseName=$(basename "$1")

if [[ "$baseName" =~ "beta" ]]; then
  echo "包含 beta"
  echo "$baseName"
  echo "$baseName" | grep -E "^v\d+.\d+.\d+-beta.\d+$"
  version=$(echo "$baseName" | grep -E "^v\d+.\d+.\d+-beta.\d+$")
  echo "$version"
else
  echo "不包含 beta"
  echo "$baseName"
  version=$(echo "$baseName" | grep -E "^v\d+.\d+.\d+$")
  echo "$version"
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
