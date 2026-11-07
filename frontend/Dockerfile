FROM node:22-alpine

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .

EXPOSE 5173
# --host so the port can be published.
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
