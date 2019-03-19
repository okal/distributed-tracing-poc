FROM okal/gradle:latest
RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN gradle build
CMD java -jar build/libs/cpu-bound-0.1.0.jar