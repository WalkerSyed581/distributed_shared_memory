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

Following is the protocol that our Client-Arbiter communication will follow:

| Request Purpose        | Message ID      | Request Syntax   | Response Syntax           |
| -------------- | ----------- | ------------ | -------------------- |
| Subscribe to network      | 0           | 0&#124;      | 0&#124;node_id       |
| Set Shared Var    | 1           | 1&#124;node_id&#124;var_name&#124;ser_value | 1&#124;node_id |
| Revoke Shared Var | 2 | 2&#124;node_id&#124;var_name | 2&#124;node_id |
| Get Shared Var | 3 | 3&#124;node_id&#124;target_node_id&#124;var_name | 3&#124;node_id&#124;var_val |
| Get List of Shared Vars | 4 | 4&#124;node_id | 4&#124;node_id&#124;serialized_obj |
| Get Write Access | 5 | 5&#124;node_id&#124;target_node_id&#124;var_name | 5&#124;node_id/err_code |
| Check Write Access | 6 | 6&#124;node_id&#124;target_node_id&#124;var_name | 6&#124;node_id/err_code |
