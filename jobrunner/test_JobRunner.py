import unittest
from JobRunner import JobRunner


class TestJobRunner(unittest.TestCase):

    def testSingleJob(self):
        config = [{"name": "job1"}]
        runner = JobRunner(config)
        self.assertEquals(["job1"], runner.getRunListFor("job1"))

    def testDoubleRun(self):
        config = [{"name": "job1"}]
        runner = JobRunner(config)
        self.assertEquals(["job1"], runner.getRunListFor("job1"))

    def testJsonLoad(self):
        config = '[{"name":"job1"}]'
        runner = JobRunner.fromJson(config)
        self.assertEquals(["job1"], runner.getRunListFor("job1"))

    def testEmptyConfig(self):
        config = []
        runner = JobRunner(config)
        self.assertRaises(KeyError, runner.getRunListFor, ["job1"])

    def testHierarchy(self):
        config = [{"name": "minifyjs"},
                  {"name": "minifycss"},
                  {"name": "minify", "depend": ["minifyjs", "minifycss"]},
                  {"name": "make", "depend": ["minify"]}]
        runner = JobRunner(config)
        self.assertEquals(["minifyjs", "minifycss", "minify", "make"], runner.getRunListFor("make"))

    def testRunOnlyOnce(self):
        config = [
            {"name": "init"},
            {"name": "job1", "depend": ["init"]},
            {"name": "job2", "depend": ["init"]},
            {"name": "startJob", "depend": ["job1","job2"]}
        ]
        runner = JobRunner(config)
        self.assertEquals(["init","job1","job2","startJob"], runner.getRunListFor("startJob"))

if __name__ == '__main__':
    unittest.main()
