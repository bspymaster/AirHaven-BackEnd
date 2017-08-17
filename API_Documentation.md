# API Documentation #

This document is intended to be a reference sheet that lists all possible API calls. 

| HTTP Method | URI                                                                   | Action                                                                         | Json Return           |
|:-----------:|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|:---------------------:|
| POST        | `http://[hostname]/AirHaven/api/[version]/files/[folder_id]/children` | Gets the files & folder metadata at the given folder id.                       | Requesting Children   |
| GET         | `http://[hostname]/AirHaven/api/[version]/users/authenticate-user`    | Verifies the given username & password (given in a standard Basic HTML header) | Authenticating Logins |

## Json Formatting ##

This section details all the different send/return json API sending 

### Requesting Children ###

**Response Json**

Returns a `children` array of objects where each object in the array is a file object contained in the folder
```
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

### Authenticating Logins ###

**Response Json**

Returns a the user authentication data, including an api session token to verify all requests.

*(Note that as of now, tokens have not been implemented, and so the API simply returns whether or not the user is verified.)*
```
{
  "token": <true|false>
}
```

### Errors ###

**404: Not Found**
```
{ 
  "error": "Not Found"
}
```
