FROM postgres:latest

ENV POSTGRES_USER myuser
ENV POSTGRES_PASSWORD mypassword
ENV POSTGRES_DB mydb
ENV SSL_CERTS_DIR /etc/postgresql/ssl

RUN mkdir -p ${SSL_CERTS_DIR} && \
    chown -R postgres:postgres ${SSL_CERTS_DIR} && \
    chmod 700 ${SSL_CERTS_DIR}

# copy SSL certificates
COPY ssl/server.crt ${SSL_CERTS_DIR}/
COPY ssl/server.key ${SSL_CERTS_DIR}/
COPY ssl/ca.crt ${SSL_CERTS_DIR}/

# set permissions for SSL files
RUN chown postgres:postgres ${SSL_CERTS_DIR}/* && \
    chmod 600 ${SSL_CERTS_DIR}/server.key

# enable SSL
RUN echo "\
ssl = on\n\
ssl_cert_file = '${SSL_CERTS_DIR}/server.crt'\n\
ssl_key_file = '${SSL_CERTS_DIR}/server.key'\n\
ssl_ca_file = '${SSL_CERTS_DIR}/ca.crt'\n\
" >> /usr/share/postgresql/postgresql.conf.sample

COPY docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/*.sh

EXPOSE 5432

CMD ["postgres"]