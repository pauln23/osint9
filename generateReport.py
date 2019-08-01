from yattag import Doc
from config import Config
import breachCompSearch
import passStrengthChecker
import typosquatListChecker

f = open('companyDetails.cfg', 'r')
company = Config(f)

def genReport():
    doc, tag, text = Doc().tagtext()

    with tag('html'):
        with tag('head'):
            doc.asis('<meta charset="utf-8">')
            doc.asis('<link rel="stylesheet" href="css/main.css">')

        with tag('body'):

            ##scripts for particles js
            with tag('div', id="particles-js"):
                pass
            with tag('script', src='js/particles.js'):
                pass
            with tag('script', src='js/app.js'):
                pass

            ##all ontop of particles
            with tag('div', klass = "overlay"):
                with tag("h3", style = 'font-size:500%'):
                    text(company.COMPANY)


                with tag('div', klass="center"):

# TYPOSQUATTING AND IP TABLE----------------------------------------------
                    with tag('table', klass="center cam"):
                        with tag('thead'):
                            with tag('tr', style="padding:70%"):
                                with tag('th', style="font-size:300%"):
                                    text('Hostname/Domain')
                                with tag('th', style="font-size:300%"):
                                    text('IP')
                                with tag('th', style="font-size:300%"):
                                    text('Status')
                                with tag('th', style="font-size:300%"):
                                    text('Abuse Score')
                                with tag('th', style="font-size:300%"):
                                    text('Country')

                        with tag('tbody'):
                            for x in company.TYPOSQUAT_DOMAINS:
                                domain, IP, registered, abuseScore, country = typosquatListChecker.checkRegistered(x)
                                with tag('tr'):
                                    with tag('th'):
                                        text(domain)
                                    with tag('th'):
                                        text(IP)
                                    with tag('th'):
                                        if registered : text('Registered')
                                        if not registered : text('Not Registered')
                                    with tag('th'):
                                        text(abuseScore)
                                    with tag('th'):
                                        text(country)

                            for p in company.IP_LIST:
                                IP, hasHosts, hostname, score, country1 = (typosquatListChecker.checkIP(p))
                                with tag('tr'):
                                    with tag('th'):
                                        if hasHosts:text(str(hostname))
                                        if not hasHosts:text('n/a')
                                    with tag('th'):
                                        text(IP)
                                    with tag('th'):
                                        text('n/a')
                                    with tag('th'):
                                        text(score)
                                    with tag('th'):
                                        text(country1)




                    doc.asis("<br>")


# PASSWORD STRENGTH TABLE----------------------------------------------
                    with tag('table', klass="center cam"):
                        with tag('thead'):
                            with tag('tr', style="padding:70%"):
                                with tag('th', style="font-size:300%"):
                                    text('Password')
                                with tag('th', style="font-size:300%"):
                                    text('Strength')
                                with tag('th', style="font-size:300%"):
                                    text('Improvements')


                            with tag('tr'):
                                with tag('th', style="font-size:200%"):
                                    doc.asis("<br>")

                            with tag('tbody'):
                                for line in company.PASSWORD_LIST:
                                    password, strength, improvements = passStrengthChecker.checkPasswords(line)
                                    with tag('tr'):
                                            with tag('th'):
                                                text(password)
                                            with tag('th'):
                                                text(strength)
                                            with tag('th'):
                                                for x in improvements:
                                                    with tag('u'):
                                                        text(x.capitalize())
                                                    doc.asis("<br>")
                                                    text(str((improvements[x])).capitalize())
                                                    doc.asis("<br>")


                    doc.asis("<br>")
# CREDENTIAL LEAKS TABLE----------------------------------------------
                    with tag('table', klass="center cam"):
                        with tag('thead'):
                            with tag('tr)'):
                                with tag('th', style="font-size:300%"):
                                    text('Credential Leaks')
                                with tag('th', style="font-size:300%"):
                                    text('Source')
                            with tag('tr'):
                                with tag('th', style="font-size:200%"):
                                    text(company.EMAIL_FORMAT)
                            with tag('tr'):
                                with tag('th', style="font-size:200%"):
                                    doc.asis("<br>")

                        with tag('tbody'):
                            for line in open('dunkinBrandsCreds.csv', 'r'):
                                creds, source = breachCompSearch.checkDomainName(line)
                                with tag('tr'):
                                    with tag('th'):
                                        text(creds)
                                    with tag('th'):
                                        text(source)





    return(doc.getvalue())

