FROM nginxdemos/hello:latest

# Comment out the following line if you're using your own HTML file
RUN echo "Hello, World! I'm Alec's project" > /usr/share/nginx/html/index.html

# Uncomment this line if you're using your own HTML file
# ADD MY_HTML_FILE /usr/share/nginx/html/

EXPOSE 80