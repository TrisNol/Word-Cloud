FROM node:20.11.1-alpine AS build
WORKDIR /app
COPY . .
RUN npm ci && npm run build --omit=dev

FROM nginx:alpine
COPY --from=build /app/dist/word-cloud /usr/share/nginx/html
EXPOSE 80
CMD ["/bin/sh",  "-c",  "envsubst < /usr/share/nginx/html/assets/env.template.js > /usr/share/nginx/html/assets/env.js && exec nginx -g 'daemon off;'"]