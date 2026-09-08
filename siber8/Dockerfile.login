FROM nginx:alpine
COPY login.html /usr/share/nginx/html/index.html
EXPOSE 80