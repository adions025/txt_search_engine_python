# Text search engine

A command line driven text search engine using Python 3.6 and the Map Reduce approach.
The search take the words given on the prompt and return a list of the top 10
matching filenames in rank order, giving the rank score against each match.

## Requirements

* Python 3.6
* pytest

## Installation

1. Clone this repository / unzip
2. Install dependencies
 ```
   pip install -r requirements.txt
 ```

**Python 3.6 is needed**

- If you are using other Python version, please install 3.6
- If you are using conda envs:
1)
     ```
       conda create -n myenv python=3.6 pytest
     ```
2)    
     ```
       conda activate myenv
     ```
   
## Usage

**args:**
* --h: help (optional arg)
* --command: search
* --path: /to/path/files/

**e.g.**
```
$ python main.py search --path /to/path/files/
```


## Test

The __../data/__ folder has been created to do some test and has been tested in Windows os.

To run tests:

```
$ pytest
```

or specific test:

```
$ pytest tests/test_files.py::test_find_results
```

## Author

* **Adonis González Godoy** ([Email](adions025@gmail.com) - [Github](https://github.com/adions025))