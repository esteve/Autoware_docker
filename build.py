#!/usr/bin/env python3

import docker

import os

import sys

if __name__ == '__main__':
    _, docker_os, docker_ros_distro = sys.argv
    docker_tag = 'autoware/travis:develop-{}-{}'.format(docker_os, docker_ros_distro)
    client = docker.from_env()
    dockerfile_dirname = os.path.dirname(os.path.realpath(__file__))
    client.images.build(path=dockerfile_dirname, tag=docker_tag)
