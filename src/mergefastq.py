from utils import Utils
from subprocessUtils import SubProcessUtils
import sys
#/home/flavia.costa/disk1/exomes-DEC-2022/fev/Dados_brutos
class MergeFastq:
    def __init__(self, fastqFolder):
        self.fastqFolder = fastqFolder
 
    @staticmethod
    def getSampleNameList(path):
        # result = set()
        inputs = Utils.listFiles(path, '*L001*.fastq.gz')
        # cat Exo-R01-0012_S12_L001_R2_001.fastq.gz Exo-R01-0012_S12_L002_R2_001.fastq.gz 
        # Exo-R01-0012_S12_L003_R2_001.fastq.gz Exo-R01-0012_S12_L004_R2_001.fastq.gz > Exo-R01-0012_R2.fastq.gz
        return sorted(inputs)

    @staticmethod
    def getSampleFileList(path):
        l1 = path
        l2 = path.replace('L001', 'L002')
        l3 = path.replace('L001', 'L003')
        l4 = path.replace('L001', 'L004')
        return [l1, l2, l3, l4]
    
    @staticmethod
    def getSampleOutputFileName(path):
        output = path.replace('_L001', '')
        return output

    def run(self):
        allfiles = MergeFastq.getSampleNameList(self.fastqFolder)
        for path in allfiles:
            sampleFiles = MergeFastq.getSampleFileList(path)
            outputFile = MergeFastq.getSampleOutputFileName(path)
            SubProcessUtils.mergeFiles(sampleFiles, outputFile)
            print('File merged at ' + outputFile)
        print(str(len(allfiles)) + ' Files Processed')
        
def argumentsOK():
    numberOfArguments = len(sys.argv)
    if (numberOfArguments != 2):
        print('mergefastq.py requires 1 argument as follow:')
        print('python3 mergeban.py <fastq_files_folder>')
        print('examples:')
        print('python3 mergefastq.py /tmp/exomes/fastq_files/')
        return False
    if not Utils.folderExists(sys.argv[1]):
        print('Error: Folder does not exist')
        return False
    return True

def main():
    print('Initializing mergefastq.py as a program')
    if argumentsOK():
        path = sys.argv[1]
        print('Processing fastq files in folder ' + path)
        merge = MergeFastq(path)
        merge.run()

if __name__ == '__main__':
    main()