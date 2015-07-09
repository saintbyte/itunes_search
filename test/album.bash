#!/bin/bash
set -x
set +ue
HOST='http://blogtest.ural.im'
wget -O- "${HOST}/album/1/"