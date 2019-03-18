FROM gradle:5.2.1-jdk8-alpine
WORKDIR /home/gradle/project
COPY . /home/gradle/project
RUN gradle build
CMD java -jar build/libs/cpu-bound-0.1.0.jar