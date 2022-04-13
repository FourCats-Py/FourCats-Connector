#!/bin/bash

tag=${1##*/}
version=`echo $TAG |grep -E "^v.+\d+$"`

if [[ $? -eq 0 ]]; then
  version=${version:1}
else
  version=$tag
fi

echo "Get version ${version}"

echo `sed -e "/^__version__\s*=\s*[\'\"]([^\'\"]*)[\'\"]$/s//__version__ = "${version}"/g" fourcats_connector/__init__.py`

