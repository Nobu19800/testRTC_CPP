FROM ubuntu:18.04

RUN apt-get update\
 && apt-get install -y --no-install-recommends\
 g++\
 make\
 cmake\
 omniorb-nameserver\
 libomniorb4-dev\
 omniidl\
 doxygen\
 nkf\
# gnupg\
 wget\
 && wget --no-check-certificate https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_ubuntu.sh\
 && sh pkg_install_ubuntu.sh\
# && export repo="http://openrtm.org/pub/Linux/ubuntu/ bionic"\
# && echo "deb $repo main" | tee -a /etc/apt/sources.list\
# && apt-key adv --keyserver keys.gnupg.net --recv-keys 4BCE106E087AFAC0\
# && apt-get autoclean\
# && apt-get -qq update\
# && apt-get install -y --force-yes openrtm-aist-dev\
 && apt-get clean\
 && rm -rf /var/lib/apt/lists/*

COPY testRTC_CPP /root/testRTC_CPP
WORKDIR /root/testRTC_CPP
RUN mkdir build && cd build && cmake .. -DBUILD_DOCUMENTATION=ON -DBUILD_TESTS=ON && make && make doc && make install && cpack && make test
