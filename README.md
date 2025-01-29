# Getting started on Windows

For the impatient: **without installation** head in your browser to https://nbviewer.org/github/exoosh/kaffeeklatsch-python3-intro/tree/main/

## Installing prerequisites on Windows

* in the start menu search enter `cmd`
    * **NB:** this can be done unelevated!
* `winget install -e --id Python.Python.3.13`
* `winget install -e --id astral-sh.uv`
* `uv tool install notebook`
    * `setx PATH "%USERPROFILE%\.local\bin;%PATH%"` (required to be able to invoke `jupyter-notebook`)

## Then download this

* E.g. click the green "Code" button then choose "Download ZIP"
    * unpack the ZIP with right-click "Extract ..."
* ... or `git clone` this repository
* Head into that directory where you unpacked the ZIP or cloned this repo
* invoke `jupyter-notebook`