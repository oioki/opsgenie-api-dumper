# opsgenie-api-dumper

```
usage: opsgenie_api_dumper.py [-h] -k KEY [-r {eu,us}] [-o OUTPUT]

Dump all available data having Opsgenie API key

optional arguments:
  -h, --help            show this help message and exit
  -k KEY, --key KEY     Opsgenie API key
  -r {eu,us}, --region {eu,us}
                        Region for Opsgenie API
  -o OUTPUT, --output OUTPUT
                        Local directory to dump data
```


## Example

```
$ ./opsgenie_api_dumper.py -k REDACTED
... v2/alerts
... v1/incidents
... v2/integrations
    [SNIP]
```
