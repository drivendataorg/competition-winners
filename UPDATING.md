# Pulling the latest from the submodules

If submodule projects are updated, you can pull the most recent version into the main project using:

`git submodule update --remote --merge`

from the `competition-winners` repository root directory.

Running `git status` should now show which modules have been updated. Now, `git add .` and commit with a message like `"Merge submodule updates"`.

# Adding a competition repository as a submodule of this repository

 1. Once a competition repository is ready to be added as a submodule, clone this repository using:

`git clone --recursive https://github.com/drivendata/competition-winners.git`.

 2. Then, in the root directory run:

`git submodule add https://github.com/drivendataorg/name-of-competition-repo name-of-competition-repo`.

This will update the `.gitmodules` file to point to the competition repo url and collect the contents under the path `name-of-competition-repo` on the competition winners repository page. Running `git status` should show

```
modified:   .gitmodules
new file:   name-of-competition-repo
```

 3. Add a link to the competition table in the readme

 4. Complete the update by staging `README.me`, `.gitmodules` and `name-of-competition-repo` then committing the changes to master. The new submodule should now appear on the remote page.


