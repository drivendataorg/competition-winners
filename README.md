[<img src='https://s3.amazonaws.com/drivendata-public-assets/logo-white-blue.png' width="600">](https://www.drivendata.org/)
<br><br>

## Background

DrivenData runs machine learning competitions to help non-profits, NGOs, governments, and other social impact organizations use data science in service of humanity. Part of DrivenData's mission is to enable data scientists and non-profits to learn from the work that is done in these competitions. To this end, the code submitted by winners for almost all DrivenData competitions are released under a permissive open source license for others to learn from, use, and adapt.

## What's in this Repository

This repository makes it easy to find code prodvided by the winners of [competitions](https://www.drivendata.org/competitions/) hosted on DrivenData. Use the list below to browse to any particular competition's winning repository; or, you can clone this repository to get all of the code at once.

### Winning Submissions

| Competition
| ---
| [America's Next Top (Statistical) Model](https://github.com/drivendataorg/americas-next-top-statistical-model)
| [Box-Plots for Education](https://github.com/drivendataorg/box-plots-for-education)
| [Countable Care: Modeling Women's Health Care Decisions](https://github.com/drivendataorg/countable-care)
| [From Fog Nets to Neural Nets](https://github.com/drivendataorg/from-fog-nets-to-neural-nets)
| [Keeping it Fresh: Predict Restaurant Inspections](https://github.com/drivendataorg/keeping-it-fresh)
| [Naive Bees Classifier](https://github.com/drivendataorg/naive-bees-classifier)
| [Senior Data Science: Safe Aging with SPHERE](https://github.com/drivendataorg/senior-data-science)
| [Pri-matrix Factorization](https://github.com/drivendataorg/pri-matrix-factorization)
| [Pover-T Tests: Predicting Poverty](https://github.com/drivendataorg/pover-t-tests)
| [Random Walk of the Penguins](https://github.com/drivendataorg/random-walk-of-the-penguins)
| [N+1 Fish, N+2 Fish](https://github.com/drivendataorg/n-plus-one-fish)
| [Power Laws: Forecasting Energy Consumption](https://github.com/drivendataorg/power-laws-forecasting)
| [Power Laws: Anomaly Detection](https://github.com/drivendataorg/power-laws-anomalies)
| [Power Laws: Optimizing Demand-side Strategies](https://github.com/drivendataorg/power-laws-optimization)
| [Power Laws: Cold Start Energy Forecasting](https://github.com/drivendataorg/power-laws-cold-start)
| [Sustainable Industry: Rinse Over Run](https://github.com/drivendataorg/rinse-over-run)
| [Open AI Caribbean Challenge: Mapping Disaster Risk from Aerial Imagery](https://github.com/drivendataorg/open-ai-caribbean)
| [Hakuna Ma-data: Identify Wildlife on the Serengeti with AI for Earth](https://github.com/drivendataorg/hakuna-madata)
| [Open Cities AI Challenge: Segmenting Buildings for Disaster Resilience](https://github.com/drivendataorg/open-cities-ai-challenge)
| [Clog Loss: Advance Alzheimer’s Research with Stall Catchers](https://github.com/drivendataorg/clog-loss-alzheimers-research)
| [TissueNet: Detect Lesions in Cervical Biopsies](https://github.com/drivendataorg/tissuenet-cervical-biopsies)
| [Wind-dependent Variables: Predict Wind Speeds of Tropical Storms](https://github.com/drivendataorg/wind-dependent-variables)
| [MagNet: Model the Geomagnetic Field](https://github.com/drivendataorg/magnet-geomagnetic-field)
| [Genetic Engineering Attribution Challenge](https://zenodo.org/record/4774228#.YQRNnXVKgkF)
| [Hateful Memes](https://github.com/drivendataorg/hateful-memes.git)
| [Overhead Geopose Challenge](https://github.com/drivendataorg/overhead-geopose-challenge)
| [STAC Overflow: Map Floodwater from Radar Imagery](https://github.com/drivendataorg/stac-overflow)
| [Image Similarity Challenge](https://github.com/drivendataorg/image-similarity-challenge)
| [Deep Chimpact Challenge](https://github.com/drivendataorg/deep-chimpact-winners)
| [On Cloud N: Cloud Cover Detection Challenge](https://github.com/drivendataorg/cloud-cover)
| [Mars Spectrometry: Detect Evidence for Past Habitability](https://github.com/drivendataorg/mars-spectrometry)
| [NASA Airathon: Predict Air Quality](https://github.com/drivendataorg/nasa-airathon)
| [Where's Whale-do?](https://github.com/drivendataorg/wheres-whale-do)
| [Run-way Functions: Predict Reconfigurations at US Airports](https://github.com/drivendataorg/nasa-airport-config)
| [Snowcast Showdown](https://github.com/drivendataorg/snowcast-showdown)
| [Mars Spectrometry 2: Gas Chromatography](https://github.com/drivendataorg/mars-spectrometry-gcms)
| [The BioMassters](https://github.com/drivendataorg/the-biomassters)
| [Tick Tick Bloom: Harmful Algal Bloom Detection Challenge](https://github.com/drivendataorg/tick-tick-bloom)
| [VisioMel Challenge: Predicting Melanoma Relapse](https://github.com/drivendataorg/visiomel-melanoma)
| [Meta AI Video Similarity Challenge](https://github.com/drivendataorg/video-similarity-challenge)
| [Pushback to the Future: Predict Pushback Time at US Airports](https://github.com/drivendataorg/nasa-airport-pushback)
| [Unsupervised Wisdom: Explore Medical Narratives on Older Adult Falls](https://github.com/drivendataorg/unsupervised-wisdom)
| [Pale Blue Dot: Visualization Challenge](https://github.com/drivendataorg/pale-blue-dot)
| [Kelp Wanted: Segmenting Kelp Forests](https://github.com/drivendataorg/kelp-wanted)
| [SNOMED CT Entity Linking Challenge](https://github.com/drivendataorg/snomed-ct-entity-linking)
| [Pose Bowl: Spacecraft Detection and Pose Estimation Challenge](https://github.com/drivendataorg/pose-bowl-spacecraft-challenge)
| [Water Supply Forecast Rodeo](https://github.com/drivendataorg/water-supply-forecast-rodeo)
| [Youth Mental Health Narratives Challenge](https://github.com/drivendataorg/youth-mental-health)
| [Goodnight Moon, Hello Early Literacy Screening](https://github.com/drivendataorg/goodnight-moon)

## Using this repository

This repository includes each competition's winners repository using git's [submodule](https://github.blog/2016-02-01-working-with-submodules/) functionality. Note that when any repo containing submodules is cloned, each submodule needs to be initialized else they remain empty.

### Cloning this repository with all submodules directly

To avoid explicitly initializing each submodule, use the `--recursive` flag when cloning:

`git clone --recursive https://github.com/drivendata/competition-winners.git`.

This will download the `competition-winners` repository, as well as the contents of _every_ submodule in the winners repository.

### Download submodules for already-cloned repository

If you've already cloned this repository without the `--recursive` flag and the submodules are empty, use the following command to download them:

```bash
git submodule update --init --recursive
```
