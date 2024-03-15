FROM postgres
ENV POSTGRES_USER ecommerce
ENV POSTGRES_DB ecommerce
ENV POSTGRES_PASSWORD ecommerce
EXPOSE 5432
COPY ./schema/ecommerce-demo-pg.sql /docker-entrypoint-initdb.d/init.sql
