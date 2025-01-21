# Code Citations

## License: unknown
https://github.com/spladug/wessex/tree/13db2ec81e9e1a7eecf9f52c22698035ff53f53a/.github/workflows/python-publish.yaml

```
on: ubuntu-latest

       steps:
       - uses: actions/checkout@v2

       - name: Set up Python
         uses: actions/setup-python@v2
         with:
           python-version: '3.8'

       - name: Install dependencies
         run: |
           python -m pip install -
```


## License: MIT
https://github.com/matthewwithanm/python-markdownify/tree/e6e23fd512ce85c7a6548791903f6507bd109345/.github/workflows/python-publish.yml

```
steps:
       - uses: actions/checkout@v2

       - name: Set up Python
         uses: actions/setup-python@v2
         with:
           python-version: '3.8'

       - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install
```


## License: MIT
https://github.com/MatterMiners/lapis.caching/tree/e79b720796c49be3a8816c7eb929ece4106ab60b/.github/workflows/linter.yml

```
, pull_request]

   jobs:
     build:
       runs-on: ubuntu-latest

       steps:
       - uses: actions/checkout@v2

       - name: Set up Python
         uses: actions/setup-python@v2
         with:
           python-version: '3.8'

       - name: Install dependencies
```

