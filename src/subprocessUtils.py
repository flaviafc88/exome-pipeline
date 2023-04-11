import subprocess

class SubProcessUtils(object):
    @staticmethod
    def callJar(jarPath, paramList):
        #print('Call Jar')
        #print(jarPath)
        #print(paramList)
        params=['java', '-jar', jarPath] + paramList
        result=subprocess.check_output(params)
        return result
    
    @staticmethod
    def callLs(jarPath, paramList):
        params=['ls'] +  paramList + [jarPath]
        result=subprocess.check_output(params)
        return result

    @staticmethod
    def mergeFiles(fileList, destination):
        cmd = ['cat'] + fileList
        with open(destination, "w") as outfile:
            subprocess.run(cmd, stdout=outfile)