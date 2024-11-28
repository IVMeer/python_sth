# root= \\192.168.30.17\video\anti-thief-oss\

root_dir = \\192.168.30.17\\video\\anti-thief-oss\\20241022\\

find "$root_dir" -type d -name "*_scanning*" | while read folder; do
    find "$folder" -type f -name "*.json"
done
