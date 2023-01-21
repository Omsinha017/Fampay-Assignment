
# FamPay Assignment

## Goal

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.


## Tech Stack
- Python (Programming Language)
 - Django
 - SQLite (Database)
 - Django Rest Framework


## API Reference

#### Get all videos / Search a video

```http
  GET /api/v1/search_videos
```
If query params is passed, then it will show the list of videos after filtering the data stored in db, in descending order of publication date in pagination format, else it will return all the data stored in database in descending order of publication date in pagination format

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` | **Optional** |



#### Get item

```http
  POST /api/v1/add_key/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `key`      | `string` | **Required** Youtube API Key |

This API will add, Youtube API key to the database, So that If the current key Quota exceeds, the limit then we can add the new key in the database and scheduler starts to fetch latest data

## Run Locally

Clone the project

```bash
  git clone https://github.com/Omsinha017/Fampay-Assignment.git
```

Go to the project directory

```bash
  cd Fampay
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```

Setup the Database
```bash
  python3 manage.py migrate
```

Create superuser for accessing the dashboard to view the stored videos

```bash
  python3 manage.py createsuperuser
```

Start the server

```bash
  python3 manage.py runserver
```

To access the dashboard checkout http://127.0.0.1:8000/admin

#### Now run the following apis described in the Postman collection for testing the project, and make sure to add youtube API key using the postman collection

## Screenshots

![Get Search Data](https://drive.google.com/uc?export=view&id=1F1ySmkRaM3_1ZZgc3gTs5DE0Q_aUfriC)


![Save Youtube API Key](https://drive.google.com/uc?export=view&id=1NvKj2WwiSGj7qqRJ_k1WP_jSZEHjT2u8)
