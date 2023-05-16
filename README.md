# Fourth down API client and data science helper

**![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/leetheperm/Forth-Down-API-client/python-package.yml)**
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/leetheperm/Forth-Down-API-client)

A python wrapper for the Fourth down play-by-play API written by Pratik Thanki


## Guide

### using the library

This library works best with Jupyter Notebooks, but can also be used as a python client in scripts. See the notebooks directory for a simple user guide.

Server side docs:

- Github: https://github.com/pratikthanki/FourthDown
- Site: https://fourthdown.azurewebsites.net/

### installation

clone this repository and then run  `pip install pip install .\fourth_down\` in your terminal

### Getting started


[Fourth down client demo](/notebooks/fourth_down_demo.ipynb) has examples of how to use this client for data science in a jupyter notebook.


### Endpoints supported

| Name| Endpoint     |Python Class | JSON | Pandas Dataframe    |
| :---       | :---        |    :----:   |         :---: |  :---:
|Game plays| `/api/game/plays` | Yes &check; | Yes &check;  |No &cross;|
|Game drives| `api/game/drives`   | No &cross;| Yes  &check;    | No &cross;|
|Scoring summaries| `api/game/scoringsummaries` | No &cross; | Yes &check; | No &cross;|
|NFL Fast R| `api/nflfastr`   | No &cross; | No  &cross; | No &cross;|
|Schedule| `api/schedule`   | No &cross;| Yes  &check;    | No &cross;|
|Results| `api/schedule/results`   | No &cross; | Yes &check;  | No &cross;|
|Teams| `api/teams`   | Yes &check;| Yes  &check; | No &cross;|

### Future improvements

- [ ] Add data frames / pandas support
- [ ] Add plots
- [ ] Handle non 200 responses


### Contributors
- Titusz https://github.com/tituszban
- Lee https://github.com/leetheperm/
