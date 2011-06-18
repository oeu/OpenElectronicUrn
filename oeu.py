#!/usr/bin/python
# -*- coding: utf-8 -*-
# Please read Licence file before going further 
"""
\\begin{abstract}
Welcome to the Open Electronic Ballot Box Project (OEU or \OE)!
This is a citizen initiative to provide to everyone all a simple tool to organize very secure\\footnote{Secirity is a matter of probability, but in the range of existing ballot systems our system maybe reach current highest security level} votes using the anyone computer ressources (No hardware/software dedicated machine). Removing need of voting office.

Open means that all tools and data are opensource but also that the system is fully distributed and replicated. There is no need of some autority that would keep more secret or more power than the basic citizen. The security model is based on state of the art cryptography research results but also on the principle that Internet is large enought to maintain billion of copies of non infected software. Just try to imagine how hard would be for some hacking organization to infect at the same time all the opensource compilers, (GCC for instance) in the world to make the operation '1+1' returning '3' on one very specific source code and at the same time keep result equal 2 for all other source code in the world!.
You might think that only high skill math and software research people can understand all this. Well we will try to keep as much simple as possible, using many tutorials, examples, faq, tests. It is amazing how you can find today on the Net very well written RSA Tutorials. We would like to reach the same result with only the e-vote problem in mind. The main goal is that a 18 years old (age allowing vote for citizens in many countries) everage educated person could understand every details, after spending a minimum time study on it. We even think that teaching all the e-voting scheme could be integrated in the general education process. This can be support for Math, Computer Science and Democratic studies. 
\\end{abstract}

Hello world!
\\section{The three \\OE{} Roles}
Every one can have one or several roles, as Designer, Manager or Citizen. There is no rules and no constraint to candidate for these roles. It is only a matter of interest and skills. Nobody (individual or organization) shall discourage anyone to play these roles if he is interrested in. 
\\begin{enumerate}
\\item{Designer}
A designer is a person like me who design, improve, translate, fix the program given here (the same software generate the text you are currently reading). His name is listed in the text header. He or She me follow simple rules (Licence propagation, digest publishing,...)
\\item{Manager}
A Manager is a person or a group of persons (organization) that initiates a vote. The Manager does not modify the program. Usually, he is using the program of a designer who is not himself. A manager is in charge of initiating a vote, sending a unique signed ID to each citizen he would like to participate to a vote, let those citizen add their public key to the ring, revoque some IDs after a conflict and time stamp the urn to close the registration phase. He also close the vote by adding a final signed time stamp.
\\item{Citizen}
A citizen is an individual (can be a group if it make sense to give one ballot for a group) having generated locally a couple of public key, private key. He or she can register to a vote organized by a manager using the urn of a designer. A citizen willing to vote had to sign the unique id given by the manager. When the time stanp is set by the manager, he can vote.
The voting task is technically adding a Linkable Ring Signature to his choice message.
Any citizen can run validity checking tools on the urn, get voting results (temporary since not every registered citizen has not voted). Because the program and the data are all full text, every one, in particular citizer are invited to check validity and count with any external tools or even manually.  
Registered Citizen receved an e-mail from the namager before closing the vote 
\\end{enumerate}

\\section{Crypto animals for \\OE{} !}
\\begin{itemize}

\\item{Digest}

\\item{Signature}

\\item{Time Stamp}

\\end{itemize}

\\section{FAQ}
\\begin{enumerate}

\\item How do insure that the text I am reading is the right one ?
This is simple, if your reading the text source file (oeu.py). Find a computer with Python interpreter, Run the script, it should not complain if this is an original. Use a LaTeX suite (pdflatex utility) on oeu.tex generated file to build a PDF formated document. 
If you are reading a Postscript, PDF or HTML file, you do have a full insurance that this is the right document. We strongly recommend you to download to source file.
In both cases, to check the document origin and version, just check that the digest (in header PDF document or in last line of text file) is the one given on the WWWW \\url{https://github.com/oeu/OpenElectronicUrn}).

\\item What happen If someone change the content of this text ?
Well the modified file has a different digest, so any list or ballots referencing this digest will be invalid.

\\item How do you preserve anonymous vote ?

\\item Putting several ballot in the ballot box is really not possible ?
No, linkable ring signatures have a tag that is always the same if signed by the same individual. However, knowing the tag does not reveal the identity of the signer. One of the basic check on the ballot box is to find signatures with the same tags and qualify the signer public signature as invalid (for the current ballot).  

\\item If someone thiev my registration id, what can I do ?

\\item If some smart guy crack the algorithm ?
I am sure he or she will join us to fix the failure or improve the security of the system and will be qualified as the top designer. Until organization gives rewards, we will give him or her credit for nice contribution to democracy progress.

\\item How do you merge ballot boxes ?
This is explain in details somewehere else, but the idea is to merge only compatibles ballot boxes (referencing the same list, that reference the same oeu.py file) and to remove the identical parts.

\\item Can you merge vote list ?
With some constrainsts. During registration, list of public keys can be merged, but when the vote start, the list of public keys shall be fixed. Such list (digest) is referenced by the ballot box. 

\\item Why do you put every thing in text files?
Because text file can be read with many and any text editor and it would be impossible for any cracker to infect all text editors on the planet at the same time without being discovered. Of course text files are not very compact, but it is not a big issue for voting. You can compress the text file (zip, tgz, bz2,...) before sending it on networks. 
Text files can be used for building documents (LaTex suite), write source code and store data...all we need for e-vote.

\\item Why Python code ?
It could have been any other language, but this one is used worldwide (impact on security), compact (text file size), modern (buildin high level idioms), easy to learn (very important for the project philosophy) and has nice libraries. In particular, the pycropto module provides tools for cryptographic algorithm.

\\item Your system is very old fashon, we have now nice graphical interfaces ?
Your are right, but we do not want to sacrify the security in making beautiful user interfaces. Graphical rendering is not requested for the moment (We did not currectly investigate the problem of showing candidate face pictures instead of their names or ids ...shall democratic countries assume that voters can read ?).
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

try:
    import pycripto
except:
    pass

def readme(digest):
    """
    The 'oeu.py' file includes all you need to understand and play with the project.\n
    Just run it to build 'oeu.tex' (LaTeX) file, compile and print it.\n
    For your convenience, the 'oeu.pdf' PDF file is commited.\n\nEnjoy!
    """
    o = 'Head digest is: %s\n\n'%digest
    return o + readme.__doc__

def document(digest):
    """ Generate LaTeX document """
    o = '\\documentclass{article}\n'
    o += '\\usepackage[margin=2cm]{geometry}\n'
    o += '\\usepackage{url}\n'
    o += '\\begin{document}\n'
    o += '\\title{\OE{}: The Open Electronic Ballot Box}\n\\author{%s}\\maketitle\n'%__author__
    o += 'Version: \\emph{%s} State: \\emph{%s} '%(__version__,__state__)
    o += '[SHA1 digest\\footnote{You have to check first that this digest is the same given by running an external utility like \\emph{sha1sum} on the text source file and second, that this digest is the one given on the author Web page on Internet \\url{https://github.com/oeu}.}: %s]\n\n'%digest
    o += '\\copyright %s | Licence: GPLv3'%__author__
    o += __doc__
    fl,fb = 'list.txt','box.txt'
    o += '\\begin{verbatim}\n'
    if os.path.isfile(fl):
        o += 'voters\n'
    else:
        lst = open(fl,'w')
        lst.write('# PublicKeys [%s]'%digest)
        lst.close()    
        pass # insert in doc

        pass # insert in doc

    if os.path.isfile(fb):
        o += 'ballots\n'
    else:
        bal = open(fb,'w')
        bal.write('# Ballots [%s]'%digest)
        bal.close()    
    o += '\\end{verbatim}\n'
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
    #h,r = '#%s\n'%hashlib.sha1(open(__file__).read()).hexdigest(),False
    print '...build tex file'

    tex = open('README.md','w')
    tex.write(readme(digest))
    tex.close()    
    print '...build readme file'
    
    with open(__file__) as f:
        l = list(f)
        if '#%s\n'%hashlib.sha1('%s'%l[:-1]).hexdigest() != l[-1]:
            open(__file__,'a').write('#%s\n'%hashlib.sha1('%s'%l).hexdigest())
            print '...digest updated'
    
    print 'OK!'

# SHA1
#f630eb55b920bb0854c07e0e7fdd69ee8fa8fe35
