# dotfiles

My config of nvim,which is used to write code and tex.The pdf reader is zathura and the code complete is github's copolit.

# Usage

## remove the date out of date
```shell
sudo rm -rf ~/.local/share/nvim ~/.local/state/nvim ~/.cache/nvim
```
## install support
```shell
sudo apt-get install python3-venv python3-pip
```

## install neovim and support
```shell
sudo add-apt-repository ppa:neovim-ppa/unstable
sudo apt update
sudo apt install neovim gcc g++ make
```

## install copilot support
Download from web https://nodejs.org/en/download/
```shell
sudo apt install python3 make python3-pip 
tar -zxvf node-***.tar.gz
./configure
make -j4
sudo make install
```

# install zsh and config
```shell
sudo apt install zsh
# install oh-my-zsh
cd ~/.dotfile/zsh/
bash install.sh
# install theme
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
# install plugins
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

# install anaconda
dowload the install-package from web.
```shell
tar -zxvf anaconda-***.tar.gz
./Anaconda-***.sh
```
