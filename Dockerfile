FROM alpine:latest
RUN apk add --no-cache git bash
WORKDIR /root
RUN git config --global user.name "rishav1305" && \
    git config --global user.email "rishav.chatt@gmail.com"
VOLUME ["/root"]
#ENTRYPOINT ["git"]
CMD ["/bin/bash"]