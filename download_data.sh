#!/bin/bash

DATA_DIR=$(pwd)/data/assign/
assign1=dic_ec
assign2=dic_ce

mkdir -p ${DATA_DIR}
wget http://nlp.nju.edu.cn/MT_Lecture/${assign1}.rar -O ${DATA_DIR}/${assign1}.rar
unrar x ${DATA_DIR}/${assign1}.rar  ${DATA_DIR}
wget http://nlp.nju.edu.cn/MT_Lecture/${assign2}.rar -O ${DATA_DIR}/${assign2}.rar
unrar x ${DATA_DIR}/${assign2}.rar  ${DATA_DIR}

