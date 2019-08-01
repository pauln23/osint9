##The data gathered for DunkinBrands is from RecordedFuture's dataset
##Each dataset could be downloaded individually with adaquate space and time, which would be thousands of gigabytes

def checkDomainName(line):
    try :
        credentialData, source = line.split(',')
    except Exception:
        credentialData, source = '', ''
    return(credentialData, source)
