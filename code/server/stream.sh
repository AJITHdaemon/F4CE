chmod 777 temp.mkv &
python ../client/main.py &
echo "y" | ffmpeg -f alsa -ac 2 -ab 128k -i pulse -f x11grab -s 1366x768 -r 30 -i :0.0 -acodec libmp3lame -vcodec libx264 -vtag X264 temp.mkv &
