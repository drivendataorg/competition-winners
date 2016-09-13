## competition-winners

Note that when any repo containing submodules is cloned, each submodule needs to be initialized else they remain empty.

To avoid explicitly initializing each submodule, use the `--recursive` flag when cloning:

`git clone --recursive https://github.com/drivendata/competition-winners.git`

If submodule projects are updated, merge the most recent version into the main project using:

`git submodule update --remote —merge`



