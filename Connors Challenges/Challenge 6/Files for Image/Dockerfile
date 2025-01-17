# Use a Debian base image
FROM debian:bullseye

# Set environment variables
ENV MINECRAFT_VERSION=1.13
ENV MINECRAFT_SERVER_JAR=server.jar
ENV MINECRAFT_MEMORY=512M
ENV JDK_VERSION=8u181
ENV JDK_BUILD=b13
ENV JAVA_HOME=/opt/java/jdk1.8.0_181

# Install necessary tools
RUN apt-get update && \
    apt-get install -y wget tar && \
    rm -rf /var/lib/apt/lists/*

# Create directory for Java installation
RUN mkdir -p /opt/java

# Download and extract JDK
RUN wget --no-check-certificate -c --header "Cookie: oraclelicense=accept-securebackup-cookie" \
    https://repo.huaweicloud.com/java/jdk/8u181-b13/jdk-8u181-linux-x64.tar.gz -O /tmp/jdk-8u181-linux-x64.tar.gz && \
    tar -xzf /tmp/jdk-8u181-linux-x64.tar.gz -C /opt/java && \
    rm /tmp/jdk-8u181-linux-x64.tar.gz

# Debug: List contents of /opt/java/jdk1.8.0_181/bin
RUN ls -l /opt/java/jdk1.8.0_181/bin

# Directly invoke java from its static location
RUN /opt/java/jdk1.8.0_181/bin/java -version

# Set up Minecraft server directory
WORKDIR /minecraft

# Copy world and server.properties files into the container
# Assume you have 'world' and 'server.properties' in your project directory
COPY ./world /minecraft/world
COPY ./server.properties /minecraft/server.properties
COPY ./flag.txt /minecraft/flag.txt

# Download the Minecraft server jar
RUN wget -O ${MINECRAFT_SERVER_JAR} https://piston-data.mojang.com/v1/objects/d0caafb8438ebd206f99930cfaecfa6c9a13dca0/server.jar

# Accept the Minecraft EULA
RUN echo "eula=true" > eula.txt

# Expose the default Minecraft server port
EXPOSE 25565

# Set the command to start the Minecraft server
CMD /opt/java/jdk1.8.0_181/bin/java -Xmx${MINECRAFT_MEMORY} -Xms${MINECRAFT_MEMORY} -jar ${MINECRAFT_SERVER_JAR} nogui