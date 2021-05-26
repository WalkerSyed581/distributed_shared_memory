# CS332 - Distributed Computing
The aim is to implement a read replication based Distributed Shared Memory in Python which allows other Python programs to simply import and sue it as required. Following are the various design specifications that need to be considered:

* DSM Algorithm
* Dsitribtuion and Access of Data
* Granularity
* Concurrent Access

## Granularity

There are three ways to tackle the division of data which are:

* Page-based DSM
* Object-based DSM
* Variable-based DSM

In our case we will be going with using either Object-based or Variable-based. Both of these techniques require modern compilers and programs which do not just worked like old programs focusing on the pages in the memory.

