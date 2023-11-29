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

# if meet error "E5108:Error executing lua ~/.local/share/nvim/lazy/LazyVim/lua/lazyvim/util/ui.lua:attempt to index local 'ret'(a nil value)"

```lua
function M.get_signs(buf, lnum)
  -- Get regular signs
  ---@type Sign[]
  local signs = vim.tbl_map(function(sign)
    ---@type Sign
    local ret = vim.fn.sign_getdefined(sign.name)[1]
    if ret ~= nil then --------------| Lines in Question
      ret.priority = sign.priority --|
      return ret                   --|
    end -----------------------------|
  end, vim.fn.sign_getplaced(buf, { group = "*", lnum = lnum })[1].signs)

  -- Get extmark signs
  local extmarks = vim.api.nvim_buf_get_extmarks(
    buf,
    -1,
    { lnum - 1, 0 },
    { lnum - 1, -1 },
    { details = true, type = "sign" }
  )
  for _, extmark in pairs(extmarks) do
    signs[#signs + 1] = {
      name = extmark[4].sign_hl_group or "",
      text = extmark[4].sign_text,
      texthl = extmark[4].sign_hl_group,
      priority = extmark[4].priority,
    }
  end
```
