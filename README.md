# Hydra Template

## Installation

```
pip3 install hydra-core --upgrade
```

## Program Flow

`run.py`

Acts as an entry point

Role:
- Instantiates dotenv and read params
- Reads nested configuration that starts with configs/index.yaml
- Composes a final configuration from cmd line args, dotenv, and file-based config.
- Sets up the quality of life functions
- Prints the config to screen for sanity and to file for posteriority
- Starts execution of the main process through `src.exec.start`

Calls:
- src/utils
- src/exec/start

Depends on:
- configs/index.yaml
---

`src/exec`

Acts as the main process

Role:
- Utilizes the composed config and conditionally execute the main program loop

---

`configs/index.yaml`

Acts as primary file configuration

Role:
- Defines root variables
- Defines branches such as `configs/nested` and assigns default path
- Defines how hydra creates the output directories for each job run

---

`configs/nested`

Example of Nested Config, available through command line as nested={leaf-yaml}

Role:
- Provides a primary config through `configs/nested/default.yaml`
- Provides logic to selectively override the variables in default config via `configs/nested/alternative.yaml`