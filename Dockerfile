# Use an official Python runtime as a parent image
FROM python:3.10

# установка хрома
RUN apt-get update && apt-get install -y xvfb x11vnc
RUN Xvfb -screen 0 1024x768x24 :99 +extension RANDR &
RUN x11vnc -display :99 -forever &
RUN apt-get install -y wget && apt-get install -y gnupg2
#xvfb-run -a --server-args="-screen 0 1280x800x24 -ac -nolisten tcp -dpi 96 +extension RANDR"
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y google-chrome-stable

#RUN google-chrome-stable --headless --no-sandbox --disable-gpu --dump-dom https://www.mail.ru/
#CMD ["google-chrome-stable", "--no-sandbox", "--headless", "--disable-gpu", "--remote-debugging-address=0.0.0.0", "--remote-debugging-port=9222"]

#google-chrome-stable --headless --no-sandbox  --repl --crash-dumps-dir=./tmp https://www.chromestatus.com/

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# устанавлваем прогу cryptoPro
RUN apt-get -y install libccid pcscd opensc
# тут должно быть скачивание архива linux-amd64_deb.tgz
#RUN tar -xf linux-amd64_deb.tgz
#RUN cd linux-amd64_deb
#RUN ./install.sh cprocsp-rdr-pcsc cprocsp-rdr-rutoken cprocsp-rdr-cryptoki

# устанавливаем расширение крипто про
#RUN dpkg -i cprocsp-pki-cades-*-amd64.deb
#RUN dpkg -i cprocsp-pki-plugin-*-amd64.deb
#RUN chmod +x /app/chrome_ext.sh
#RUN /app/chrome_ext.sh

#RUN google-chrome-stable --headless --no-sandbox --screenshot https://www.mail.ru/

# install dependencies
RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx
RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# install chromedriver
#RUN apt-get -y install chromium-chromedriver
RUN apt-get install -y xvfb
RUN apt-get install -y zip
RUN apt-get install -y wget
RUN apt-get install -y ca-certificates

RUN wget -N https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/118.0.5993.32/linux64/chromedriver-linux64.zip
RUN unzip chromedriver-linux64.zip
RUN chmod +x chromedriver-linux64/chromedriver
RUN chmod +x chromedriver-linux64/LICENSE.chromedriver
RUN cp chromedriver-linux64/chromedriver /usr/local/bin
RUN cp chromedriver-linux64/LICENSE.chromedriver /usr/local/bin
RUN rm chromedriver-linux64.zip
RUN rm -R chromedriver-linux64

# install selenium
RUN pip install selenium

# Install any needed packages
RUN python setup.py develop

# Make port 8080 available to the world outside this container
EXPOSE 8080