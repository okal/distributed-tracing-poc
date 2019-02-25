FROM ruby:2.5
RUN apt-get update -qq && apt-get install -y nodejs
RUN mkdir '/usr/src/app'
WORKDIR '/usr/src/app'
COPY Gemfile '/usr/src/app/Gemfile'
COPY Gemfile.lock '/usr/src/app/Gemfile.lock'
RUN bundle install
COPY . '/usr/src/app'

EXPOSE 3000

# Start the main process.
CMD ['rails', 'server', '-b', '0.0.0.0']