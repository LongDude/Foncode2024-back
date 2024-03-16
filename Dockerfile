FROM python:3.9-buster

RUN apt-get update

#php postgres
#RUN apt-get install -y libpq-dev \
#    && docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \
#    && docker-php-ext-install pdo pdo_pgsql pgsql



#zsh
RUN apt-get install -y zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

RUN git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git ~/.zsh/zsh-autocomplete
RUN echo "source ~/.zsh/zsh-autocomplete/zsh-autocomplete.plugin.zsh" >> ~/.zshrc
RUN sed -i 's/robbyrussell/lukerandall/g' ~/.zshrc

ENV LC_CTYPE C.UTF-8


#django
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html

COPY requirements.txt ./
RUN pip install -r requirements.txt

CMD python manage.py migrate && python manage.py createsuperuser --noinput && python manage.py runserver 0.0.0.0:8000