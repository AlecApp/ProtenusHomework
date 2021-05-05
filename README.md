## How to Run the Docker Container
1. From your local CLI, run `git clone https://github.com/AlecApp/ProtenusHomework.git`
2. Change into the newly downloaded `ProtenusHomework` directory (i.e. where the Dockerfile is.)
3. Run the following command: `docker build . -t protenus:latest` and wait for the container to be built.
4. Once the container has been built, run the following command: `docker run -p 8080:80 protenus:latest`
    - Note that you can use any of your system's available ports in place of `8080`
5. You can view the running container by visiting `127.0.0.1:8080` in your web browser.
6. When you're ready to stop the container, return to the CLI window and press `CTRL+C` to terminate the process.


## Cleanup
Before attempting to remove the container, make sure it is not currently running. You can view running containers with the `docker ps` command.

If your container is currently running you can stop it with the following command: `docker stop CONTAINER_ID` where `CONTAINER_ID` is the container ID shown by `docker ps`.
*Note, if you wish to stop **all** running containers, you can use the command `docker stop $(docker ps -q)` instead.*

Once your container is stopped, run the following commands:
1. `docker container prune` (press `y` when prompted)
2. `docker image prune -a` (press `y` when prompted)


## Modifying the Container

### Publishing the container on a different port e.g. `8081`
To publish the container on a different port, run the following command: `docker run -p MY_PORT_NUMBER:80 protenus:latest`
- `MY_PORT_NUMBER` is the port of your choosing e.g. `docker run -p 8081:80 protenus:latest`

This will allow you to access the container through `127.0.0.1:MY_PORT_NUMBER` in your web browser.

* Note that you do not need to make any modifications to the Dockerfile or rebuild the container.
* Note that the selected port must be available for use.
    - If you're running Linux (or Mac OSX?), you can view which ports are already consumed by running `sudo lsof -i -P -n | grep LISTEN`.
* Note that this will **not** stop any identical containers that were published to different ports!


### Using your own content for index.html
Any valid HTML code/file can be used as the container's homepage.

To use your own HTML file, remove the `RUN echo ...` statement in the Dockerfile and uncomment the `ADD MY_HTML_FILE ...` statement. Make sure to replace the `MY_HTML_FILE` with the filepath of your HTML file relative to the Dockerfile's directory e.g. `ADD my_html_file.html ...` or `ADD /src/my_html_file.html ...`.

Once done, you must rebuild & run the modified container (using the steps under "How to Run the Docker Container") before your changes will be visible.