# visitoolkit_connector
client-side implementation of 'DMS JSON Data Exchange'  

*(most parts of specification v1.4 is already implemented,   
but my code currently contains many rough edges...)*

**Installation via pip**   
https://pypi.org/project/visitoolkit-connector   
*(runs on Python 3)*  


## description
An INOFFICIAL OpenSource client library written in Python to   
*ProMoS NT (c)* AKA *Saia Visi.Plus (c)* version 1.7 or higher  

- search for datapoints   
- manipulations on datapoints (get, set, delete)   
- retrieving of trend data   
- retrieving of alarms and protocols   
- event-based monitoring of datapoints 

**visitoolkit_connector** communicates over websockets to DMS and implements the official 'DMS JSON Data Exchange' protocol.   
All JSON objects (requests and responses) are mapped to instances of Python classes.  
All JSON values are mapped to attributes.  
Events from datapoint subscriptions are handled by **visitoolkit_eventsystem** for executing your Python callbacks in a background thread.  


*documentation for this protocol is without any warranty temporary available under
https://github.com/stefanbraun-private/stefanbraun-private.github.io/tree/master/ProMoS_dev_docs  
All rights reserved by the respective owner 'MST Systemtechnik AG'* 


## usage
```python
from visitoolkit_connector import connector
```
*FIXME: add examples...*   
   
   
Increasing logging level for bughunting:
```python
import logging
logging.getLogger('visitoolkit_connector').setLevel(logging.DEBUG)
```

## background information
**visitoolkit_connector** is a core part of **visitoolkit**. 

**visitoolkit** is written for the proprietary Building and Process Management System
'ProMoS NT' (c) MST Systemtechnik AG'  
(also known as 'Saia Visi.Plus' (c) Saia-Burgess Controls AG) 

Intention:  
Support creator of visualisation projects...  
Add efficiency...  
Reduce manual error-prone processes...  
Add missing features...

Disclaimer: Use 'visitoolkit' at your own risk!
