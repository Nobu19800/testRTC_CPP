FROM ubuntu:18.04

RUN apt-get update\
 && apt-get install -y --no-install-recommends\
 g++\
 make\
 cmake\
 uuid-dev\
 libboost-filesystem-dev\
 omniorb-nameserver\
 libomniorb4-dev\
 omniidl\
 && export repo="http://openrtm.org/pub/Linux/ubuntu/ bionic"\
 && echo "deb $repo main" | sudo tee -a /etc/apt/sources.list\
 && sudo apt-get -qq update\
 && sudo apt-get install -y --force-yes openrtm-aist-dev\
 && apt-get clean\
 && rm -rf /var/lib/apt/lists/*

COPY testRTC_CPP /root/testRTC_CPP
WORKDIR /root/testRTC_CPP
RUN mkdir build && cd build && cmake .. && make && sudo make install & sudo make package
