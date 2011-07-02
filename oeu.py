#!/usr/bin/python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
#  © Copyright 2011 Laurent Fournier 
#    This file is part of OE project.
#
#    Formose is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Formose is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with OE file.  If not, see <http://www.gnu.org/licenses/>.
#-----------------------------------------------------------------------------

#LaTeX documentation
"""
\\begin{abstract}
Welcome to the Open Electronic Ballot Box Project, "OEU" for Open Electronic Urn or \\OE{}!

This is an open citizen initiative, not a research article.
\\OE{} provides to everyone a Free, Open, Simple, Secure and complete tool for organizing remote electronic vote (e-vote).
%\\footnote{Security is a matter of probability, but in the range of existing ballot systems our system expect to reach highest security level} 

This project challenges to require less than 1000 lines of Python\\footnote{This is one of the most used high level Software Development Language, see \\url{http://www.python.org}} code in order to remain easilly analysable\\footnote{To compare with 13000 lines of Jif dedicated language + 8000 lines of Java code for the Civitas project.} by anyone able to vote at an election.

We are addressing the problem of Internet/Remote electronic voting using no hardware specific machine, just basic personnal computer. The security model is based on usage of widely used Open-Source\\footnote{Define Open-Source in one sentence!} Software components.

Using \\OE{} add new features making polls more democratic compliant. It removes need of managing vote offices, and all activities/costs of traditional vote. You can initiate a poll, e-vote on some organization proposed poll and also verify yourself that the all voting process is secure. Require skeels in Math equivalent to the average heighteen year's old young person. 

"Open" means that all tools and data are Open-Source but also that the system is fully distributed and replicated. There is no need of some autority that would keep more secret, more power or more knowledge than the basic citizen. The security model is based on state of the art cryptography research results but also on the principle that Internet is large enought to maintain billion of copies of non infected software instances. Just try to imagine how hard would be for some malicious organization to infect at the same time all the Open-Source compilers, (\\url{http://gcc.gnu.org} for instance) in the world to make the operation '1+1' computing '3' on one very specific source code and at the same time keep result equal to 2 for all other source code in the world!.

You might think that only high skill math and computer science research people can understand all this. Well we will try to keep as much simple as possible, using tutorials, examples, faq, tests. It is amazing how you can find today on the Net very well written RSA Tutorials. We would like to reach the same result with only the e-vote problem in mind. The main goal is that a 18 years old (age allowing vote for citizens in many countries) everage educated person could understand every details, after spending a minimum time study on it. We even think that teaching all the e-voting scheme could be integrated in the general education process. This can be support for Math, Computer Science and Democratic studies. 
\\end{abstract}

\\section{News}
The \OE{} project start June 22,2011, so we are still in a very early phase and trying to improve all parts of the project (algorithms, coding, documentation, testing...). 

We have a basic process running with a RSA RingSignature\\ref{Rivest1} implementation to insure anonymity of voters.
We sould add the linkable feature to insure vote unicity and make the signature lenght constant (not function of the number of voters as it is currently)
We will investigate some time released scheme in order to reveal voting results only at a defined time, reling on an Internet trusted time stamper.One simple solution would be for a vote manager to generate a key for that and give everyone the private key when the desired time allapse, but what about if the manager does not send the private key?. 

Another issue is the box merging process. We plan to use a distributed hash table and write a P2P client to update boxes. This also has to be secure and anonymous. Unlike files pointed by Torrents, \\OE{} boxes are growing when people register and votes, so we have to limit their size.


\\section{Hello World!}
These two words 'Hello World!' is well known from software developpers. When learning a new computer language, everyone try to pass the simple test of printing these two words. This is to make you aware that you are reading the result of a computer transformation, not directly inserted data.  During this transformation, many other verifications, generation occurs using for instance a Python interpreter, a \\LaTeX\\cite{lamport94} compiler and a PDF formatter. The source code, the 'oeu.py' file is used to generate the documentation, let you organize a vote, register for an election, insert your ballot, merge ballot box, install the tool in a Web server, verify the results and many other things like improving the all system. 

\\section{The three \\OE{} Roles}
Every one can have one or several roles, as Designer, Manager or Citizen. There is no rules and no constraint to candidate for these roles. It is only a matter of interest and skills. Nobody (individual or organization) shall discourage anyone to play these roles if he is interrested in. 
\\begin{description}
\\item[Designer]
A designer is a person like me who design, improve, translate, fix the program given here (the same software generate the text you are currently reading). His name is listed in the text header. He or She follow simple rules (License propagation, digest publishing,...)
\\item[Manager]
A Manager is a person or a group of persons (organization) that initiates a vote. The Manager does not modify the program. Usually, he is using the program of a designer who is not himself. A manager is in charge of initiating a vote, sending a unique signed ID to each citizen he would like to participate to a vote, let those citizen add their public key to the ring, revoque some IDs after a conflict and time stamp the urn to close the registration phase. He also close the vote by adding a final signed time stamp.
\\item[Citizen]
A citizen is an individual (can be a group if it make sense to give one ballot for a group) having generated locally a couple of public key, private key. He or she can register to a vote organized by a manager using the urn of a designer. A citizen willing to vote had to sign the unique id given by the manager. When the time stanp is set by the manager, he can vote.
The voting task is technically adding a Linkable Ring Signature to his choice message.
Any citizen can run validity checking tools on the urn, get voting results (temporary since not every registered citizen has not voted). Because the program and the data are all full text, every one, in particular citizer are invited to check validity and count with any external tools or even manually.  
Registered Citizen receved an e-mail from the namager before closing the vote 
\\end{description}

\\section{Crypto animals for \\OE{} !}
\\begin{itemize}

\\item{Digest}
A digest is a small string representing a usually large file. This is used to index files in large databases but also for a human beeing to remember or find a particular file. All files copies have the same digest. A very used feature is that have a small modification on a file (changing just on bit) will produce a completly different digest...easy for visual detection. More than one file have the same digest, but it is very hard from for example a spreadsheet file with some amount to change that value and add hidden content so that the digest would be the same than the original file. The solution, if found gives you a huge file size. On a text file (no hidden content) is even harder.   

\\item{Alice, Bob and Gustave}
Here the three most famous guys in Crypto World. Usually, Alice and Bob are nice guys, they will play roles of ellection manager or regular citizen in our e-vote scheme. Gustave is here malicius and will be anything to crack \\OE. 

\\item{Signature}
...
\\item{RSA}
...
\\item{Short Linkable Ring Signature}
...
\\item{Time Stamp}
...
\\end{itemize}

\\section{The process}
\\OE{} tool is always improving but for using it, we must work on the same revision.
So the first thing to do is to select the \\OE, usually the last one and hoppely the more secure.
For a large election, the digest of \\OE{} has to be published on many place, and of course on the official web site of the organizer. This period of time has to be long enought to be sure that every one plan to use the same revision of \\OE, can download it. The list (list.txt file) include an election identification, also published by the manager of the vote.

The manager has already or build a list of all participants of the vote, but this list is outside \\OE{} because it contents private informations; the full name, date of birth, address, phone nombers, e-mail, social security number....anything that can identify with high probability the participants. Means use for such list depend on the criticity of the vote and we can immagine that for non critical elections, a simple e-mail may be requested. Note that the security level of this task is the same for a traditional vote or for preparing an e-vote.     

The manager then generate unique ids for each participants. It is better to generate a small hashed id instead of positive integers, because a malicious participant would have more difficulties to guess valid ids. Also manager is invited to use a secure canal for sending these ids. The security s not impacted, just the number of revocated ids to manage before closing the list.

Each participant is invited to generate locally two keys RSA 2048 keys. Disconect the computer from the internet to be sure that nobody see what you are doing. Keep secret the private key (protected with at least with a pass phrase) and send the public key and and the signed id to the manager. 

There is multiple way to keep secure the private key, with strong authentification. Each citizen should be concerned with this constrainst. If you loose your private key, no one can help you to recover it. It is then better to generate another one and register again to the vote after requesting a revocation of the old public key to the manager. If the vote has started (registration closed), you cannot vote if you don't have private key copy ! If someone thief your private key and the passphrase you have written on a paper (don't do that), and has access to all authentifications devices you used during key generation, then he/she can vote at your place. More exactly, if you vote and the thief also vote, the result depend if its or not on the same box (before or after merging). Voting twice on the same box is simply rejected the second ballot, but if you use another box to vote (referencing the same election), then both votes are saved, but during the merging operation of the boxes, linked signature will raise a flag. If your two or several votes are for the same candidate, your ballot is saved, but any difference in candidate selection will produce an null ballot (do not confuse with white ballot, that is more a supplementary option in the selection list, if the election manager allows it).

After receiving all public ids, merging lists, the manager close the registration phase by signing a time stamped message on the list. 

All revocated ids (and public keys) are removed from the list.
Then the list is fixed with the closure date. If anyone propose to new public id list to the manager, the former cannot use it and even if a sign it, only the first time stamping signature is valid. Time confidence depend on the selected time stamping organization on the Net. For critical vote, selected an old and secure time stamper is requested.  
When the list is closed and published on the Net, it is easy for every one to check that he/she bellons to that list. There is not your full name, but just your public id. Save your public key secret if you don't whant anybody except the manager to know that you are participating to this vote. This is a poor anonymity that you cannot achieve with classical vote...every body in the vote office can see you.

Let the fun start!
Citizen can vote just after receiving the closed public id list. Empty ballot box referencing the list can be fill in. 
The header of the list reference all candidates for the election, with some id (small number). This id is well visible on the ballot box after people vote. It is even easy to count temporary ballot results for each box. That is why we suggest to send the box file directly to some merging server. From this server you can dowload to latest merged box with all the ballots  mixed with yours. To some extend the merging server could find your ip address and correlate with your identity if it has access to an ip geographical adress dictionnary. It also has to have the box file just before you vote to compare them and found for who you votes. To protect from you from this, you can use any other computer not at your home, you can use dynamic ip adresses or anonymous ip adress. Also it is recommended to add several votes (several individuals) on the same box before sending to the merge server. If you don't mind having the risk to show your vote to your related or small group, then share the same box. Again, if the box file on a computer if not sniffed (you can install a fresh linux install from scratch and share it with a group you trust), then the vote order is not revealed. When voting \\OE{} insert the current vote at a random position. If you use an empty ballot box and send it to an individual, not a merging server, you cannot hide to him for who you vote. We can imagine that some people would prefer to go to some vote office providing computer ressources. There is less insurance that these computers are observers safe than that for your computer. The issue here is maintaining anonymity, but at large scale anonymous ballot are very probable. 

The result of the vote is not changed by the type of strategy (merging a lot of small boxes or less big boxes).
Note that with traditional vote, the same problem occurs, because on some very small vote office, knowing the results gives some assumption of who votes for who, people knowing each other. With a difference is that the citizen can chose to participate to a small or a large group with e-vote when he/she is forced to move to a designated vote office in traditional vote. 

Last task, the manager shall stop the vote because we cannot wait infinite time that all resgistered people vote. The voting closure date has to be published on the Web. When this date occurs, the manager sign a time stamp of the last ballot box. 

Imagine that some citizen claims to have voted before the closing date and he/she send too late the ballot box to a merge server or to the manager. Then this citizen has to add a time stamp on the ballot box. This time time is the proof that vote occurs before the closing date. What about if the citizen vote, time stamps, but do not share his ballot with other ?
We can define a new delay, but informal. The manager will accept to merge boxes with time stamp before its own time stamp.
This case should be very improbable because each citizen is invited to check its vote on a web server.
The manager can also wait a small delay between the official closure date and its time stamping in order to include communication delays (few minutes to upload a file).

\\section{FAQ}
\\begin{description}

\\item[How do insure that the text I am reading is the right one ?]
This is simple, if your reading the text source file (oeu.py). Find a computer with Python interpreter, Run the script, it should not complain if this is an original. Use a \\LaTeX suite ('pdflatex' utility) on 'oeu.tex' generated file to build a PDF formated document. 
If you are reading a Postscript, PDF or HTML file, you do have a full insurance that this is the right document. We strongly recommend you to download to source file.
In both cases, to check the document origin and version, just check that the digest (in header PDF document or in last line of text file) is the one given on the WWW \\url{https://github.com/oeu/OpenElectronicUrn}).

\\item[What happen If someone change the content of this text ?]
Well the modified file has a different digest, so any list or ballots referencing this digest will be invalid.
However, anyone can define his all \\OE{} like file and claims to have the original. This may raise copyright issues.
I invite you to check that the file digest is the one find here: \\url{https://github.com/oeu/OpenElectronicUrn}. In that case, the PDF document is there: \\url{https://github.com/oeu/OpenElectronicUrn/oeu.pdf?format=raw}.

\\item[How do you preserve anonymous vote ?]
This is the kernel of the system. linkable ring signature allows any member of a group of public keys to sign a message (here, the message contains the selection of the candidat) without saying anythin on her identity. Even on worse case any juge cannot prove that such a given signature comes from that individual. Everyone knows and can check that this is a member of the group who signed it. The linkable feature is some information that prove that the same individual signed two messages, still anonymouslly. This feature is used to refuse several vote of the same person. 

\\item[Putting several ballot in the ballot box is really not possible ?]
No, linkable ring signatures have a tag that is always the same if signed by the same individual. However, knowing the tag does not reveal the identity of the signer. One of the basic check on the ballot box is to find signatures with the same tags and qualify the signer public signature as invalid (for the current ballot).  

\\item[Someone pick up my registration id, what can I do ?]
A rule is that every participants to a vote has to sign the id.
If you did not received your id, contact the vote manager so see what is wrong, he will give you the same id again.
If you received your id, but you think that someone else had rip it off. Try to sign first and your safe.
If you try to sign after the thief, the urn will refuse registration. Contact the manager, prove your identity and then he will revocate your last id and give you a new one. A revocated id cannot participate to the vote.

\\item[If some smart guy cracks the algorithm ?]
I am sure he or she will join us to fix the failure or improve the security of the system and will be qualified as the top designer. Until organization gives rewards, we will give him or her credit for nice contribution to democracy progress.

\\item[How do you merge ballot boxes?]
This is explained in details somewehere else, but the idea is to merge only compatibles ballot boxes (referencing the same list, that reference the same oeu.py file) and to remove the identical parts.

\\item[Can you merge vote list?]
With some constrainsts. During registration, list of public keys can be merged, but when the vote start, the list of public keys shall be fixed. Such list (digest) is referenced by the ballot box. 

\\item[Why do you put every thing in text files?]
Because text file can be read with many and any text editor and it would be impossible for any cracker to infect all text editors on the planet at the same time without being discovered. Of course text files are not very compact, but it is not a big issue for voting. You can compress the text file (zip, tgz, bz2,...) before sending it on networks. 
Text files can be used for building documents (LaTex suite), write source code and store data...all we need for e-vote.

\\item[Why Python code?]
It could have been any other language, but this one is used worldwide (impact on security), compact (text file size), modern (buildin high level idioms), easy to learn (very important for the project philosophy) and has nice libraries. In particular, the \\emph{pycrypto} module provides tools for cryptographic algorithm.

\\item[Your system is very old fashon, we have now nice graphical interfaces?]
Your are right, but we do not want to sacrify the security in making beautiful user interfaces. Graphical rendering is not requested for the moment (We did not currectly investigate the problem of showing candidate face pictures instead of their names or ids ...shall democratic countries assume that voters can read ?).

\\item What about hitorical/economical/social/phicological studies of e-vote ?
We are reading carefully these studies and we welcome all suggestions and contribution in the group.

\\item[When a translation in other local languages ?]
Our first goal is to mature one version in english to collaborate with the maximum of developpers, crypto experts and anybody having ideas on e-vote. Also \\OE{} shall pass first release tests. One time will come that translation will be requested and we hope to find many free contributions arround. I can do it for French if been helped for my English! .

\\item[Can I run tests set ?]
This is done automatically each time you run \\OE{}. We may include an option to bypass all tests if they take too much time.
\\item[Is there White ballot ?]
This depends of what decided the manager of the election. White ballot is just another option indicating that voter wants to select none of previous options. If you organize an ellection, do not forget to add this option.

\\end{description}

\\section{The little story}
I started the project the day I register for voting one the preliminary election of the green party in France (EELV June 2011). This election was managed on Internet by a private company (Extelia). Opacity of the process and poor security level makes me furious, knowing that the company claims for very high security and certification level. 
I also found on Internet citizen associations against e-vote. I share their worries for the present (2011) but not for the future. I also found very interresting papers on 'group/ring signature' and how anonymity can be achieved. This is not my research field, so I have hard time to understand the details. I would be interrested by learning from the experts of the domain.
It seems that starting 2008, some serious papers describe realistic e-vote schemas, but I did not found any implementations on the Net. I decided to start this project hopping to build a simple but operational implementation of e-vote. 

I am targetting an e-vote for French presidentiel election of 2017. That let us time to test implement, document, test, teach and communicate about the \\OE{} project. My son Tom will exactly be 18 years old in 2017 and he will be allowed to vote maybe the first time using a Secure Electronic Scheme.

%\\glossary{}

\\begin{thebibliography}{99}
\\bibitem{lamport94}\nLeslie Lamport\n\\emph{\\LaTeX: A Document Preparation System}.\nAddison Wesley, Massachusetts,\n2nd Edition,\n1994.
\\bibitem{Rivest01}\nRonald L. Rivest and Adi Shamir and Yael Tauman, \\emph{How to leak a secret}, In ASIACRYPT 2001, pages 554--567, Springer-Verlag,2001

\\end{thebibliography}
"""
##### Source Code #####
__author__='Laurent Fournier'
__version__='0.1'
__state__='alpha'

import os,sys,re,base64,hashlib,copy,getopt,shutil
import time,datetime,random
from subprocess import Popen, PIPE

try:
    import Crypto.PublicKey.RSA
except:
    print '...python pycrypto module not installed !'

def make_readme(digest):
    """
    Welcome to the OEU project, do not hesitate to share your viewpoint and contribute if you wish.\n
    
    This is a 'just one file' project; the full documentation and the source code are a unique Python file; 'oeu.py'.
    This file includes all you need to understand and play with the project.\n

    To have formated documentation, run the 'oeu.py' file to build 'oeu.tex' (LaTeX) file, compile and print it.\n
    For your convenience, the 'oeu.pdf' PDF file is commited.\n\nEnjoy!
    """
    o = 'Head digest is: %s\n\n'%digest
    print '...build readme file for GitHub'   
    txt = open('README.md','w')
    txt.write(o + make_readme.__doc__)
    txt.close()

def make_apache(digest):
    """
    \nWSGIScriptAlias /oeu /home/laurent/OpenElectronicUrn/oeu.py
    """ 
    print '...build oeu.conf file for Apache' 
    txt = open('oeu.conf','w')
    txt.write('#Apache configuration file for wsgi\n#%s'%digest + make_apache.__doc__)
    txt.close()

def make_pdf(fbox,digest,results):
    """ Generate LaTeX document """
    o = '%%This file is generated by running \'oeu.py\' file (digest:%s)\n%% Do not edit by hands !\n\n'%digest
    o += '\\documentclass{article}\n'
    o += '\\usepackage[margin=2cm]{geometry}\n'
    o += '\\usepackage[utf8]{inputenc}'
    o += '\\usepackage{url}\n'
    o += '\\usepackage{fancyhdr,lastpage}\n'
    o += '\\pagestyle{fancy}\n'
    o += '\\fancyhf{}\n'
    o += '\\rfoot{\\scriptsize{Page \\thepage\\ of \\pageref{LastPage}}}\n'

    o += '\\begin{document}\n'
    o += '\\title{\OE{}: The Open Electronic Ballot Box}\n'
    o += '\\author{%s \\url{openurn@gmail.com}}\n'%__author__
    o += '\\maketitle\n\n'
    o += 'Version: \\emph{%s} State: \\emph{%s} '%(__version__,__state__)
    o += '[SHA1 digest\\footnote{Please first check that this digest is the same given by running an external utility like \\emph{sha1sum} on the text \emph{oeu.py} source file and second, that this digest is the one given on the project Web page on Internet \\url{https://github.com/oeu/OpenElectronicUrn}.}: %s]\n\n'%digest
    o += 'License: GPLv3 | \\copyright %s'%__author__
    o += __doc__

    o += '\\section{The Python Code}\n'
    o += '\\subsection{The Ring Signature}\n'
    o += 'The \\emph{ring} Python class provides both anonymous and regular RSA signature.'
    o += '\\small\n\\begin{verbatim}\n'
    d = False
    for l in open(__file__).readlines():
        if re.match(r'.*end class ring',l): d = False
        elif re.match(r'class ring',l): d = True
        if d: o+= l
    o += '\\end{verbatim}\\normalsize\n'
    
    o += '\\subsection{The Main script}\n'
    
    o += '\\small\n\\begin{verbatim}\n'
    d = False
    for l in open(__file__).readlines():
        if re.match(r'if __name__',l): d = False
        elif re.match(r'def run()',l): d = True
        if d: o+= l
    o += '\\end{verbatim}\\normalsize\n'

    o += '\\section{The Data}\n'
    o += 'See generated \emph{box.txt} file.\\\\\n'
    o += 'Lines starting with \\emph{\\%} character are header defining the election; name, id and candidate list\\\\\n' 
    o += 'Lines starting with \\emph{@} character are manager public key and signature\\\\\n'
    o += 'Lines starting with \\emph{\\#} character are voters public key and signature of their id\\\\\n'
    o += 'Lines starting with \\emph{\\textless digit\\textgreater} sequence of characters are ballots; selection and anonymous signature os the selection\n'
    o+= '\\tiny\n\\begin{verbatim}\n'
    if os.path.isfile(fbox):
        bal = open(fbox)
        for l in bal.readlines():
            o += l[:180]+'...\n' if len(l) > 180 else l
    bal.close()    
    o += '\\end{verbatim}\\normalsize\n'
    o += '\\section{Results}\n\\begin{verbatim}\n'
    o += '%s'%results
    o += '\\end{verbatim}\n'
    o += '\\emph{The end of the document}\n\\end{document}'
    digest = hashlib.sha1(open(__file__).read()).hexdigest()
    print '...build oeu.tex'
    tex = open('oeu.tex','w')
    tex.write(o)
    tex.close()    
    print '...build oeu.pdf'
    Popen(('cd /tmp; pdflatex -interaction=batchmode %s 2>/dev/null'%os.path.abspath('oeu.tex')), shell=True).communicate()
    shutil.move('/tmp/oeu.pdf','oeu.pdf')

def merge():
    """ TODO merge two boxes if they are relalive to the same list"""
    pass

def gen_keys(name):
    """ generate PEM format keys """
    d = 'keys'
    if not os.path.isdir(d):
        os.mkdir(d)
    if not os.path.isfile('%s/%s.pem'%(d,name)):
        kf = open('%s/%s.pem'%(d,name),'w')
        kf.write(Crypto.PublicKey.RSA.generate(1024,os.urandom).exportKey('PEM')) 
        kf.close()  

def gen_mail(players,election,manager):
    o,oi,n = '','',0
    voteID = h2b64(hashlib.sha1(election).hexdigest()[:10])
    d = 'mail'
    if not os.path.isdir(d):
        os.mkdir(d)
    for name in players.keys():
        n += 1
        y = random.randint(0,0x100000)
        theid = h2b64(hashlib.sha1('%d'%y).hexdigest())[:10]
        oi += '%05d %s %s\n'%(n,theid,name)
        o = '%This letter is generated by OE\n%Do not edit by hands!\n'
        o += '\\documentclass{letter}\n\\signature{The manager}\n'
        o += '\\address{%s\\\\%s \\\\ City \\\\ Country}\n'%(name,players[name])
        o += '\\usepackage[margin=2cm]{geometry}\n'
        o += '\\usepackage[utf8]{inputenc}'
        o += '\\usepackage{url}\n'
        o += '\\begin{document}\n'
        o += '\\begin{letter}'
        o += '{Election ID: %s\\\\ Manager: %s \\\\ Web Site:\\url{http:\\....} \\\\France}\n'%(voteID,manager)
        o += '\\opening{Dear %s:}\n'%name
        o += 'Please Find bellow your personnal ID code for registering to \\emph{%s} elections\n\n'%election
        o += '\\begin{verbatim}\n\n\t\t         %s\n\n\n\\end{verbatim}\n'%theid
        o += 'Keep it secret until you registered for this election.\n\n'
        o += 'You should have received this letter in a well sealed envelope.\n'
        o += '\\OE{} team strongly recommand to manager to send this by regular mail, not e-mail because your main living address is for us a good proof of your identity.\n'
        o += 'If by chance, you should not but you received several letters like this, so several ID, for the same election. This means that the manger knows you with different identities. This is an error of the manager, not the \\OE{} team. The manager should take all means, including geographical investigation, meeting you physically, to insure unicity of your identity on its list. He/she will be gracefull from you to know that error and fix it.\n\n'
        o += 'If someone else than you has opened the envelope, or just seen and copy your personnal ID,\n'
        o += 'please contact the election manager for requesting another personnal ID. He will recovate this one.\n\n'
        o += 'If you are not willing to vote for this election, you should destroy this letter\n'
        o += 'Just be aware that anyone getting access to your ID can register in your place,\n'
        o += 'and will be able to vote for you if you are not contacting the manager to revocate the ID.\n\n\n'
        o += '\\closing{Enjoy \\OE{},}\n'
        o += '\\ps{P.S. Contact \\OE{} project team for any security related question.}\n'
        o += '\\encl{A copy of \\OE{} full document, can also be downloaded at: \\\\ \\url{https://github/oeu/OpenElectronicUrn/blob/master/oeu.pdf?raw=true}}\n'
        o += '\\end{letter}\n'
        o += '\\end{document}\n'
        maill = open('mail/%s.tex'%name,'w')
        maill.write(o) 
        maill.close()  
        Popen(('cd /tmp; pdflatex -interaction=batchmode %s'%os.path.abspath('mail/%s.tex'%name)), shell=True).communicate()
        shutil.move('/tmp/%s.pdf'%name,'mail/%s.pdf'%name) 
    tex = open('id.txt','w')
    tex.write(oi + '# Manager should keep secret this list !\n')
    tex.write(oi + '# end\n')
    tex.close()   

def create_box(boxf,manager,poll,candidates):
    """ """
    voteID = h2b64(hashlib.sha1(poll).hexdigest()[:10])
    ManagerKey = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%manager).read())
    box = open(boxf,'w') 
    digest,n = hashlib.sha1(open('oeu.py').read()).hexdigest(),0
    header = '%% OE Version:0.1 Digest:%s Election:%s ID:%s\n'%(digest,poll,voteID)
    n = 0
    for x in candidates:
        n += 1
        header += '%% <%s>%s\n'%(n,x)
    box.write(header)
    box.write('@ %s %s\n'%(itob64(ManagerKey.publickey().n),ring([ManagerKey]).sign0(header)))
    box.close()

def register(boxf,I):
    """ """
    ManagerPubKey = None
    myK = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%I).read())
    for l in open(boxf).readlines():
        m = re.match(r'@\s([\w\-]+)\s([\w\-:]+)$',l)
        if m:
            ManagerPubKey = myKey(b64toi(m.group(1)))
            # check header signature
    if ManagerPubKey:
        for l in open('mail/%s.tex'%I).readlines():
            m = re.match(r'\s+(\S+)$',l)
            if m:
                a = ring([myK])
                box = open(boxf,'a')
                box.write('# %s %s\n'%(itob64(myK.publickey().n), a.sign0(m.group(1))))
                box.close()   

def validate_registration(boxf,I):
    """ """
    ManagerKey = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%I).read())
    lid,revocable,seen = {},{},{}
    for l in open('id.txt').readlines():
        m = re.match(r'\d+\s(\S+)\s(\S+)$',l)
        if m:   
            lid[m.group(1)] = m.group(2)
    for l in open(boxf).readlines():
        m = re.match(r'#\s([\w\-]+)\s([\w\-:]+)$',l)
        if m: 
            currentK = myKey(b64toi(m.group(1)))
            a,found = ring([currentK]),False
            for item in lid.keys():
                if a.verif0(item,m.group(2)):
                    if seen.has_key(lid[item]):
                        revocable[m.group(1)] = True
                    found,seen[lid[item]] = True,True
            if not found:
                revocable[m.group(1)] = True
    if revocable: # FIX BOX
        for l in open(boxf).readlines():
            print revocable,seen
    shutil.move(boxf,boxf+'~')
    o,p,header = '',None,''
    for l in open(boxf+'~').readlines():
        m = re.match(r'@\s([\w\-]+)\s([\w\-:]+)$',l)
        if m:
            p = m.group(1)
        elif re.match(r'#\s([\w\-]+)\s([\w\-:]+)$',l):
            o += l
        elif re.match(r'%',l):
            header += l
    a = ring([ManagerKey])
    box = open(boxf,'w')
    box.write(header)
    box.write('@ %s %s\n'%(p,a.sign0(header+o)))
    box.write(o)
    box.close()

def check_registration(boxf,I,theId):
    o,manS,manK,youarein = '',None,None,False
    for l in open(boxf).readlines():
        m = re.match('@\s([\w\-]+)\s([\w\-:]+)$',l)
        if m:
            manK = myKey(b64toi(m.group(1)))
            manS = m.group(2)
        else:
            o += l
    assert manK and manS and ring([manK]).verif0(o,manS)
    # find her entry
    aKey = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%I).read())
    for l in open(boxf).readlines():
        m = re.match(r'#\s(%s)\s([\w\-:]+)$'%itob64(aKey.publickey().n),l)
        if m:
            if ring([aKey]).verif0(theId,m.group(2)): 
                youarein = True
    return youarein

def close_box(boxf,I):
    """ """
    box = open(boxf,'a')
    ManagerKey = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%I).read())
    a = ring([ManagerKey])
    dat = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
    box.write('%s %s\n'%(dat,a.sign0(dat)))
    box.close()

def vote(boxf,I,choice):
    """ I select choice (number) in box """
    aKey = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%I).read())
    myring,i = [],0
    for l in open(boxf).readlines():
        m = re.match(r'#\s([\w\-]+)\s([\w\-:]+)$',l)
        if m:
            k = b64toi(m.group(1))
            if k == aKey.publickey().n:
                myring.append(aKey)
                index = i
            else:
                myring.append(myKey(k))
            i += 1
    box = open(boxf,'a')
    sig = ring(myring).sign('<%d>'%choice,index)
    box.write('%s %s\n'%('<%d>'%choice,sig))
    box.close()
    return hashlib.sha1('<%d>'%choice + sig).hexdigest()

def check_vote(boxf,I,receipt):
    """ need the secret receipt """
    myring,lchoix = [],{}
    for l in open(boxf).readlines():
        m0 = re.match(r'%\s(<\d+>)(.*)$',l)
        if m0:
            lchoix[m0.group(1)] = m0.group(2)
        m1 = re.match(r'#\s([\w\-]+)\s([\w\-:]+)$',l)
        if m1:
            myring.append(myKey(b64toi(m1.group(1))))
    for l in open(boxf).readlines():
        m = re.match(r'(<\d+>)\s(.*)$',l)
        if m:
            if receipt == hashlib.sha1(m.group(1)+m.group(2)).hexdigest():
                if ring(myring).verif(m.group(1),m.group(2)) and lchoix.has_key(m.group(1)):
                    return lchoix[m.group(1)]
    return 'Ballot not found !'


def tally(boxf):
    """ tally box """
    myring,lchoix,t = [],{},{}
    for l in open(boxf).readlines():
        m0 = re.match(r'%\s(<\d+>)(.*)$',l)
        if m0:
            lchoix[m0.group(1)] = m0.group(2)
            t[m0.group(2)] = 0
        m1 = re.match(r'#\s([\w\-]+)\s([\w\-:]+)$',l)
        if m1:
            myring.append(myKey(b64toi(m1.group(1))))
        m = re.match(r'(<\d+>)\s(.*)$',l)
        if m:
            if ring(myring).verif(m.group(1),m.group(2)):
                if lchoix.has_key(m.group(1)) and t.has_key(lchoix[m.group(1)]):
                    t[lchoix[m.group(1)]] += 1
    return t

def get_players(lf):
    """ all players with their ids """
    players = {}
    if os.path.isfile(lf):
        for l in open(lf).readlines():
            m = re.match(r'(\w+)\s+(.*)$',l)
            if m:
                players[m.group(1)] = m.group(2)
    return players

class myKey:
    """ Defines structure for 1024 length RSA key """
    def __init__(self,n,d=None):
        self.n,self.d,self.e = n,d,0x10001L

def itob64(n):
    c = hex(n)[2:-1]
    if len(c)%2:
        c = '0'+c
    x = base64.urlsafe_b64encode(c.decode('hex'))
    return re.sub(r'=*$','',x)

def b64toi(c):
    v = c + '='*((4-len(c)%4)%4)
    x = base64.urlsafe_b64decode(v)
    return int(x.encode('hex'),16)

def h2b64(c):
    if len(c)%2:
        c = '0'+c
    x = base64.urlsafe_b64encode(c.decode('hex'))
    return re.sub(r'=*$','',x)

class ring:
    """ RSA Ring Signature from Rivest, Shamir and Tauman, "how to leak a secret", 2001 
    Usage: r is a ring of RSA public keys, (one is also private for the signer), S is the signature
      a = oeu.ring(r)
      S = a.sign('hello world!',2) # signer is here the second member in the ring
      assert a.verif('hello world!',S)
    """
    def __init__(self,kl):
        """ Set public keys, RSA size """
        self.kl,self.e = kl,1024
            
    def permut(self,msg):
        """ Define permutation list from message """
        x = int(hashlib.sha1(msg).hexdigest(),16)
        self.p,self.p1 = [],[]
        while x > self.e:
            q,r = x//self.e,x%self.e
            self.p.append(r)
            self.p1.insert(0,r)
            x = q
        
    def itob64(self,n):
        """ utility to transform int to base64) """
        c = hex(n)[2:-1]
        if len(c)%2:
            c = '0'+c
        x = base64.urlsafe_b64encode(c.decode('hex'))
        return re.sub(r'=*$','',x)

    def b64toi(self,c):
        """ utility to transform base42 to int) """
        v = c + '='*((4-len(c)%4)%4)
        x = base64.urlsafe_b64decode(v)
        return int(x.encode('hex'),16)

    def E(self,x,w=True):
        """ Permutations of message Ek() and Ek-1() function in the paper"""
        p = self.p if w else self.p1
        for i in range(len(p)-1):
            y = ((x>>p[i])^(x>>p[i+1]))&1
            x = x^((y<<p[i])|(y<<p[i+1]))
        return x

    def trap(self,x,e,n):
        """ Modified RSA trap; g() function in the paper """
        q,r = x//n,x%n
        return q*n + pow(r,e,n) if (q+1)*n <= 2**self.e else x

    def sign(self,msg,s): 
        """
        Find ys such that E(yn....^E(y2^E(y1^E(y0)))) = 0 
        ys = E1(ys+1^...E(yn)) ^ E(ys-1^...E(y1^E(y0)))
        """
        self.permut(msg)
        x,y = [],[]
        for i in range(len(self.kl)):
            if i != s:
                xi = random.randint(0,2**self.e-1)
                x.append(xi)
                y.append(self.trap(xi,self.kl[i].e,self.kl[i].n))
        ya,yb = 0,0
        for yi in y[:s]: ya = self.E(yi^ya)
        for yi in reversed(y[s:]): yb = self.E(yb^yi,False)
        x.insert(s,self.trap(ya^yb,self.kl[s].d,self.kl[s].n))
        return ' '.join('%s'%self.itob64(xi) for xi in x)

    def verif(self,msg,X):
        """ E(yn....^E(y2^E(y1^E(y0)))) =? 0 """
        self.permut(msg)
        x = []
        for xi in X.split(' '): x.append(self.b64toi(xi))
        Y = map(lambda i,j:self.trap(i,j.e,j.n),x,self.kl)
        return reduce (lambda x,y:self.E(x^y),Y,0) == 0

    def sign0(self,msg,s=0):
        """ RSA regular signature"""
        salt = self.itob64(random.randint(0,0xFFFFFL))
        return salt + ':' + self.itob64(pow(int(hashlib.sha1(salt+msg).hexdigest(),16),self.kl[s].d,self.kl[s].n))

    def verif0(self,msg,x,s=0):
        """ RSA verification """
        [salt,sig] = x.split(':') 
        return int(hashlib.sha1(salt+msg).hexdigest(),16) == pow(self.b64toi(sig),self.kl[s].e,self.kl[s].n)

# end class ring:


def my_app(environ,start_response):
    """ for downloading init boxp """
    start_response('200 OK',[])
    return []

class middleware:
    """ Web Application """
    def __init__(self,app):
        self.app = app
        #create_box('/tmp/box.txt','Robert','POLL TEST',['Marcel Dupond','Marie Durand'])

    def __call__(self,environ, start_response):
        environ['mid.oeu'] = 'POLL TEST'
        environ['mid.manager'] = 'Robert'
        def custom_start_response(status, header):
            header.append(('Content-type','application/xhtml+xml'))
            return start_response(status, header)
        response_iter = self.app(environ, custom_start_response)
        o = '<?xml version="1.0" encoding="UTF-8"?>\n'
        o += '<svg xmlns="http://www.w3.org/2000/svg">\n'
        o += '<text x="10" y="20">I am the manager \'%s\'</text>'%environ['mid.manager']
        o += '<text x="10" y="40">My public Key is:</text>'
        o += '<text x="10" y="60">Download init box for %s</text>'%environ['mid.oeu']
        voteID = h2b64(hashlib.sha1(environ['mid.oeu']).hexdigest()[:10])
        o += '<text x="400" y="60">Election Id:%s</text>'%voteID
        a = '</svg>\n'
        response_string = o + ''.join(response_iter) + a 
        return [response_string]

application = middleware(my_app)

def update():
    """ update file digest if changed """
    with open(__file__) as f:
        l = list(f)
        if '#%s\n'%hashlib.sha1('%s'%l[:-1]).hexdigest() != l[-1]:
            open(__file__,'a').write('#%s\n'%hashlib.sha1('%s'%l).hexdigest())
            print '...digest updated'
            fl,fb = 'list.txt','box.txt'
            #if os.path.isfile(fl):
            #    os.remove(fl)
            #if os.path.isfile(fb):
            #    os.remove(fb)                

def gen_test_list(fi):
    """  This is here just for testing, use another tool to output this file 
    on each linne first word is unique name following by the adress 
    """
    if not os.path.isfile(fi):
        tex = open(fi,'w')
        tex.write('Alice   2 Place du Capitole 31000 Toulouse\n')
        tex.write('Bob     24 Rue des Paradoux 31000 Toulouse\n')
        tex.write('Robert  23 Avenue des Champs Elysées 75000 Paris\n')
        tex.write('Carol   17 Place Colbert 69000 Lyon\n')
        tex.write('Oscar   22 Rue Arago 31000 Toulouse\n')
        tex.write('Eve     22 Rue Jean Jaures 31000 Toulouse\n')
        tex.write('Mallory 13 Rue Grognard 69000 Lyon\n')
        tex.write('Trudy   12 Places aux Herbes 38000 Grenoble\n')
        tex.write('Isaac   17 Place du Capitole 31000 Toulouse\n')
        tex.write('Arthur  26 Rue Chappet 69000 Lyon\n')
        tex.write('Merlin  8 Place de la Comédie 33000 Bordeau\n')
        tex.write('Peggy   19 Place de Jaude 63000 Clermont-Ferrand\n')
        tex.close()   

def run():
    """ This is an example of voting scenario """
    bf,lf,manager,election = 'box.txt','list.txt','Robert','POLL TEST'
    gen_test_list(lf)
    players = get_players(lf)
    for name in players.keys():
        gen_keys(name)
    gen_mail(players,election,manager)
    create_box(bf,manager,election,['Marcel Dupond','Marie Durand','Joe Smith','White ballot'])
    for name in players.keys():
        register(bf,name) # individual registration 
    validate_registration(bf,manager) # manager validate registration
    for l in open('id.txt').readlines():
        m = re.match(r'\d+\s(\S+)\s(\S+)$',l)
        if m:   # Every one checks his registration
            assert check_registration(bf,m.group(2),m.group(1))
    close_box(bf,manager) # Manager closes registration phase
    receipt = {}
    for name in players.keys():        
        receipt[name] = vote(bf,name,random.randint(1,4)) # random vote for testing !
    close_box(bf,manager) # Manager closes the poll
    for name in players.keys():
        print '...\'%s\' votes for \'%s\''%(name,check_vote(bf,name,receipt[name])) # Voter checks his vote
    return tally(bf)

if __name__ == '__main__':
    """ This is an example of voting scenari """
    print 'Runing test:\n...wait!'
    # options not yet used
    opts, args = getopt.getopt(sys.argv[1:], 'htdi:', ['help', 'table','diff','id='])
    for r in opts:
        if r[0] in ('-h','--help'):
            help(os.path.basename(sys.argv[0])[:-3])
    update() # comment this line during development
    res = run()
    print '...results: %s'%res # display results
    digest = hashlib.sha1(open(__file__).read()).hexdigest()
    make_pdf('box.txt',digest,res)
    make_readme(digest)
    make_apache(digest)
    print 'OK'

# SHA1

#225f3fcd6ffcfe903b8846d30203bf59a0e87b11
