#!/bin/sh

scp id_dsa.pub admin@router:
ssh admin@router "/user ssh-keys import file=id_dsa.pub user=admin-ssh"
