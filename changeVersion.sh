#!/bin/bash

tag=${1##*/}
version=$(echo $tag | grep -E "^v.+\d+$")

if [[ $? -eq 0 ]]; then
  version=${version:1}
else
  exit 1
fi

echo "Get version ${version}"
echo "sed -i '' -r \"s/^__version__[[:space:]]+=[[:space:]]+[\'\"](.*)[\'\"]$/__version__ = \"${version}\"/\" fourcats_connector/__init__.py"
echo $(sed -i '' -r "s/^__version__[[:space:]]+=[[:space:]]+[\'\"](.*)[\'\"]$/__version__ = \"${version}\"/" fourcats_connector/__init__.py)
