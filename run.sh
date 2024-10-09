#!/bin/bash

nasm $1 -f elf64 -o out.o

if [ -f out.o ]; then
    ld -s out.o -o outfile
    rm out.o
fi
if [ -f outfile ]; then
    ./outfile
    rm outfile
fi
