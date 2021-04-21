FROM nginx

RUN rm /etc/nginx/conf.d/default.conf && \
    apt-get update && \
    apt-get -y install lsb-release && \
    apt-get -y install software-properties-common && \
    apt-get -y install gnupg2 && \
    apt-get -y install wget && \
    apt-get -y install unzip && \
    apt-get -y install supervisor && \
    curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - && \
    apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" && \
    apt-get update && \
    apt-get -y install consul 

COPY load-balancer.conf.ctmpl /etc/nginx/conf.d/load-balancer.conf.ctmpl
COPY consul-template-config.hcl .
COPY supervisor.conf /etc/supervisor.conf

RUN wget https://releases.hashicorp.com/consul-template/0.25.2/consul-template_0.25.2_linux_amd64.zip && \
    unzip consul-template_0.25.2_linux_amd64.zip -d /usr/sbin/

CMD ["supervisord", "-n", "-c", "/etc/supervisor.conf"]