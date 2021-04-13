FROM node:13.12.0-alpine

# Set working directory
WORKDIR /app/ui

# Copy app dependencies
COPY package.json package-lock.json /app/ui/


# Install app dependencies.
RUN npm install

# Copy working files.
COPY . /app/ui

EXPOSE 3000
