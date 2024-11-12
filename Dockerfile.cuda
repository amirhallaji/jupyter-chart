FROM nvidia/cuda:12.6.2-cudnn-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive \
    SHELL=/bin/zsh \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /srv/jupyterhub

RUN apt-get update -qq && \
    apt-get install -yqq --no-install-recommends \
    ca-certificates \
    curl \
    gnupg \
    locales \
    nodejs \
    npm \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    libopenblas-dev \
    liblzma-dev \
    python3 \
    python3-pip \
    zsh \
    git \
    fonts-powerline && \
    locale-gen en_US.UTF-8 && \
    npm install -g configurable-http-proxy@^4.2.0 && \
    npm cache clean --force && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /var/log/* /var/tmp/* ~/.npm

RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended && \
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions && \
    sed -i 's/plugins=(git)/plugins=(git zsh-autosuggestions)/' ~/.zshrc && \
    chsh -s $(which zsh)

RUN ln -sf /usr/bin/python3 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip

RUN python3 -m pip install --no-cache-dir \
    jupyterhub==5.0.0 \
    notebook \
    numpy \
    pandas \
    matplotlib

COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

RUN chown 777 . && \
    chmod 777 -R /srv/jupyterhub

USER nobody

EXPOSE 8000

WORKDIR /srv/jupyterhub

CMD ["jupyterhub", "-f", "/etc/jupyterhub/jupyterhub_config.py"]
