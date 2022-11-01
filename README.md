**mr data: captain i see a klingon warbird de-cloaking in the logfiles**

 what's in a name?
 
 loogck = log + look + lock
 
 loogck a.k.a. l3   (d3,s3,bu3,...)


installing:
```git clone https://github.com/e7dal/loogck
cd loogck
poetry shell
poetry install
```

first create a proces that will genrate some random log:
```
$ pip install essential_generators
$ python scripts/generate_random_logs_logging.py &> data.txt&
```

and now try loogck with one of these commands:
```
$loogck data.txt -m static
$loogck data.txt -m bounce
$loogck data.txt -m hexify
```

(:you can also see these demo's in the demo folder:)
