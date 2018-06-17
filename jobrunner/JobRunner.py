import json
class JobRunner:
    config = []

    def __init__(self, config=[]):
        self.config = config

    @staticmethod
    def fromJson(configJson):
        return JobRunner(json.loads(configJson))

    def __findJob(self, jobName):
        for job in self.config:
            if (job.get("name") == jobName):
                return job
        raise KeyError('Can not find job with name {}'.format(jobName))


    def __addJobWithDependencies(self, jobName, jobList=[], jobMap={}):
        job = self.__findJob(jobName)
        for dependencyName in job.get("depend",[]):
            self.__addJobWithDependencies(dependencyName, jobList, jobMap)

        if(not jobMap.has_key(jobName)):
            jobList.append(jobName)
            jobMap[jobName]=jobName

        return jobList

    def getRunListFor(self, jobName):
        return self.__addJobWithDependencies(jobName,[], {})
