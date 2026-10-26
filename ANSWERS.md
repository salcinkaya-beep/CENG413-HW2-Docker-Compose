# HW-2 Answers

## 1. Service names and networking

Docker Compose creates a network for the services in the project. On this network, Docker's DNS lets the app find Redis using the service name `redis`. The app uses this name instead of an IP address. Containers on the default bridge network used by `docker run` do not automatically resolve each other by container name; a user-defined network is needed for automatic name resolution.

## 2. Stateless and stateful services

The Flask app is stateless because it does not save the counter in its own container. Redis is stateful because it stores the counter in the `redis_data` volume. I removed and restarted the app container, and the counter continued from 2 to 3. After `docker compose down` and restarting, it continued to 4. After `docker compose down -v` and restarting, the counter returned to 1 because the volume was deleted.

## 3. Database passwords

A database password should come from a secure source outside the repository, such as an environment variable supplied through an ignored `.env` file or a secrets manager. Committing a password to Git can expose it to anyone with repository access, even if the repository is private. It can also remain in Git history after the file is changed or deleted. This project uses Redis without a password for this local exercise and does not contain a database password.

## AI assistant use

I used an AI assistant to help me prepare the Docker Compose configuration and understand the testing steps. I ran the tests myself and reviewed the results.
