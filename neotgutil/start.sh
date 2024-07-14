cmd="neotorghost -r"
cj="*/5 * * * * $cmd"
echo "$cj" > /tmp/mcj
crontab /tmp/mcj; rm /tmp/mcj