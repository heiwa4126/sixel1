# sixel1

Windows Terminal 1.22 以降で Sixel に対応したらしいので、そのテスト。

libsixel を使わずに Python だけでやってみる

## 実行

1. Windows Terminal 1.22 以降で (tmux 不可)
2. WSL や ssh でつないだ Linux 等にこのプロジェクトをクローンして

```sh
uv sync
uv run sixel1
```

## Windows だと

[lubosz/python-sixel](https://github.com/lubosz/python-sixel)が、
POSIX にしか存在しない termios を呼ぶので動きません。
