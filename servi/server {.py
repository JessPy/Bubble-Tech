server {
    listen 80;
    server_name seu_dominio.com;

    # Redirecionar HTTP para HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name seu_dominio.com;

    ssl_certificate /caminho/para/seu/certificado.pem;
    ssl_certificate_key /caminho/para/sua/chave.key;

    location / {
        proxy_pass http://127.0.0.1:5000;  # Sua aplicação Flask
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
