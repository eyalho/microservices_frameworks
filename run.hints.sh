
# Only http api example:
nameko run --config config.yml micro.api # run <folder_name.file_name>
curl localhost:8080/hello

# http api -> run microservices through rabbitmq example:
docker run -d -p 5672:5672 rabbitmq:latest # run rabbitmq docker locally
nameko run --config config.yml micro.dispatcher # terminal1
nameko run --config config.yml micro.workers.subscribers # terminal2
curl -d "eyal" -X POST 0.0.0.0:8080/hello