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

In our case we will be going with using Object-based DSM as it will be quite general and will allow the subscribers to pass in data of any kind in the form of objects which will be passed on to the main object-based memory where the storage place will be decided.

