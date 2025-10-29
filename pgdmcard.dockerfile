FROM postgres:17-alpine
LABEL maintainer="Danwiilo Ltda"
LABEL license="MIT License"
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=dmcard
EXPOSE 5432