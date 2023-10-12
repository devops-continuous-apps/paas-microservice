# Platform as a Service Microservice

Manual deployment of a microservice on a Platform as a Service (PaaS) environment.

## Table of Contents

- [Platform as a Service Microservice](#platform-as-a-service-microservice)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Usage](#usage)
  - [License](#license)

## Getting Started

These instructions will help you get your project up and running.

### Prerequisites

You'll need the following tools to run this project:

- Docker: [Docker Installation](https://docs.docker.com/get-docker/)
- Docker Compose: [Docker Compose Installation](https://docs.docker.com/compose/install/)

### Usage

To set up and run the project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/devops-continuous-apps/paas-microservice
   ```

2. Change into the project directory:

   ```bash
   cd paas-microservice
   ```

3. Build and run the project using Docker Compose:

   ```bash
   docker-compose -f "docker-compose.yml" up --build
   ```

## Postman Collection

 Download the [Postman Collection](Blacklists.postman_collection.json) to test the API. Remember to set the environment variables before running the requests.

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](LICENSE)**
- Copyright 2023 © DevOps Continuous Apps
