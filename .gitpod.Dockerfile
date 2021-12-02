FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN sudo apt-get update \
    && sudo apt-get install -y \
    && sudo rm -rf /var/lib/apt/lists/*

# pip it up
RUN pip install pandas scipy