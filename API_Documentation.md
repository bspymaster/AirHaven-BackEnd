# API Documentation #

This document is intended to be a reference sheet that lists all possible API calls. 

| HTTP Method | URI                                                                 | Action                                                   | Json Return |
|:-----------:|:-------------------------------------------------------------------:|:-------------------------------------------------------- |:-----------:|
| POST        | `http://[hostname]/AirHaven/api/[version]/files/[file_id]/children` | Gets the files & folder metadata at the given folder id. | [Requesting Children](Requesting-Children)

## Json Formatting ##

This section details all the different send/return json API sending 

### Requesting Children ###

**Response Json**

Returns a `children` array of objects where each object in the array is a file object contained in the folder
```json
{
  "children": [
    {
      "id": <file_id_integer>,
      "name": <file_name_string>,
      "type": <"file"|"folder">
    }
  ]
}
```

### Errors ###

**404: Not Found**
```json
{ 
  "error": "Not Found"
}
```