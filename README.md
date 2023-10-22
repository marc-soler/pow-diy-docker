# pow-diy-docker

## Notes
- If the python executable needs user input, add -t (open terminal) -i (interactive mode) after docker run
- pip freeze > requirements.txt to dump all installed requirements into a .txt
- docker rmi -f $(docker images -a -q) removes all images
- add -p localport:remoteport after docker run to map the ports of the container to those of you local machine
- docker exec -it [CONTAINER_ID] /bin/sh to enter the container's terminal
- once in a container's terminal, CTRL+P followed by CTRL+Q to exit the terminal without stopping the container. CTRL+C and CTRL+D exit and kill the container.
