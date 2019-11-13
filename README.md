Stuff You Should Know
=====================


You can't know everything, but you should know a little bit about this
stuff. Try something new! Here's some stuff from my configs and my
history on my work computer. Make of it what you will!


- `brew`
- `tldr`
- `zsh` (see `antigen` and the `.zshrc` below)
- `git`
- Copy the contents of the example dotfiles into your `~/.zshrc` and
  `~/.gitconfig` respectively.
- `chsh`
- `tmux`
- `pkill`
- `cat`
- `|` (pipe)
- `>`, `>>` (stream redirection (`stdout`))
- `<` (stream redirection (`stdin`))
- `httpie` (`http` once installed -- nice command line HTTP interface --
  think postman for the command line)
- `fd` (find files by name better than `find`)
- `rg` (find strings in files better than `ack`, `ag`, etc.,)
- `z` (this is an antigen package -- see antigen's page for install
  instructions)
- `fzf` (this is way cooler with the terminal integration (`[ -f
  ~/.fzf.zsh ] && source ~/.fzf.zsh`)

```sh
$ cat ~/.zshrc
# Antigen stuff
source /usr/local/share/antigen/antigen.zsh

antigen use oh-my-zsh
antigen use rupa/z
antigen bundle git
antigen bundle kubectl

antigen bundle zsh-users/zsh-syntax-highlighting
antigen theme geometry-zsh/geometry
antigen apply

# An alias
alias gcan=git commit --ammend --no-edit

# A personal helper function
convert_music () { ffmpeg -i $1 -f mp3 -acodec libmp3lame -ab 320000 -ar 44100 $2 }

# Make my history longer
HISTFILE=/Users/ac/.zsh_history
HISTSIZE=100000
SAVEHIST=100000
```
