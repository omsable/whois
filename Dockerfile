FROM          ruby:alpine3.7
COPY          main.rb /main.rb
RUN           gem install whois
ENTRYPOINT   ["ruby", "main.rb"]
