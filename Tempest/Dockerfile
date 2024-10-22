FROM ubuntu

#Update Dependencies
RUN apt-get update

#AFL Dependencies
RUN apt-get install -y build-essential python3-dev automake cmake git flex bison libglib2.0-dev libpixman-1-dev python3-setuptools cargo libgtk-3-dev
RUN apt-get install -y lld-14 llvm-14 llvm-14-dev clang-14 || RUN apt-get install -y lld llvm llvm-dev clang
RUN apt-get install -y gcc-$(gcc --version|head -n1|sed 's/\..*//'|sed 's/.* //')-plugin-dev libstdc++-$(gcc --version|head -n1|sed 's/\..*//'|sed 's/.* //')-dev
RUN apt-get install -y ninja-build # for QEMU mode


#Aux Dependendencies
RUN apt-get install -y python3
RUN apt-get install -y bsdmainutils #Includes Hexdump
RUN apt-get install -y gdb
RUN apt-get install -y gcc


#Setup Fuzzing Dir with Example
RUN mkdir -p Tempest/Fuzzing
WORKDIR Tempest/Fuzzing
RUN git clone https://github.com/AFLplusplus/AFLplusplus
WORKDIR /Tempest/Fuzzing/AFLplusplus
RUN make all
WORKDIR /Tempest/Fuzzing
COPY src/Fuzzing .
RUN gcc buffer_overflow.c -o buffer_overflow


#Setup SAST Dir with Example
WORKDIR /Tempest
RUN mkdir SAST
WORKDIR /Tempest/SAST
COPY src/SAST .


#Set Working Directory to Tempest
WORKDIR /Tempest