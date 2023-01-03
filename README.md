# MM-quecat - a unified multi-model query tool

This repository contains the proof-of-concept implementation of MMQL, a multi-model query language based on category theory, which I proposed in my master's thesis.

Using MMQL, you can query data stored in a variety of different databases in a unified way with a single query, greatly simplifying access to multi-model data, as you only need to use a single query language instead of N query languages for N databases. In addition, you don't need to worry about joining together data from different databases, as MMQL does it for you automatically.

For the theoretical background, please refer to my master's thesis (link will be added when it is published).
You can also check out the demo paper about MM-quecat (link will be added when it is published), which showscases its functionality.

## Installation

Firstly, you will need a functioning instance of [MM-evocat](https://mm-evocat.com/), with a configured set of databases, schema category and mappings. Please refer to the MM-evocat docs for more details on how to do this. However, for now you cannot use any version of MM-evocat, as for the development of my thesis, it was necessary to freeze the version of MM-evocat to work with a consistent API. In addition, I had to make a number of custom modifications to MM-evocat in places where the required functionality for MM-quecat was not complete. For this reason, it is necessary to use the [modified version of MM-evocat](https://github.com/yawnston/evolution-management) until the required changes are made by its author, at which point MM-quecat will be able to use the live version of MM-evocat.

In addition, you will need Python 3.8 or newer. To install the required packages to run MM-quecat, run `pip install -r requirements.txt`.

I personally recommend that you run MM-evocat as well as the databases with data in Docker containers. Using the docker-compose file provided [here](https://gist.github.com/yawnston/5dbff710cff2e73d74a1412aafc5dc71), consider the following folder structure:

```
<project-root>/
    evolution-management/
        ...
    querycat/
        ...
    docker-compose.yaml
```

The folder `querycat` contains this repository, and the folder `evolution-management` contains the repository with the modified version of MM-evocat. If you follow the installation guide for MM-evocat correctly, with this setup you will get a neat, containerized MM-evocat instance with all required databases in the same docker-compose file, all communicating on the same Docker network.

Be aware that while running MM-quecat is really simple, unfortunately configuring and running MM-evocat is really complicated, and even though I tried to simplify it as much as possible with the Dockerfiles and the docker-compose I added, you will still need to mess about with a bunch of Java configs according to MM-evocat's docs. You currently need to define the schema category and mappings by yourself in MM-evocat which can be bothersome, but maybe in the future we can use [MM-infer](https://openproceedings.org/2022/conf/edbt/paper-142.pdf) to do this automatically.

## Usage

The interface for MM-quecat is very simple - there is a single function `execute_query(query_string: str, schema_id: int, mmcat_base_url: str)` in the file `src/quecat.py`, which accepts the MMQL query string, as well as the ID of the schema category in MM-evocat which should be used for this query, and finally also the base URL to the MM-evocat instance.

This function returns a single value - an instance category (again, please refer to my thesis for an explanation of what this is). The final idea is to return the chosen representation of the result like JSON or RDF, but unfortunately MM-evocat does not support the conversion of an instance category into these formats yet, which is why we can only return the instance category at this moment.

You can either use MM-quecat as a library as described above, or you can edit the main function in `src/querycat.py` according to your wishes and run that (but make sure to set your `PYTHONPATH` environment variable to the workspace root, otherwise the imports won't work).

## Experiments

If you have a MM-evocat instance correctly configured, you can also run the experiments described in my master's thesis (Chapter 8). Each of the three experiments is in its own Python source file in the `experiments` folder: `postgresql_native.py`, `mongodb_native.py` and `cross_db.py`. Running any of these files (again, provided you have a running MM-evocat instance) will run the corresponding experiment, printing out timing information at the end.

You can adjust the parameters of the experiments in the `experiments/setting.py` file, which contains a simple list of things you can change about the experiments, like the size of data used or URL to the databases. Note that if you change the database URL in this settings file, you will also need to change the database URL in MM-evocat for the experiments to work correctly, as the experiments access the same database both from Python code and via MM-evocat.

## Code structure

The structure of the code is relatively simple, loosely following the strucutre of the proposed algorithms from my master's thesis:

- Code related to __parsing__ the query is in `src/parsing/`
- The automatically generated client code for MM-evocat using its OpenAPI spec is in `src/open_api_definition_client/`
- Code which builds query and join plans is in `src/querying/`
- Database wrappers are in `src/wrappers/`
- Code which merges instance categories together (using MM-evocat) is in `src/merging/`
- Code which performs projection on the query results is in `src/projection/`
- Experiments from the thesis are located in `src/experiments/`

The repo also contains a couple of extra folders, namely `grammars/` which contains the MMQL grammar in the file `Querycat.g4`, and `notes/` which contains my personal notes I was making during the writing of my thesis. Don't expect to find anything useful in the notes, it's just a convenient place where I could keep my notes safe and versioned.

## Development

Even though Python is dynamically typed, prefer to use static typing where possible. This project also follows [PEP8](https://peps.python.org/pep-0008/) styling where possible. Formatting/linting is done with [Black](https://github.com/psf/black), which is automatically run in GitHub Actions for every commit, failing if any issues are found.
