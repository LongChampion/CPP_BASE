#!/bin/bash

cd /
sudo mkdir -p /build/glibc-OTsEL5/
cd /build/glibc-OTsEL5/
sudo wget http://ftp.gnu.org/gnu/glibc/glibc-2.27.tar.gz
sudo tar -xzvf glibc-2.27.tar.gz
sudo rm glibc-2.27.tar.gz