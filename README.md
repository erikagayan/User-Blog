# User-Blog

## Features
In user blog api, you can create a user and create posts. An admin can make a user a moderator and both admin and moderator can edit or delete posts. There is also a bot that creates the required number of users and creates the required number of posts.


# Installation
1. Docker: [Install Docker](https://docs.docker.com/get-docker/)
- If you want to use PostgreSQL: [Install PostgreSQL](https://www.postgresql.org/download/)
2. Clone this repository to your local machine: https://github.com/erikagayan/User-Blog
3. Navigate to the project directory
4. Create `.env` file and define environmental variables by following '.env.sample'.
5. Build the Docker container using Docker Compose:`docker-compose build`
6. Access list of containers: `docker ps -a`
7. Create a superuser for accessing the Django admin panel and API: `docker exec -it <container_id here> python manage.py createsuperuser`
8. Start the Docker container: `docker-compose up` 
9. To stop the container, use: `docker-compose down`
