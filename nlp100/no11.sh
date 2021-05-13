#!/bin/bash
# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
. share.sh
cd $WORK_DIR
target="hightemp.txt"
cp $RESOURCE_DIR/$target ./
cat $target | sed s/"\t"/ /g
