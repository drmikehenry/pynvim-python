# `pynvim-python`

## Introduction

`pynvim-python` is a thin wrapper designed to expose the Python interpreter
associated with Neovim's `pynvim` library. When placed on the executable `PATH`,
`pynvim-python` chains to the Python interpreter associated with `pynvim`,
essentially providing a renamed Python interpreter that won't collide with other
Python interpreters on `PATH`.

## Installation

Typical installation uses `uv`[^1] or `pipx`[^2] to install `pynvim-python` on
the `PATH`, e.g.:

- For `uv`:

  ```sh
  uv tool install pynvim-python
  ```

- For `pipx`:

  ```sh
  pipx install pynvim-python
  ```

## Post-installation Neovim configuration

After installing `pynvim-python`, configure Neovim to use it by setting the
global variable `python3_host_prog` to be the string `pynvim-python`:

- Via Vimscript in `init.vim`:

  ```vim
  let g:python3_host_prog = 'pynvim-python'
  ```

- Via Lua in `init.lua`:

  ```lua
  vim.g.python3_host_prog = 'pynvim-python'
  ```

## References

[^1]: https://docs.astral.sh/uv/
[^2]: https://pipx.pypa.io/stable/
