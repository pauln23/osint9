##Main Script for OSINT TOOL
from config import Config
import typosquatListChecker
import passStrengthChecker
import generateReport

f = open('companyDetails.cfg', 'r')
company = Config(f)


with open('reportGenerated/reportTest.html', 'w+') as writer:
    writer.write(generateReport.genReport())








