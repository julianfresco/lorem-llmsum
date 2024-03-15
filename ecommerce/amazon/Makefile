
create:
	docker build -t ecommerce-pg:latest ./
delete:
	docker rm ecommerce-pg
start:
	docker run -d --name ecommerce-pg -p 127.0.0.1:5432:5432 ecommerce-pg:latest
	docker container ls -f name=ecommerce
stop:
	docker stop ecommerce-pg
seed:
	echo "make seed: TODO\!"
refresh:
	make stop delete create start seed
