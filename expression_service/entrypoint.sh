#!/bin/bash
consul agent -node=client-expression$(hostname -i) -config-dir=/etc/consul.d -join=$CONSUL_IP --data-dir /path/to/datadir &
python server.py