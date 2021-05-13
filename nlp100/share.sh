#!/bin/bash
cd $(dirname $0)
cd ../
PYTHONDBOX_HOME=$(pwd)
RESOURCE_DIR="$PYTHONDBOX_HOME/resource/nlp100"
WORK_DIR="$PYTHONDBOX_HOME/tmp/$(date '+%Y%m%d%H%M%S')"
mkdir -p $WORK_DIR
echo "work dir created. [$WORK_DIR]"
echo "-----------------------------"

# 終了時に自動でテンポラリを削除
function finally () {
  echo "-----------------------------"
  rm -rf $WORK_DIR
  echo "work dir deleted. [$WORK_DIR]"
}
trap finally EXIT
