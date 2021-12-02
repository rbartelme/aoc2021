FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN sudo apt-get update \
    && sudo apt-get install -y pip htop\
    && sudo rm -rf /var/lib/apt/lists/*

# pip it up
RUN pip3 install pandas scipy
