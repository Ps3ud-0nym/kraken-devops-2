#!/bin/bash

# Obtain all hostnames related to docker from /etc/hosts
awk '{ print $2 }' /etc/hosts | grep docker.internal
