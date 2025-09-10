FROM node:22.18-slim AS installer

WORKDIR /app

COPY package*.json .
RUN npm install

FROM installer

WORKDIR /app

COPY . .
# RUN npm run build

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]