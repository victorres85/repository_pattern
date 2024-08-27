# Repository Pattern

This is a practice project aiming to get get some practice with the Repository Pattern. 

So far I have created the following models: parlamentar, post and social_media, have also created the repository for related to the parlamentar model and a few different pydantic schemas. Everything has been created by utilising a TDD approach.

**Next Steps**: will conclude finish the repositories for the remaining models, create the endpoints to perform CRUD operations to the database and review the pydantic schemas. 




To run this project please follow the steps below:

1. Clone the repository
2. Install project libraries with poetry
3. Setup database
4. Run tests


## Clone repo
Use the command below to clone the repo to your machine  
`git clone https://github.com/victorres85/repository_pattern.git`  


## Install project libraries:
To install the libraries on your terminal enter the root folder of the project (repository_pattern), and enter the command below:  
`poetry install`  

#### obs:
I have commited the .vscode with the aim of simplifying the testing process, in this directory you will find the file settings.json, it will be necessary to change the current python path which is found on `"pylint.interpreter":[]` and add the python path from your local machine, for that you can execute the commands below:  
`poetry shell`   
and   
`which python`  
the first command will activate the virtual environment and the second one will return the python path for the virtual environment, simply copy the given python path and past as a new value of the "pylint.interpreter" field. 


## Database

This project utilises postgres database running on a Docker container, to run postgres container on your machine please follow the steps below:

### Pull the postgres 
you can do it by running the command below:  
`docker pull postgres:14`  

### Run the container
By executing the command below you will run the postgres container, but also set up enviroment variables to define the postgres username, password, database name and the port in which postgres will be running inside the container and the port of your local machine on which will be mapped to the related container port. 

```
docker run --name my-postgres-container \
    -e POSTGRES_USER=repo_user \
    -e POSTGRES_PASSWORD=repo_pass \
    -e POSTGRES_DB=repo_db \
    -p 5432:5432 \
    -d postgres:14
```

#### obs: 
If you run the code as described above you will be able to use the string below to connect this flask application to the database:  
`postgresql+psycopg2://repo_user:repo_pass@localhost:5432/repo_db`  
In case you make any change to the docker run command below make sure to update the changed values on the correspondent variable in the .env file.


## Run Tests
To run the tests please execute the command below:  
`pytest tests/`
