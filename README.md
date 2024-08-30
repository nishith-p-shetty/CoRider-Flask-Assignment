
# CoRider Flask Assignment

Flask User Resource App


## Appendix

A VISUAL UI AVILABLE AT [/apidoc/](http://localhost:8123/apidoc/)

Note: password is not encrypted, and is kept in plain text

Directory Structure 
```
├── README.md
├── docker-compose.yml
├── flask_app
│   ├── Dockerfile
│   ├── app
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── static
│   │       └── swagger.json
│   ├── requirements.txt
│   └── run.py
├── mongo_db
```

## API Reference

#### Get Server Status

```http
  GET /users/ping
```

| Parameter |
| :-------- |
| `none` |

#### Get all users

```http
  GET /users
```

| Parameter |
| :-------- |
| `none` |

#### Get Specfic User

```http
  GET /users/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. ID of user returned when created new user |


#### Create New User

```http
  POST /users
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `User Deatails`      | `JSON` | **Required**. User details in JSON |


#### Update User

```http
  PUT /users/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. ID of user returned when created new user |
| `User Deatails`      | `JSON` | **Required**. Updated user details in JSON |


#### Delete User

```http
  DELETE /users/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. ID of user returned when created new user |



## Installation

* Install Docker
* Git Clone this project

```bash
  git clone https://github.com/nishith-p-shetty/CoRider-Flask-Assignment
```
* CD to folder 
```bash
    cd CoRider-Flask-Assignment
```

* Set Environment Variables in docker-compose.yal

* Docker compose and run

```bash
    docker compose up -d
```
## Run Locally

* CD to folder 
```bash
    cd CoRider-Flask-Assignment
```

* Set Environment Variables in docker-compose.yal

* Docker compose and run

```bash
    docker compose up -d
```
## Demo

You can try in postman or [/apidoc/](http://localhost:8123/apidoc/)

## Tech Stack

**Language:** Python 3.11

**Client:** Postman, Swagger UI

**Server:** Flask

**Database:** MongoDB

