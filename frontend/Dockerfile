FROM node:18.12.1-alpine
WORKDIR /code/frontend

COPY frontend/package*.json ./
RUN npm install

COPY frontend/ ./
CMD ["npm", "start"]
