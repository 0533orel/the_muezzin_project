The Muezzin Project

- config folder:
- A file containing the environment variables
- 
- DAL folder:
- Contains files that talk to the database
- 
- data_services folder:
- Contains files that deal with the data such as loading the files, importing metadata on the files, converting audio to text, and classifying bds
- 
- kafka_service folder:
- Responsible for kafka services:
- producer - sends data to kafka.
- consumer - is responsible for receiving the data from the same topic and then processing the data and creating a dictionary with all the requested data and then sending it to Elasticsearch with a unique identifier. And with that unique identifier it sends the file itself to MongoDB
- 
- logs folder:
- A main class that writes logs and sends them to ElasticSearch with its own index
- 
- model folder:
- Contains auxiliary functions
-
-docker compose: contains the necessary services: kafka, elasticsearch and mongoDB
-
-readme





