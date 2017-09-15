#!/bin/bash

TEST_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-${(%):-%N}}")"; pwd)"

CONTAINER_OS="${CONTAINER_OS:-centos}"
CONTAINER_TAG="${CONTAINER_TAG:-latest}"
TEST_CONTAINER="$CONTAINER_OS:ttcopy_test"
TEST_CONTAINER=${CONTAINER}
DOCKER_FILE_PATH="$TEST_DIR/Dockerfile"
cat $DOCKER_FILE_PATH \
    | sed "s/@@@TAG_NAME@@@/$CONTAINER_TAG/" \
    | docker build -t $TEST_CONTAINER -

echo "# --------------------"
echo "# Docker container info"
echo "# --------------------"
cat $DOCKER_FILE_PATH \
    | sed "s/@@@TAG_NAME@@@/$CONTAINER_TAG/"
echo
_cmd="docker run -i --rm $TEST_CONTAINER uname -a"
echo $_cmd
$_cmd

echo "# --------------------"
echo "# wget version"
echo "# --------------------"
docker run -i --rm $TEST_CONTAINER /usr/bin/wget --version

docker run -i --rm $TEST_CONTAINER pwd
