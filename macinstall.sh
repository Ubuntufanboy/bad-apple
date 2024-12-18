mkdir .venv

python3 -m venv .venv
brew install ffmpeg
pip3 install tqdm
pip3 install numpy
pip3 install pygame

git clone https://github.com/Ubuntufanboy/ascii-video-player
cd ascii-video-player
cd src


git clone https://www.github.com/Ubuntufanboy/bad-apple.git
cd bad-apple

pip3 install brotli
brew install yt-dlp
pip3 install Pillow

chmod +x remote.sh
