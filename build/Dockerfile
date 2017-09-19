FROM centos:@@@TAG_NAME@@@

RUN yum update -y
RUN yum install -y curl wget openssl rpm-build gzip tar
RUN useradd -u 1000 mockbuild

WORKDIR /home/mockbuild

ADD rpmbuild rpmbuild
RUN mkdir -p rpmbuild/BUILD rpmbuild/BUILDROOT rpmbuild/RPMS rpmbuild/SOURCES rpmbuild/SPECS rpmbuild/SRPMS
RUN chown -R mockbuild:mockbuild /home/mockbuild

USER mockbuild:mockbuild
