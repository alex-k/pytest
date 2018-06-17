from pprint import pprint
from jobrunner.JobRunner import *

configJson = '[{"name": "minifyjs"}, {"name": "minifycss"}, {"name": "minify", "depend": ["minifyjs","minifycss"]}, {"name": "make", "depend": ["minify"]}]'

jobRunner = JobRunner.fromJson(configJson)
jobs = jobRunner.getRunListFor("make")

pprint(jobs)
