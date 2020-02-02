# run rabbitmq docker locally
docker run -d -p 5672:5672 rabbitmq:latest

# 1. http example:
nameko run --config config.yml micro.api # run <folder_name.file_name>
curl localhost:8080/hello

# 2. Events example
# http api (api_dispatcher) --rabbit_event--> triger the EmptySubscriber
# EmptySubscriber on 2nd microservice just print it
nameko run --config config.yml micro.api_dispatcher # terminal1
nameko run --config config.yml micro.workers.subscribers # terminal2
# Here just EmptySubscriber will logout
curl -d "eyal" -X POST 0.0.0.0:8080/hello

# 3. Producer - Consumer example:
# http api (api_dispatcher) --rabbit_event--> triger the WorkerSubscriber
# WorkerSubscriber on 2nd microservice produce a msg to exchange with routingkey
# Worker on 3d microservice consume the msg and print 
nameko run --config config.yml micro.api_dispatcher # terminal1
nameko run --config config.yml micro.workers.subscribers # terminal2
nameko run --config config.yml micro.workers.consumer # terminal3