from utils import Utils
from subprocessUtils import SubProcessUtils
import sys

class MergeBan:
    def __init__(self, bamFolder, sampleName):
        self.bamFolder = bamFolder
        self.sampleName = sampleName
        self.picardJarPath = '/usr/local/bin/picard.jar'
        #self.picardJarPath = 'src/First.jar'
 
    @staticmethod
    def getSampleNameList(path):
        result=set()
        inputs = Utils.listFiles(path, '*.bam')
        for input in inputs:
            r=input.split('_L')[0]
            r=r.split('/')[-1]
            result.add(r)
        return list(sorted(result))

    def getSampleName(self):
        return self.sampleName

    def getPicardInputFiles(self):
        pattern = self.sampleName + '*_L*.bam'
        inputs = Utils.listFiles(self.bamFolder, pattern)
        return inputs

    def getPicardOutputFileName(self):
        return self.bamFolder + '/' + self.sampleName + '_merged.bam'

    def getPicardParams(self):
        params = ['MergeSamFiles']
        inputs = self.getPicardInputFiles()
        for input in inputs:
            file = 'I=' + input
            params.append(file)
        
        params.append('O=' + self.getPicardOutputFileName())
        return params
    
    def run(self):
        result=SubProcessUtils.callJar(self.picardJarPath, self.getPicardParams())
        print(result)
        # java -jar /usr/local/bin/picard.jar MergeSamFiles 
        # I=Exo-R01-0297_S1_L001.bam 
        # I=Exo-R01-0297_S1_L002.bam 
        # I=Exo-R01-0297_S1_L003.bam 
        # I=Exo-R01-0297_S1_L004.bam 
        # O=Exo-R01-0297_S1_merged.bam 
        # USE_THREADING=true
        
def argumentsOK():
    numberOfArguments = len(sys.argv)
    if (numberOfArguments != 3 and numberOfArguments != 2):
        print('mergeban.py requires at least 1 argument as follow:')
        print('python3 mergeban.py <bam_files_folder> <optional:sample_name_pattern>')
        print('examples:')
        print('python3 mergeban.py /tmp/exomes/bam_files/ Exo-R01-0297_S1')
        print('python3 mergeban.py /tmp/exomes/bam_files/')
        return False
    if not Utils.folderExists(sys.argv[1]):
        print(sys.argv[1] + ' folder not found.')
        return False
    if (numberOfArguments == 3 and len(sys.argv[2]) < 3):
        print('Invalid sample name pattern (too short).')
        return False
    return True

def getSampleNameArgument():
    numberOfArguments = len(sys.argv)
    if (numberOfArguments >= 3):
        return sys.argv[2]
    return None

def main():
    print('Initializing mergeban.py as a program')
    if argumentsOK():
        # mergeBan = MergeBan('/tmp/exomes/bam_files', 'Exo-R01-0297_S1')
        sampleName = getSampleNameArgument()
        path = sys.argv[1]
        if sampleName == None:
            sampleNameList=MergeBan.getSampleNameList(path)
            print('Processing all ban files in folder ' + path)
            print(len(sampleNameList), ' Samples found')
            for sampleName in sampleNameList:
                print('Processing ban files in folder ' + path + ' for sample name ' + sampleName)
                mergeBan = MergeBan(path, sampleName)
                mergeBan.run()
        else:
            print('Processing ban files in folder ' + path + ' for sample name ' + sampleName)
            mergeBan = MergeBan(path, sampleName)
            mergeBan.run()

if __name__ == '__main__':
    main()