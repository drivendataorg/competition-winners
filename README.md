[<img src='https://community.drivendata.org/uploads/default/optimized/1X/e055d38472b1ae95f54110375180ceb4449c026b_1_690x111.png'>](https://www.drivendata.org/)
<br><br>

## What's in this Repository
This repository contains code volunteered from leading competitors in the [competitions](https://www.drivendata.org/competitions/) hosted on DrivenData.

## Winning Submissions

| Competition
| ---
| [America's Next Top (Statistical) Model](https://github.com/drivendataorg/americas-next-top-statistical-model)
| [Box-Plots for Education](https://github.com/drivendataorg/box-plots-for-education)
| [Countable Care: Modeling Women's Health Care Decisions](https://github.com/drivendataorg/countable-care)
| [From Fog Nets to Neural Nets](https://github.com/drivendataorg/from-fog-nets-to-neural-nets)
| [Keeping it Fresh: Predict Restaurant Inspections](https://github.com/drivendataorg/keeping-it-fresh)
| [Naive Bees Classifier](https://github.com/drivendataorg/naive-bees-classifier)
| [Senior Data Science: Safe Aging with SPHERE](https://github.com/drivendataorg/senior-data-science)

<br><br>

## Cloning this repository

Note that when any repo containing submodules is cloned, each submodule needs to be initialized else they remain empty.

To avoid explicitly initializing each submodule, use the `--recursive` flag when cloning:

`git clone --recursive https://github.com/drivendata/competition-winners.git`.

This will download the `competition-winners` repository, as well as the contents of _every_ submodule in the winners repository.

If submodule projects are updated, merge the most recent version into the main project using:

`git submodule update --remote —-merge`

## Adding a competition repository as a submodule of this repository

Once a competition repository is ready to be added as a submodule, clone this repository using:

`git clone --recursive https://github.com/drivendata/competition-winners.git`.

Then, in the root directory run:

`git submodule add https://github.com/drivendataorg/name-of-competition-repo name-of-competition-repo`.

This will update the `.gitmodules` file to point to the competition repo url and collect the contents under the path `name-of-competition-repo` on the competition winners repository page.
