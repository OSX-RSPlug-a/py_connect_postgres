mkdir ssl
cd ssl

openssl req -new -x509 -days 365 -nodes -out ca.crt -keyout ca.key -subj "/CN=root-ca"

openssl req -new -nodes -out server.csr -keyout server.key -subj "/CN=postgres"
openssl x509 -req -in server.csr -days 365 -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt

chmod 600 server.key ca.key