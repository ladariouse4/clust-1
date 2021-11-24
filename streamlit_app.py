import os
os.system('curl -L https://github.com/cdr/code-server/releases/download/v3.12.0/code-server-3.12.0-linux-amd64.tar.gz --output code-server.tar.gz \
&& curl -L https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz --output ngrok.tgz \
&& tar xf ngrok.tgz \
&& tar xf code-server.tar.gz \
&& nohup ./ngrok http 10000 --log=stdout & ./code-server-3.12.0-linux-amd64/bin/code-server --auth=none --port=10000')
