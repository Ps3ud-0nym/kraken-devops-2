#!/bin/bash

# Obtain all hostnames related to docker from /etc/hosts
# Print second column with awk, and then select only results containing
# the string 'docker'

awk '{ print $2 }' /etc/hosts | grep docker.internal
