#### CSV by columns splitter

Author: Ilya Rusin <ilya.rusin@protonmail.com>
Licence: MIT

### Installing for local development

  1. In Ubuntu/Linux Mint install Python 3.7 locally. See instructions at [Installing The Latest Python 3.7 On Ubuntu 16.04 / 18.04](https://websiteforstudents.com/installing-the-latest-python-3-7-on-ubuntu-16-04-18-04/) or [https://www.techiediaries.com/ubuntu-install-python/](https://www.techiediaries.com/ubuntu-install-python/).
  2. Clone repository into local folder using PyCharm.
  3. In `Settings -> Project Interpreter` add new Python 3.7 virtual environment.
  4. Open Terminal in PyCharm with `venv` activated and run `pip install -e .[dev]` for installing runtime dependencies and test framework.
  
 
### Code Style
[Google Python Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md) linted with `flake8`.
 
### Testing

Open Terminal in PyCharm with `venv` activated and run `make test`.


### Working with Git

  1. [GitLab Flow](https://docs.gitlab.com/ee/workflow/gitlab_flow.html) is assumed as best practice.
  2. `master` is protected branch. Only Scorista group maintainers allowed to merge into `master`.
  3. To implement new feature developer clones `develop` branch, commits changes and opens a Merge Requests into `develop` when work on current branch is done, tested and synchronized with current state of the `develop` branch.
  4. Developers are allowed to accept Merge Requests into `develop`.
  5. Merge Requests into `master` allowed only if current state of `develop` is synchronized with master, contains only new commits without rebasing past git history and all tests passes.
  6. Merge Requests into `master` getting merged by Maintainer after code passes Code Review not more often than once a workday between 9.00 - 12.00 GMT+03.
  
### LICENSE

MIT