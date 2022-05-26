# stage 1

FROM node:12.7-alpine AS my-app-build
WORKDIR /app
COPY . .
RUN npm ci && npm run build --prod

# stage 2

FROM nginx:alpine
COPY --from=my-app-build /app/dist/word-cloud /usr/share/nginx/html
EXPOSE 80
CMD ["/bin/sh",  "-c",  "envsubst < /usr/share/nginx/html/assets/env.template.js > /usr/share/nginx/html/assets/env.js && exec nginx -g 'daemon off;'"]