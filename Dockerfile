FROM alpine:3.6

# Update source repositories
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.4/main" >> /etc/apk/repositories && \
	echo "http://dl-4.alpinelinux.org/alpine/v3.4/community" >> /etc/apk/repositories

RUN apk update && \
	apk add python py-pip curl unzip dbus-x11 ttf-freefont firefox-esr dbus xvfb tar && \
	pip install --upgrade pip && \
	pip install selenium && \
	pip install pyvirtualdisplay

ADD . /code
WORKDIR /code

# Install geckodriver:
RUN export BASE_URL=https://github.com/mozilla/geckodriver/releases/download \
  && export VERSION=$(curl -sL \
    https://api.github.com/repos/mozilla/geckodriver/releases/latest | \
    grep tag_name | cut -d '"' -f 4) \
  && curl -sL \
  # $BASE_URL/$VERSION/geckodriver-$VERSION-linux64.tar.gz | tar -xz \
  # $BASE_URL/v0.16.1/geckodriver-v0.16.1-linux64.tar.gz | tar -xz \
  $BASE_URL/v0.15.0/geckodriver-v0.15.0-linux64.tar.gz | tar -xz \
  && mv geckodriver /usr/local/bin/geckodriver \
  && chmod a+x /usr/local/bin/geckodriver

# run Xvfb in the background with a display number
RUN Xvfb :10 -ac &
ENV DISPLAY=:10

RUN pip install -r requirements.txt

# Install chromium with webdriver
RUN apk add --update --no-cache bash chromium chromium-chromedriver
ENV PATH="/usr/bin/chromedriver:${PATH}"

ENTRYPOINT ["bash", "docker-entrypoint.sh"]

CMD ["python", "app.py"]

