FROM node:22.18-slim as installer

WORKDIR /app

COPY package*.json ./
RUN npm install

FROM installer

WORKDIR /app

COPY . .
# RUN npm run build

EXPOSE 8080

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]