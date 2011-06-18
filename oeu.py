#!/usr/bin/python
# -*- coding: utf-8 -*-
# Please read Licence file before going further 
"""
\\begin{abstract}
Welcome to the Open Electronic Ballot Box Project (OEU or \OE)!
This is a citizen initiative to provide to everyone all tools to organize very secure votes using the anyone computer ressources.
Open means that all tools and data are opensource but also that the system is fully distributed and replicated. There is no need of some autority that would keep more secret or more power than the basic citizen. The security model is based on state of the art cryptography research results but also on the principle that Internet is large enought to maintain billion of copies of non infected software. Just try to imagine how hard would be for some hacking organization to infect at the same time all the opensource compilers, (GCC for instance) in the world to make the operation '1+1' returning '3' on one very specific source code and at the same time keep result equal 2 for all other source code in the world!.
You might think that only high skill math and software research people can understand all this. Well we will try to keep as much simple as possible, using many tutorials, examples, faq, tests. It is amazing how you can find today on the Net very well written RSA Tutorials. We would like to reach the same result with only the e-vote problem in mind. The main goal is that a 18 years old (age allowing vote for citizens in many countries) everage educated person could understand every details, after spending a minimum time study on it. We even think that teaching all the e-voting scheme could be integrated in the general education process. This can be support for Math, Computer Science and Democratic studies. 
\\end{abstract}

Hello world!
\\section{The three \\OE{} Roles}
Every one can have one or several roles, as Designer, Manager or Citizen. There is no rules and no constraint to candidate for these roles. It is only a matter of interest and skills. Nobody (individual or organization) shall discourage anyone to play these roles. 
\\begin{enumerate}
\\item{Designer}
A designer is a person like me who design, improve, translate, fix the program given here (the same software generate the text you are currently reading). His name is listed in the text header. He or She me follow simple rules (Licence propagation, digest publishing,...)
\\item{Manager}
A Manager is a person or a group of persons (organization) that initiates a vote. The Manager does not modify the program. Usually, he is using the program of a designer who is not himself. A manager is in charge of initiating a vote, sending a unique signed ID to each citizen he would like to participate to a vote, let those citizen add their public key to the ring, revoque some IDs after a conflict and time stamp the urn to close the registration phase. He also close the vote by adding a final signed time stamp.
\\item{Citizen}
A citizen is an individual (can be a group if it make sense to give one ballot for a groupe) having generated locally a couple of public key, private key. He or she can register to a vote organized by a manager using the urn of a designer. A citizen willing to vote had to sign the unique id given by the manager. When the time stanp is set by the manager, he can vote.
The voting task is technically adding a Linkable Ring Signature to his choice message.
Any citizen can run validity checking tools on the urn, get voting results (temporary since not every registered citizen has not voted). Because the program and the data are all full text, every one, in particular citizer are invited to check validity and count with any external tools or even manually.  
Registered Citizen receved an e-mail from the namager before closing the vote 
\\end{enumerate}

\\section{Crypto animals for \\OE{} !}
\\begin{enumerate}

\\item{Digest}

\\item{Signature}

\\item{Time Stamp}

\\end{enumerate}

\\section{FAQ}
\\begin{enumerate}

\\item How do insure that the text I am reading is the right one ?

\\item What happen If someone change the content of this text ?

\\item How do you preserve anonymous vote ?

\\item Putting several ballot in the url is really not possible ?

\\item If someone thiev my registration id, what can I do ?

\\item If some smart guy crack the algorithm ?

\\item How do you merge ballot boxes ?

\\item Why do you put every thing in text files?

\\item Your system is very old fashon, we have now nive graphical interfaces ?

\\end{enumerate}

\\section{The little story}
I started the project because I wanted to vote the preliminary election of the green party in France (EELV June 2011). 
This election was contucted on Internet by a private company (DEXUUUUUU).
I found the process not secure at all. 
blabla...
"""
##### Source Code #####
__author__='Laurent Fournier'
__version__='0.1'
__state__='alpha'

import os,sys,base64,hashlib,copy
from subprocess import Popen, PIPE

# check srp and pycripto modules are installed !

def document(digest):
    """ Generate LaTeX document """
    o = '\\documentclass{article}\n'
    o += '\\usepackage[margin=2cm]{geometry}\n'
    o += '\\usepackage{url}\n'
    o += '\\begin{document}\n'
    o += '\\title{\OE{}: The Open Electronic Ballot Box}\n\\author{%s}\\maketitle\n'%__author__
    o += 'Version: \\emph{%s} State: \\emph{%s} '%(__version__,__state__)
    o += '[SHA1 digest\\footnote{You have to check first that this digest is the same given by running an external utility like \\emph{sha1sum} on the text source file and second, that this digest is the one given on the author Web page on Internet \\url{https://github.com/oeu}.}: %s]\n'%digest
    o += '\\copyright %s | Licence: GPLv3'%__author__
    o += __doc__
    fl,fb = 'oeu_list.txt','oeu_box.txt'
    if os.path.isfile(fl):
        o += '\\begin{verbatim}\n'
        o += 'voters\n'
        o += '\\end{verbatim}\n'
    else:
        lst = open(fl,'w')
        lst.write('# Voting Public keys')
        lst.close()    
        pass # insert in doc

        pass # insert in doc

    if os.path.isfile(fb):
        o += '\\begin{verbatim}\n'
        o += 'ballots\n'
        o += '\\end{verbatim}\n'
    else:
        bal = open(fb,'w')
        bal.write('# Ballots')
        bal.close()    
    return o + '\\end{document}'

def check():
    """ """
    pass

def merge():
    """ merge two boxes if they are relalive to the same list"""
    pass

if __name__ == '__main__':
    """ main """
    digest = hashlib.sha1(open(__file__).read()).hexdigest()
    tex = open('oeu.tex','w')
    tex.write(document(digest))
    tex.close()    
    # if LATEX installed !
    #pdfile = '%s.pdf'%dfile
    #Popen(('cd /tmp; pdflatex %s;mv %s %s'%(dfile,pdfile,target)), shell=True).communicate()
    #out,err = Popen(('git', 'log','--pretty=oneline','-1'), env=e,stdout=PIPE).communicate()
    #h,r = '#%s\n'%hashlib.sha1(open(__file__).read()).hexdigest(),False
    
    with open(__file__) as f:
        l = list(f)
        if '#%s\n'%hashlib.sha1('%s'%l[:-1]).hexdigest() != l[-1]:
            open(__file__,'a').write('#%s\n'%hashlib.sha1('%s'%l).hexdigest())

    print 'OK!'

# SHA1
#c4d7657722acc86931acfdf7a6dd05d2233cfba8
#98c118653e5cfbeb0b93ca5dd18ecce5adf9b559
