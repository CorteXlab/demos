# IA Demo

This folder contains the Interference Aligment demo developped by Yasser Fadlallah during 2015

This scenario in demo is comprised by:

2 Transmitters:

- Main TX
- Interfering TX

3 Receivers:

- UE 1
- UE 2
- UE 3

and 1 scheduler (considered to be in the core network)

In order to compile and use this scenario do the following:

## Compile the source

Use the following commands fro your shell prompt at the airlock server:

$ cd gr-projectGT
$ mkdir build
$ cd build
$ cmake -DCMAKE_INSTALL_PREFIX=/home/cxlbuser/tasks/task
$ make

