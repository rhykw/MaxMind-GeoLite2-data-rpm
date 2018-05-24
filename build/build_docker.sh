#!/bin/bash

set -e
set -x

TEST_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-${(%):-%N}}")"; pwd)"

TEST_CONTAINER="${CONTAINER}.builder"
DOCKER_FILE_PATH="$TEST_DIR/Dockerfile.centos"
dockerfile=$(mktemp $(pwd)/Dockerfile.XXXXXXXX)

mkdir -p rpmbuild/SOURCES
sources=$(cat *.spec|awk '($1~"^Source"){print $2}')
if [ ! -z "$sources" ]; then
    ( cd rpmbuild/SOURCES && wget $sources )
fi

mmdb=$(tar --wildcards -ztf rpmbuild/SOURCES/GeoLite2-Country.tar.gz '*.mmdb')
source_date=$(IFS='-_/';set -- $mmdb;echo $3)

cat $DOCKER_FILE_PATH \
    | sed "s/@@@CONTAINER@@@/$CONTAINER/" > $dockerfile

docker build -t $TEST_CONTAINER -f $dockerfile .

for spec in *.spec;do
    docker run -i --rm $TEST_CONTAINER rpmbuild --define "_source_yyyy_mm ${source_date:0:4}.${source_date:4:2}" -ba $spec
done
