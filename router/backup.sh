#!/bin/sh

# backup text config
ssh -i id_dsa admin@router "/export" > backup.routeros
