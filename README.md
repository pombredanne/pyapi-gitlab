# pyapi-gitlab

pyapi-gitlab is a python wrapper for the [Gitlab API](https://github.com/gitlabhq/gitlabhq/tree/master/doc/api).

[![Build Status](https://travis-ci.org/Itxaka/pyapi-gitlab.svg?branch=develop)](https://travis-ci.org/Itxaka/pyapi-gitlab)
[![Coverage Status](https://coveralls.io/repos/Itxaka/pyapi-gitlab/badge.png?branch=develop)](https://coveralls.io/r/Itxaka/pyapi-gitlab?branch=develop)
[![PyPI](https://img.shields.io/pypi/v/pyapi-gitlab.svg)](https://pypi.python.org/pypi/pyapi-gitlab)
![PyPi downloads](https://img.shields.io/pypi/dm/pyapi-gitlab.svg)
[![Requirements Status](https://requires.io/github/Itxaka/pyapi-gitlab/requirements.svg?branch=develop)](https://requires.io/github/Itxaka/pyapi-gitlab/requirements/?branch=develop)
[![License](http://img.shields.io/pypi/l/pyapi-gitlab.svg)](https://www.apache.org/licenses/LICENSE-2.0.txt)
[![Docs](https://readthedocs.org/projects/pyapi-gitlab/badge/?version=latest)](http://pyapi-gitlab.readthedocs.org/)



## Requirements

- requests


## Naming convention

pyapi-gitlab has its own versioning in which the 2 first numbers indicates the Gitlab version that its supported for that library. a 7.5 version means that its compatible with the Gitlab 7.5 and lower API versions.

## Installation

```bash
pip install pyapi-gitlab
```

pyapi-gitlab supports python version 2.6, 2.7, 3.3 and 3.4


# Versions tested

| Gitlab version | Status |
|:-------------:| :-----:|
| 7.9.X      | :x:<sup>1</sup> |
| 7.8.X      | :heavy_check_mark: |
| 7.7.X      | :heavy_check_mark: |
| 7.6.X      | :heavy_check_mark: |
| 7.5.X      | :heavy_check_mark: |
| 7.4.X      | :heavy_check_mark: |
| 7.3.X      | :heavy_check_mark: |
| 7.2.X      | :heavy_check_mark: |
| 7.1.X      | :x:<sup>2</sup> |
| 7.0.X      | :x:<sup>3</sup>   |

1. 3 out of 17 tests failing: Seems that create snippet wall note now returns true/false instead of the created snippet. Snippet creating now does not return the created snippet. And move project does not return a dict either.
2. Label creation is not supported on this version.
3. Contributors endpoint seems to not exists in this version. Label creation is not supported on this version.

## Changelog

# 7.8.5

 - Use ```requests.json()``` instead of decoding everything (@satreix)
 - Add getmergerequestchanges (@bor-sh)
 - Add getmilestoneissues (@JonathonReinhart)
 - Add editproject (@nelg)
 - Add editgroupmember (@)
 - Fix hook metadata creation #137 (@jzelinskie)
 - Fix addprojectmember (@btall)
 - Fix Raise exception instead of returing it in creategroup (@brenard)

# 7.8.4

 - Just a bumped version, now that its tested and fully supports Gitlab versions up to 7.8

# 7.5.4

 - Change license to Apache 2.0
 - getproject now accepts a namespace/projectname as well like the gitlab api

# 7.5.3

 - New function wrapper ``getall`` to get all results from any function that provides pagination [Anirudh Dutt]
 - Remove pagination params from ``getdeploykeys``, ``getbranches`` and ``getsshkeys`` as they dont support it [Anirudh Dutt]
 - Add oAuth tokens to the login method [Ken Cochrane]
 - You can now add the type of hook when creating it [tonicbupt]
 - Allow Project Issues to be filtered by passing kwargs [Nick Whyte]
 - Update docs [Itxaka Serrano]

# 7.5.2

 - Support for the full Gitlab 7.5 API
 - Fix python 2.6 compatibility
 - All methods have documentation (Inside the library only, the docs are lagging a bit behind).
 - New fork api that allows to actually fork a project instead of doing fork relations
 - New label methods (getlabel, createlabel, editlabel, deletelabel)
 - All get* methods that return more than one item support pagination. Check page and per_page args. Default to first page and 20 items per page.
 - BREAKING CHANGE: Old sudo arg in methods to execute as other user is gone. Now there is a method setsudo(user_id/user_username) which will setup the header, so all the subsequent API calls will be done as that user. To get back to your user just do a setsudo() and the sudo parameter will be cleared
 - BREAKING CHANGE: Some methods were returning True or False instead of the object created. Now all the methods in which there is something returning from the server is returned as a dictionary/list of dictionaries to the user
 - BREAKING CHANGE: Some methods now use kwargs for the optional parameters so the code is more easy and readable. Methods affected: createproject, createprojectuser, createmilestone, editmilestone, updatemergerequest
 - BREAKING CHANGE: Project wallnotes does not exist anymore, seems that they have been moved to project snippets (getsnippets, getsnippet, createsnippet, deletesnippet)
 - BREAKING CHANGE: Removed getreadme method as its not part of the gitlab api, nor was it ever.
 - BREAKING CHANGE: Old methods that started with list* are not get*. This is done in order to have a proper naming convention instead of having mixed listsomething and then getsomething. The actual
 - BREAKING CHANGE: Old methods with new names: getownprojects -> getprojectsowned, getallprojects -> getprojectsall

## Examples/Documentation

Check the docs at [readthedocs.org](http://pyapi-gitlab.readthedocs.org)

## License

pyapi-gitlab is licensed under the Apache License 2.0. Check the LICENSE file.

## Built with PyCharm

Thanks to Jetbrains for giving me an Open Source license for PyCharm, it has helped making development much faster!

[![Pycharm](http://www.jetbrains.com/pycharm/docs/logo_pycharm.png)](https://www.jetbrains.com/pycharm/)
