# Continuous Integration with GitHub Actions
The project is made using python

### Task 0:
The CI is in place [![CI](https://github.com/ToujoursPareil8/holbertonschool-continuous_integration/actions/workflows/ci.yml/badge.svg)](https://github.com/ToujoursPareil8/holbertonschool-continuous_integration/actions/workflows/ci.yml)


### Task 1:
[proof of failure](https://github.com/ToujoursPareil8/holbertonschool-continuous_integration/actions/runs/32855317957/job/97825739899)

[proof of success](https://github.com/ToujoursPareil8/holbertonschool-continuous_integration/actions/runs/32855835849)


### Task 2:

[Proof of version testing](https://github.com/ToujoursPareil8/holbertonschool-continuous_integration/actions/runs/33058664956)


### Task 3:

| Elements | Before | After |
| :--- | :---: | :---: |
| **Run time** | [12s](https://github.com/ToujoursPareil8/holbertonschool-continuous_integration/actions/runs/33109131512)| [15s](https://github.com/ToujoursPareil8/holbertonschool-continuous_integration/actions/runs/33109607457) |

**Technical Note: Caching Overhead (Python vs. JavaScript)**
Caching this Python micro-project adds a slight time overhead because extracting the cache archive takes longer than downloading a single pip dependency. Conversely, JavaScript ecosystems generate massive dependency trees where raw installations take minutes, making caching instantly profitable. This setup is a proactive architectural investment to maintain pipeline speed as heavier libraries are integrated.


### Task 4:

The job is done [successfully](https://github.com/ToujoursPareil8/holbertonschool-continuous_integration/actions/runs/33113558422/job/98662407227)

# Building & Publishing Docker Images in CI


### Task 0:

Docker image build: [Builds successfully](https://github.com/ToujoursPareil8/holbertonschool-continuous_integration/actions/runs/33193527852)


### Task 1:

[GHCR package](https://github.com/ToujoursPareil8/holbertonschool-continuous_integration/pkgs/container/holbertonschool-continuous_integration/1183551639?tag=27830570938311e5f4f08b4e20127c531d7cfdd1)


### Task 2: