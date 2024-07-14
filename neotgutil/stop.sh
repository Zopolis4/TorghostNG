crontab_content=$(crontab -l)
modified_content=$(echo "$crontab_content" | grep -v "neotorghost -r")
echo "$modified_content" | crontab -