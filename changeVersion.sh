#!/bin/bash

tag=${1##*/}
regVersion=$(echo $tag | grep -E "^v.+\d+$")

echo $tag
echo $regVersion

if [[ $? -eq 0 ]]; then
  version=${regVersion:1}
else
  exit 1
fi

echo "Get version ${version}"
echo "sed -e '/^__version__\s*=\s*[\'\"]([^\'\"]*)[\'\"]$/s//__version__ = '${version}'/g'"
echo $(sed -e "/^__version__\s*=\s*[\'\"]([^\'\"]*)[\'\"]$/s//__version__ = "${version}"/g" fourcats_connector/__init__.py)
