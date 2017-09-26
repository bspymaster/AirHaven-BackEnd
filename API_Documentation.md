# API Documentation #

This document is intended to be a reference sheet that lists all possible API calls. 

| HTTP Method | URI                                                                   | Action                                                                         | Json Data             |
|:-----------:|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|:---------------------:|
| POST        | `http://[hostname]/AirHaven/api/[version]/files/[folder_id]/children` | Gets the files & folder metadata at the given folder id.                       | Requesting Children   |
| GET         | `http://[hostname]/AirHaven/api/[version]/users/authenticate-user`    | Verifies the given username & password (given in a standard Basic HTML header) | Authenticating Logins |
| GET         | `http://[hostname]/AirHaven/api/[version]/users/register-user`        | Registers the username, email, and password combo for use in the system        | Registering Users     |

## Json Formatting ##

This section details all the different send/return json API sending 

### Requesting Children ###

**Response Json**

Returns a `children` array of objects where each object in the array is a file object contained in the folder.
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

If there are no children, the following is returned:
```
{
  "children": []
}
```

### Authenticating Logins ###

**Response Json**

Returns a the user authentication data, including an api session token to verify all requests. If the token is valid, the server will also send back the numeric ID associated with the user's root directory. Otherwise, the root_folder will be -1.

*(Note that as of now, tokens have not been implemented, and so the API simply returns whether or not the user is verified.)*
```
{
  "token": <true|false>,
  "root_directory": <id_integer_pointing_to_user's_root_folder | -1>
}
```

### Registering Users ###

**Request Json**

Receives the required data to properly create a user account.

*(Note that, while the password is sent via plaintext, it is encrypted securely before being stored in the database. No plaintext copy of the password is stored anywhere.)*
```
{
  "username": <username_string>,
  "email": <email_string>,
  "password": <plaintext_password_string>
}
```

**Response Json**

Sends back a list of string-formatted errors, or an empty list if there were no errors and the creation was successful.

```
{
  "errors":[<list of string error outputs>]
}
```

### Errors ###

**404: Not Found**
```
{ 
  "error": "Not Found"
}
```
