#!/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#  © Copyright 2011 Citizen-Lambda
#    This file is part of OE project.
#
#    OE is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    OE is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with OE file.  If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------

r"""\twocolumn \renewcommand{\LettrineFontHook}{\color[gray]{0.5}}\\
\lettrine[lines=4]{W}{elcome} to \oeu{}, the Open Electronic vote system. \oeu{} is a citizen initiative to provide to anyone, anonymous citizen or organization, the secure tools for voting remotelly on Internet. \oeu{} is compliant with democracy main principles and even enhance in some way democracies everyday application. \oeu{} is a self containing small source text file that is readable and understandable by anyone with basic eighteen years old\footnote{ the average legitime age for voting in many modern democracies} education skills. \oeu{} is low cost, requiring no dedicated hardware device (e-vote machine, scanner, smartcard\dots) and usage of postmail is minimized for election organizers. \oeu{} is free and open in the more strongest way, that is any future modification shall remains open-source with licence GPLv3. \oeu{} is also a contemporary artwork belonging to any citizen, named Citizen$\Lambda$.\\
The main feature that we are seeking for an i-voting system is its security model and we arguing that \oeu{} is a trustworthy system. As algorithms, code and documentation are all available for any citizen, we are challenging cryptographics, computer science and democracy experts to stress and break the system. However, our main goal is that any citizen can build is own confidence that the system is preserving voting requirements; Any eligible voter can add anonymously only one valid ballot and the tally is fully verifiable from end to end phases of an election race.\oeu{} is also coersion resistant and receipt free so selling or buying a vote is discouraged.\\
\oeu{} uses the Internet but not the Web (\textsc{http(s)} based protocol). It is rather based on a file sharing \pp{} framework. Every voter has on its own computer the last updated copie of a full electronic ballot box. The system is able to manage several ballot boxes for the same election race as for classical vote. Where the number of registered voter for a vote office in classical vote is constraint by the size of the cubic transparent ballot box and time requested to tally votes at the end of the day, the size of the electrononic ballot box can be much more higher (several billions) but can also be splitted in smaller boxes to improve computing verification time and also ensure no one from the election organizer can handling identity listing file (list of names with adresse,social security numbers and other identifcation attributes) of too many citizens. 
At a level of a nation, each citizen is registered at least in the local tax office, social security, school. 
A malicious person may try to be unknown from the administration and simply in that case would loose his right to vote. It is more problematic for voting when a malicious individual tries to have two or more identities because he is potentially able to put several ballots in the same election race. We will see that is it up to the organization managing the election to contact the right office that discorage multiple identity to get eligible voters listing (For instance, a citizen registered with several main adresses in different landscapes or states should be out of the law but by construction should pay really more taxes in that configuration than if it had declared only one main personnal adress, so the price and risk to have multiple identities all his life would be too high for the gain at one election). Because such organization (state,cites,...) are still composed of employees, human fault sensibles, it is a good principle for personnal data, even temporary, recording that such lists not be too long. Results of each ballot box is published on a web site so anyone can check that its local ballot box result is well visible on the Internet and anyone can tally with other ballot boxes results also published. If the organizer invents a virtual city name, with no phisical citizen, the trick would likelly be discovered by curious readers off the web site, more easilly that the results of such city is likely to change the final result and stronglly disagree with other real cities results.\\
We know that computers store viruses, worms\dots and other malware that could change unwittingly the citizen desired ballot choice. How \oeu{} cope with such fact? \\
\oeu{} is first an unalterable text file. A text file cannot embedd non expected executable code. Each character (ascii or unicode) means the same think on all computers arround the world, and words and sentences formed with such characters are valid instruction in the used programming language. If it is written \texttt{a=1+1}, there very very high propability that the machine understand that $a$ labeled memory should store the value $2$.\\
All the source code is visible and any modification in that source (or documentation) would produce a new \emph{digest} code (see bellow what this cryptographic animal is). This code is very small; the tool is exactly @oeulength@ lines of code, so anyone with some available time can read it and test it. The code is written in \pyt{} witch is one of the most popular and simple programming language. Many schools teach \pyt{} because it is simple but has all features of modern languages (Object Orientation, Functionnal programming,...). Syntax clarity and introspection makes \pyt{} nice for approaching literate programming.
 The good news about \pyt{} and software for voting system is that the cpu performance is not the main requirement (\emph{C} language may be faster), but the native support for very long integer arithmetics is great used in cryptography.\\Just consider the basic random calculus\footnote{as $a$,$b$,$c$ are random, you may have different values in two instances of the current documentation from the same source code, same digest.}:
@longcalculus@
To be executable, a \pyt{} programm use onther transformation tool; a \pyt{} interpreter and for generating the \pdf{} documentation, one use a \LaTeX{} suite. Both tools are open-source and runnable on all Operating Systems (MacOSX, Linux,Windows\tm{} ,\dots). A malicious programmer who wants to inject a virus into the \pyt{} interpreter or the \LaTeX{} suite should be a famous commiter; status he get by its high technical skills and its integrity in the OpenSource community that votes for him. He would had to justify the changes in the code source because every change is recorded (traced) in a configuration management system, so none of its peers car found the strange code source portion during the reviewing phases. Furthermore, a virus may be small in machine code size, but usually very big when entered in a high level language. Nowodays, there is no reason to add assembly code to a project code without suspecting a malicious purpose.\\
One can argue that the source code can be clean but the tools can be infected from the outside. Then the security does not come from the Open-Source feature, but more on the scale factor rule. There are billions of instances of \pyt{} interpreters, many of them installed in full Open-Source distributions (for instance Linux Ubuntu) with several levels of privileges and package repositories on Internet are never infected; each package has a checked digest code. Even if it would be possible to infect many versions of a \pyt{} interpreter, it would be very hard because an interpreter is a generic tool running infinite number of different programs, that a \pyt{} sentence like \texttt{myvote='Alice'} in an unpredictable source code would have been interpreted by the infected interpreter as \texttt{myvote='Oscar'} without suspicious behaviour.
Infecting the basic language operators used by cryptographic routines would also be revealed by conflict in the file sharing \pp{} framework because two ballot boxes (one produced with an infected interpreter and the other produced by a clean instance) would raise a conflict immediatly analysed by \pyt{} language authors.\\
Any programmer can build nice graphical desktop application with \pyt{} packages that would display push button for voters, but \oeu{} would rather use none of them to keep the code simple. In fact \oeu{} relies on the Operating system interface and on a basic generic terminal type window. For the action of putting a ballot in a ballot box, we done the following. \oeu{} is a \pyt{} script and is rendered as such in the graphical file system (based on the extension \texttt{.py}). All Operating systems alows to bind to a file a nice icon image, so we use an image of a physical ballot box. Ballots in \oeu{} are very small \pdf{} files (only 530 bytes long!) with written in big letters a candidate name and in very small font the public key of the voter (see bellow what this animal is). In the same directory are present the ballot box (the \pyt{} programm) and eligible ballots for all candidats (\oeu{} has generated them when you launch it the first time). Many graphical file managers render the content of the first page of the \pdf{} files, so even if you do not trust the ballot file name that is also the candidat name, you can double click on the file icon to open the \pdf{} and check its is the right guy, but without opening the file, the icon displays for you the readable (because it use huge font size) name of the candidat. The voting act consist on dragging and dropping the selected candidat (\pdf{} file) onto the ballot box (\pyt{} program). By default, the \pyt{} will interpret the dropper file as an argument, just like if you had typed \texttt{"oeu.py my\_selected\_candidate.pdf"} on a terminal, and you can also do it this way. Because the ballot embbed the voters public key, \oeu{} will request to temporary and automatically access to the coupled private key after asking the voter his \emph{passphrase}...in a terminal.\\
When a ballot is added in a local ballot box, the \pp{} protocol propagate the changes to all nodes. Destroying or altering one node ballot box has no effect since the other nodes will fix it as soon as a verification error occurs.
Voting consist on the crytographic terms in using a \emph{ring signature} (see below that animal). This kind of group signature gives the proof that the voter belongs to a group, the list of public keys of the ballot box, each key representing an legitivate voter, but in the same way insure anonymity, that is noone, even under the constraint can force a voter to proove that he is the author of a given ring signature. 
(see news bellow) Ring Signatures are short (constant size and not function of the number of registered voter), and also linkable. Linkability is the property that two ring signatures generated from the same secret key has a commun tag while ring signature generated from differents secret keys, different users, have different tags. It is then easy to detect double or multiple votes from the same citizen.

\section{News}
We are in a very early phase and trying to improve all parts of the \oeu{} project. 
Focus today is on implementing a realistic votings cenario. We are playing with regular RSA and DSA signatures for that. We had implemented the classical ring signature\cite{Rivest01}. We added the linkable feature to insure vote unicity. The current signature is currently too long so we have to propose a shortest version (constant in numbers of voters) using accumulators.\\
Optionaly, we will investigate some time released scheme in order to reveal voting results only at a defined time, reling on an Internet trusted time stamper.
One simple solution would be for a vote manager to generate a key for that and give everyone the private key when the desired time allapse, but what about if the manager does not send the private key?. 
The file sharing \pp{} framework is under construction, and we will enclose it soon in the \oeu{} code.

\section{Introduction}

 \oeu{} is a citizen initiative to provide to everyone for free in a simple and complete tool for organizing secure
%\footnote{Security is a matter of probability, but in the range of existing ballot systems our system expect to reach highest security level} electronic vote using anyone's computer ressources.\\
This project challenges to need less than 1000 lines of Python code in order to remain simple and easilly analysed\footnote{To compare with 13000 lines of Jif dedicated language + 8000 lines of Java code for the Civitas project.}.\\
We are addressing the problem of remote electronic voting using no hardware specific machine. The security model is based on usage of basic usual PC hardware and widely used OpenSource Software components.\\
Using \oeu{} add new features making polls more democratic compliant. It removes need of managing vote offices, and all activities/costs of traditional vote. You can initiate an election race, i-vote on some organization proposed poll and also verify yourself that the all voting process is secure. Basic skeels in Math equivalent to the average heighteen year's old young person. \\
"Open" means that all tools and data are Open-Source but also that the system is fully distributed and replicated. There is no need of some autority that would keep more secret, more power or more knowledge than the basic citizen. The security model is based on state of the art cryptography research results but also on the principle that Internet is large enought to maintain billion of copies of non infected software instances. Just try to imagine how hard would be for some malicious organization to infect at the same time all the Open-Source compilers, (\url{http://gcc.gnu.org} for instance) in the world to make the operation '1+1' computing '3' on one very specific source code and at the same time keep result equal to 2 for all other source code in the world!.\\
You might think that only high skill math and computer science research people can understand all this. Well we will try to keep as much simple as possible, using many tutorials, examples, faq, tests. It is amazing how you can find today on the Net very well written RSA Tutorials. We would like to reach the same result with only the i-vote problem in mind. The main goal is that a 18 years old (age allowing vote for citizens in many countries) everage educated person could understand every details, after spending a minimum time study on it. We even think that teaching all the i-voting scheme could be integrated in the general education process. This can be support for Math, Computer Science and Democratic studies. 

\section{Hello World!}
These two words 'Hello World!' is well known from software developpers. When learning a new computer language, everyone try to pass the simple test of printing these two words. This is to make you aware that you are reading the result of a computer transformation, not directly inserted data.  During this transformation, many other verifications, generation occurs using for instance a \pyt{} interpreter, a \LaTeX\cite{lamport94} compiler and a \pdf{} formatter. The source code, the \texttt{oeu.py} file is used to generate the documentation, let you organize a vote, register for an election, insert your ballot, merge ballot box, install the tool in a Web server, verify the results and many other things like improving the all system. 

\section{The \oeu{} roles}
Except for the \emph{TimeStamper} role, any citizen can play one or several roles, as Designer, Manager or Voter (more exactly voter candidate as some rules applies to be eligible as an autorized voter). There is no rules and nor constraint to candidate for these roles. It is only a matter of interest and skills. Nobody (individual or organization) shall discourage anyone to play these roles if he is interrested in. 
\begin{description}
\item[Designer]
A \emph{designer} is a person like me who design, improve, translate, fix \oeu{} the program given here (the same software generate the text you are currently reading). His name is listed in the text header. He or She follow simple rules (License propagation, digest publishing,...)
\item[Manager]
A Manager is a person or a group of persons (organization) that initiates a vote. The Manager does not modify the program. Usually, he is using the program of a designer who is not himself. A manager is in charge of initiating a vote, sending a unique signed \id{} to each citizen he would like to participate to a vote, let those citizen add their public key to the ring, revoque some IDs after a conflict and time stamp the urn to close the registration phase. He also close the vote by adding a final signed time stamp.
\item[Citizen]
A citizen is an individual (can be a group if it make sense to give one ballot for a group) having generated locally a couple of public key, private key. He or she can register to a vote organized by a manager using the urn of a designer. A citizen willing to vote had to sign the unique \id{} given by the manager. When the time stanp is set by the manager, he can vote.
The voting task is technically adding a Linkable Ring Signature to his choice message.
Any citizen can run validity checking tools on the urn, get voting results (temporary since not every registered citizen has not voted). Because the program and the data are all full text, every one, in particular citizer are invited to check validity and count with any external tools or even manually.  
Registered Citizen receve an e-mail from the namager before closing the vote.
\end{description}

\section{Crypto animals for \oeu{} !}
\begin{itemize}

\item{Digest}
A digest is a small string representing a usually large file. This is used to index files in large databases but also for a human beeing to remember or find a particular file. All files copies have the same digest. A very used feature is that have a small modification on a file (changing just on bit) will produce a completly different digest...easy for visual detection. More than one file have the same digest, but it is very hard from for example a spreadsheet file with some amount to change that value and add hidden content so that the digest would be the same than the original file. The solution, if found gives you a huge file size. On a text file (no hidden content) is even harder.   

\item{Alice, Bob and others}
Here the three most famous guys in Crypto World. Usually, Alice and Bob are nice guys, they will play roles of ellection manager or regular citizen in our i-vote scheme. Some guys are malicius and will do anything to crack or perturb the system. 

\item{Signature}
...
\item{RSA}
...
\item{DSA}
...
\item{Short Linkable Ring Signature}
...
\item{Time Stamp}
...
\end{itemize}

\section{The process}
\oeu{} tool is always improving but for using it, we must work on the same revision.
So the first thing to do is to select the \oeu, usually the last one and hoppely the more secure.\\
For a large election, the digest of \oeu{} has to be published on many place, and of course on the official web site of the organizer. This period of time has to be long enought to be sure that every one plan to use the same revision of \oeu, can download the initial ballot box and run it. 

The manager has already or build a list of all participants of the vote, but this list is outside \oeu{} because it contents private informations; the full name, date of birth, address, phone nombers, e-mail, social security number....anything that can identify with high probability the participants. Means use for such list depend on the criticity of the vote and we can immagine that for non critical elections, a simple e-mail may be requested. Note that the security level of this task is the same for a traditional vote or for preparing an i-vote.     

The manager then generate unique ids for each participants. It is better to generate a small hashed \id{} instead of positive integers, because a malicious participant would have more difficulties to guess valid ids. Also manager is invited to use a secure canal for sending these ids. The security s not impacted, just the number of revocated ids to manage before closing the list.

Each participant is invited to generate locally two keys RSA 2048 keys. Disconect the computer from the internet to be sure that nobody see what you are doing. Keep secret the private key (protected with at least with a pass phrase) and send the public key and and the signed \id{} to the manager. 

There is multiple way to keep secure the private key, with strong authentification. Each citizen should be concerned with this constrainst. If you loose your private key, no one can help you to recover it. It is then better to generate another one and register again to the vote after requesting a revocation of the old public key to the manager. If the vote has started (registration closed), you cannot vote if you don't have private key copy ! If someone thief your private key and the passphrase you have written on a paper (don't do that), and has access to all authentifications devices you used during key generation, then he/she can vote at your place. More exactly, if you vote and the thief also vote, the result depend if its or not on the same box (before or after merging). Voting twice on the same box is simply rejected the second ballot, but if you use another box to vote (referencing the same election), then both votes are saved, but during the merging operation of the boxes, linked signature will raise a flag. If your two or several votes are for the same candidate, your ballot is saved, but any difference in candidate selection will produce an null ballot (do not confuse with white ballot, that is more a supplementary option in the selection list, if the election manager allows it).

After receiving all public ids, merging lists, the manager close the registration phase by signing a time stamped message on the list. 

All revocated ids (and public keys) are removed from the list.
Then the list is fixed with the closure date. If anyone propose to new public \id{} list to the manager, the former cannot use it and even if a sign it, only the first time stamping signature is valid. Time confidence depend on the selected time stamping organization on the Net. For critical vote, selected an old and secure time stamper is requested.  
When the list is closed and published on the Net, it is easy for every one to check that he/she bellons to that list. There is not your full name, but just your public id. Save your public key secret if you don't whant anybody except the manager to know that you are participating to this vote. This is a poor anonymity that you cannot achieve with classical vote...every body in the vote office can see you.

Let the fun start!
Citizen can vote just after receiving the closed public \id{} list. Empty ballot box referencing the list can be fill in. 
The header of the list reference all candidates for the election, with some \id{} (small number). This \id{} is well visible on the ballot box after people vote. It is even easy to count temporary ballot results for each box. That is why we suggest to send the box file directly to some merging server. From this server you can dowload to latest merged box with all the ballots  mixed with yours. To some extend the merging server could find your ip address and correlate with your identity if it has access to an ip geographical adress dictionnary. It also has to have the box file just before you vote to compare them and found for who you votes. To protect from you from this, you can use any other computer not at your home, you can use dynamic ip adresses or anonymous ip adress. Also it is recommended to add several votes (several individuals) on the same box before sending to the merge server. If you don't mind having the risk to show your vote to your related or small group, then share the same box. Again, if the box file on a computer if not sniffed (you can install a fresh linux install from scratch and share it with a group you trust), then the vote order is not revealed. When voting \oeu{} insert the current vote at a random position. If you use an empty ballot box and send it to an individual, not a merging server, you cannot hide to him for who you vote. We can imagine that some people would prefer to go to some vote office providing computer ressources. There is less insurance that these computers are observers safe than that for your computer. The issue here is maintaining anonymity, but at large scale anonymous ballot are very probable. 

The result of the vote is not changed by the type of strategy (merging a lot of small boxes or less big boxes).
Note that with traditional vote, the same problem occurs, because on some very small vote office, knowing the results gives some assumption of who votes for who, people knowing each other. With a difference is that the citizen can chose to participate to a small or a large group with i-vote when he/she is forced to move to a designated vote office in traditional vote. 

Last task, the manager shall stop the vote because we cannot wait infinite time that all resgistered people vote. The voting closure date has to be published on the Web. When this date occurs, the manager sign a time stamp of the last ballot box. 

Imagine that some citizen claims to have voted before the closing date and he/she send too late the ballot box to a merge server or to the manager. Then this citizen has to add a time stamp on the ballot box. This time time is the proof that vote occurs before the closing date. What about if the citizen vote, time stamps, but do not share his ballot with other?
We can define a new delay, but informal. The manager will accept to merge boxes with time stamp before its own time stamp.
This case should be very improbable because each citizen is invited to check its vote on a web server.
The manager can also wait a small delay between the official closure date and its time stamping in order to include communication delays (few minutes to upload a file).

\section{FAQ}

\subsection*{How do insure that the text I am reading is the right one?}
This is simple, if your reading the text source file \texttt{oeu.py}. Find a computer with \pyt{} interpreter, Run the script, it should not complain if this is an original. Use a \LaTeX suite ('pdflatex' utility) on 'oeu.tex' generated file to build a \pdf{} formated document. 
If you are reading a Postscript, \pdf{} or HTML file, you do have a full insurance that this is the right document. We strongly recommend you to download to source file.
In both cases, to check the document origin and version, just check that the digest (in header \pdf{} document or in last line of text file) is the one given on the WWW \url{https://github.com/oeu/OpenElectronicUrn}).

\subsection*{What happen If someone change the content of this text?}
Well the modified file has a different digest, so any list or ballots referencing this digest will be invalid.
However, anyone can define his all \oeu{} like file and claims to have the original. This may raise copyright issues.
I invite you to check that the file digest is the one find here: \url{https://github.com/oeu/OpenElectronicUrn}. In that case, the \pdf{} document is there: \url{https://github.com/oeu/OpenElectronicUrn/oeu.pdf?format=raw}.

\subsection*{How do you preserve anonymous vote?}
This is the kernel of the system. linkable ring signature allows any member of a group of public keys to sign a message (here, the message contains the selection of the candidat) without saying anythin on her identity. Even on worse case any juge cannot prove that such a given signature comes from that individual. Everyone knows and can check that this is a member of the group who signed it. The linkable feature is some information that prove that the same individual signed two messages, still anonymouslly. This feature is used to refuse several vote of the same person. 

\subsection*{Putting several ballot in the ballot box is really not possible?}
No, linkable ring signatures have a tag that is always the same if signed by the same individual. However, knowing the tag does not reveal the identity of the signer. One of the basic check on the ballot box is to find signatures with the same tags and qualify the signer public signature as invalid (for the current ballot).  

\subsection*{Someone pick up my registration id, what can I do?}
A rule is that every participants to a vote has to sign the id.
If you did not received your id, contact the vote manager so see what is wrong, he will give you the same \id{} again.
If you received your \id{}, but you think that someone else had rip it off. Try to sign first and your safe.
If you try to sign after the thief, the urn will refuse registration. Contact the manager, prove your identity and then he will revocate your last \id{} and give you a new one. A revocated \id{} cannot participate to the vote.

\subsection*{If some smart guy cracks the algorithm?}
I am sure he or she will join us to fix the failure or improve the security of the system and will be qualified as the top designer. Until organization gives rewards, we will give him or her credit for nice contribution to democracy progress.

\subsection*{How do you merge ballot boxes?}
This is explained in details somewehere else, but the idea is to merge only compatibles ballot boxes (referencing the same list, that reference the same \texttt{oeu.py} file) and to remove the identical parts.

\subsection*{Can you merge vote list?}
With some constrainsts. During registration, list of public keys can be merged, but when the vote start, the list of public keys shall be fixed. Such list (digest) is referenced by the ballot box. 

\subsection*{Why do you put every thing in text files?}
Because text file can be read with many and any text editor and it would be impossible for any cracker to infect all text editors on the planet at the same time without being discovered. Of course text files are not very compact, but it is not a big issue for voting. You can compress the text file (zip, tgz, bz2,...) before sending it on networks. 
Text files can be used for building documents (LaTex suite), write source code and store data...all we need for i-vote.

\subsection*{Why \pyt{} code?}
It could have been any other language, but this one is used worldwide (impact on security), compact (text file size), modern (buildin high level idioms), easy to learn (very important for the project philosophy) and has nice libraries. In particular, the \emph{pycrypto} module provides tools for cryptographic algorithm.

\subsection*{Your system is very old fashon, we have now nice graphical interfaces?}
Your are right, but we do not want to sacrify the security in making beautiful user interfaces. Graphical rendering is not requested for the moment (We did not currectly investigate the problem of showing candidate face pictures instead of their names or ids ...shall democratic countries assume that voters can read?).

\subsection*{What about hitorical/economical/social/political studies of i-vote?}
We are reading carefully these studies and we welcome all suggestions and contribution in the group.

\subsection*{When a translation in other local languages?}
Our first goal is to mature one version in english to collaborate with the maximum of developpers, crypto experts and anybody having ideas on i-vote. Also \oeu{} shall pass first release tests. One time will come that translation will be requested and we hope to find many free contributions arround. I can do it for French if been helped for my English! .

\subsection*{Can I run tests set?}
This is done automatically each time you run \oeu{}. We may include an option to bypass all tests if they take too much time.
\subsection*{Is there White ballot?}
Yes, a special ballot for that is added to the list of real candidates. Its name \emph{white ballot} and the content is a white spaces string. Furthermore, \oeu{} dost not allow candidat name very close to some keywords like \emph{white} or \emph{ballot} or \emph{null} for all selected election natural languages.

\section{The little story}
I started the project the day I registered for voting for the preliminary election of the Green party in France (EELV June 2011). This election was running on Internet and managed by a private company, Extelia. Opacity of the process and poor security level makes me sceptical, knowing that the former company claims for a very high security and certification level.\\ 
I also found on Internet citizen associations against e-vote or i-vote. I share their worries for the present in 2011 but not for the future. I also found very interresting papers on 'group/ring signature' and how anonymity can be achieved. I did not found ring signature implementation so I start to build my own with the original paper.\\
This is not my research field, so I have hard time to understand all the details. I would be interrested by learning from the experts of the domain and hope such people will join the project later.
It seems that starting early 2000, some serious papers describe realistic e-vote schemas, but also I did not found any open source implementations on the Net. So I decided to start this project hopping to build a simple but operational implementation for i-vote. \\
I am targetting an i-vote for the French presidential election of 2017 or an hypothetic European race at the same date. That let us time to test implement, document, test, teach and communicate about the \oeu{} project. My son Tom will exactly be 18 years old in 2017 and he will be allowed to vote maybe the first time using a Secure Electronic system at a very large scale election race.

%\glossary{}

\begin{thebibliography}{99}
\bibitem{lamport94} Leslie Lamport \emph{\LaTeX: A Document Preparation System}. Addison Wesley, Massachusetts, 2nd Edition, 1994.
\bibitem{Rivest01} Ronald L. Rivest and Adi Shamir and Yael Tauman, \emph{How to leak a secret}, In ASIACRYPT 2001, pages 554--567, Springer-Verlag,2001.
\bibitem{Bresson01} E. Bresson, J. Stern, and M. Szydlo. \emph{Threshold ring signatures and applications to ad-hoc groups.}, In Proc. CRYPTO 2002, pages 465--480, Springer-Verlag,2002 LNCS Vol 2442.
\bibitem{Liu01} J.K.Liu,V.K.Wei, and D.S. Wong. \emph{Linkable spontaneous anonymous group signature for ad-hoc groups}, In ACISP 04,volume 3108 of LNCS, pages 325--335, Springer-Verlag,2004.

\end{thebibliography}
"""
__author__=r'Citizen$\Lambda$'
__version__='0.1'
__state__='Test'

import os,sys,re,base64,hashlib,copy,getopt,shutil
import time,datetime,random,getpass,zlib,operator
import urllib,dbhash,struct
from subprocess import Popen, PIPE

try:
    import Crypto.PublicKey.RSA
    import Crypto.PublicKey.ElGamal
    import Crypto.PublicKey.DSA
except:
    print '...python pycrypto module not installed!'

preSt,regSt,votSt,cloSt = range(4)
__smallringsize__ = 50

def make_readme(digest):
    """
    Welcome to the OEU project, do not hesitate to share your viewpoint and contribute if you wish.\n\n
    This is a 'just one file' project; the full documentation and the source code are a unique Python file; 'oeu.py'.
    This file includes all you need to understand and play with the project.\n\n
    To have formated documentation, run the 'oeu.py' file to build 'oeu.tex' (LaTeX) file, compile and print it.\n
    For your convenience, the 'oeu.pdf' PDF file is commited.\n\nEnjoy!"""
    o = 'SHA1 digest: %s\n\n'%digest[:10]
    print '...build readme file for GitHub'   
    open('README.md','w').write(o + make_readme.__doc__)

def abstract(res):
    r"""The source file used to generate the current \pdf{} formated document is \oeu{} (prononced [\oe{}vot]), a complete and secure Internet voting (\emph{i-vote}) system as a basic of democracy voting tool taking advantage of the today numeric world.
The specification, the design and the implementation of \oeu{} are presented here, knowing that all \oeu{} is included in one unique file \texttt{oeu.py} using \pyt{} programming language to run on any computer. This document is also a user's guide and a recipient for real data of an election race. As an Open-source project driven by independent citizens, \oeu{} will continiously improve its security model and its tutorials\footnote{also a Wikipedia page may be available later on.} in order to anyone to understand how it works. We hope it will become a trustworthy system\footnote{our vision is to make \oeu{} ready, tested, approuved and certified for a very large election race in Europe for instance by 2017 !}. The target users are any citizen enable to vote, so we will happy to get your feedback from citizens, especially to focus on unclear points and we will review them\footnote{issues or feature requests can be posted on \emph{GitHub} \url{https://github.com/oeu/OpenElectronicUrn/issues}}.
\oeu{} does not follow a usual approach in a sense that the project is driven by non cryptography experts; However the kernel algorithms are reviewed by both computer scientists and math researchers. We use our own open vision of what should be the requirements of an electronic voting system in modern democracies and we try to carrefully analyse social and political research in that field. 
\oeu{} is also a model of decentralized creation and usage as it is based on a file sharing \pp{} protocol over Internet.
This generated documentation also had run \oeu{} on a real or a simulated ballot box for an election race. So you may just be interrested by the results bellow.
Lastly we would like to build with your help a contemporary artwork based on \oeu{} and promoting this kind of democratic design approach."""
    o = r'\begin{center}'
    #o += r'\begin{tikzpicture}[x={(-0.5cm,-0.5cm)}, y={(0.966cm,-0.2588cm)}, z={(0cm,1cm)}, scale=0.6, color={lightgray},opacity=.5]'
    #o += r'\tikzset{facestyle/.style={fill=lightgray,draw=black,very thin,line join=round}}'
    o += r'\begin{tikzpicture}' + '\n'
    o += r'\draw[blue!40!white] (0,0) rectangle (6,4); \fill[blue!10!white] (2.4,4) rectangle (3.6,4.15);' + '\n'
    for i in range(res[7]):
        x,y = random.randrange(2,538)/100.0,random.randrange(2,300)/100.0
        o += r'\filldraw[fill=green!30!white,draw=white] (%s,%s) rectangle (%s,%s);'%(x,y,(x+0.58),(y+0.38)) + '\n'
        o += r'\filldraw[white] (%s,%s) -- (%s,%s);'%((x+0.29),(y+0.19),(x+0.58),(y+0.38)) + '\n'
        o += r'\filldraw[white] (%s,%s) -- (%s,%s);'%(x,(y+0.38),(x+0.29),(y+0.19)) + '\n'
    o += r'\end{tikzpicture}\end{center}' + '\n'

    o += r'\begin{tabular}{|l|l|}' + '\n' + r'\hline' + '\n'
    o += r'Election name& \texttt{"%s"}\\'%res[1]
    o += r'Box number& \texttt{%s}\\'%res[2]
    o += r'State& \texttt{%s}\\'%('closed' if res[5] == cloSt else ('vote' if res[5] == votSt else 'register'))
    o += r'Registration end& \textit{%s}\\'%res[3]
    o += r'Vote closing& \textit{%s}\\'%res[4]
    o += r'Casted/registered& $%s/%s$\\'%(res[7],res[6]) +'\n'
    o += r'\hline\end{tabular}' + '\n'
    o += r'\quad' + '\n'
    o += r'\begin{tabular}{|l|l|}\hline'
    l = res[8].items()
    l.sort(key = operator.itemgetter(1),reverse=True)
    n = 0
    for x in l:
        o += r'%s & %s\\'%(r'\textit{%s}'%x[0] if x[0] == 'White Ballot' else r'\texttt{%s}'%x[0],x[1]) 
        if n == 0:
             o += r'\hline' + '\n'
        n += 1
    o += r'\hline\end{tabular}' + '\n'


    #o += r'\item The designer\textquoteright s digital signature of this document (the source file \texttt{oeu.py}) is: \tiny $$\verb!%s!$$ \normalsize'%rsa(IKey).sign(open(__file__).read()) + '\n'

    return r'\begin{abstract}' + abstract.__doc__ + r'\end{abstract}' + o

def make_apache(digest):
    """
    \nWSGIScriptAlias /oeu /home/laurent/OpenElectronicUrn/oeu.py""" 
    print '...build oeu.conf file for Apache' 
    open('oeu.conf','w').write('#Apache configuration file for wsgi\n#%s'%digest + make_apache.__doc__)

def insert_code(name):
    """ ....in LaTeX """
    o = r'\lstset{basicstyle=\ttfamily ,numbers=left, numberstyle=\tiny, stepnumber=5, numbersep=5pt}'
    d = False
    o += r'\begin{lstlisting}[texcl]' + '\n'
    for l in open(__file__).readlines():
        if re.match(r'(if|def|class)',l): d = False
        if re.match(name,l): d = True
        if d: o += l
    return o + r'\end{lstlisting}' + '\n'

def expand_tag(s):
    return re.sub(r'@([^@]+)@',lambda m: eval(m.group(1)+'()'),s)

def longcalculus():
    a,b,c = random.randint(1<<80,1<<100),random.randint(1<<60,1<<80),random.randint(1<<100,1<<140)
    o = r'\begin{eqnarray}'
    o += r'x&=&a^b \bmod{c} \leftrightarrow  \text{[\pyt \: code]} \: \texttt{x = pow(a,b,c)} \nonumber \\'
    o += r'a&=&%s \nonumber \\b&=&%s \nonumber \\ c&=&%s \nonumber \\ x&=&%s \nonumber'%(a,b,c,pow(a,b,c))
    return o + r'\end{eqnarray}'

def oeulength():
    return '$%d$'%len(open(__file__).readlines())

def getstate():
    return r'\emph{State}: \Huge \texttt{%s} \normalsize \emph{Election}: \Huge \texttt{Poll Test} \normalsize \\'%__state__

def make_document(box,digest,res): 
    """ Generate LaTeX document """ 
    #o += r'\usepackage{fancyhdr,lastpage}\\\pagestyle{fancy}\fancyhf{}\\'
    #o += r'\rfoot{\scriptsize{Page \thepage\ of \pageref{LastPage}}}' + '\n'
    o = '%% This file is generated by running \'oeu.py\' file (digest:%s)\n%% Do not edit by hands!\n'%digest
    o += r'\documentclass[a4paper,10pt]{article}' + '\n'
    o += r'\usepackage[margin=2cm]{geometry}' 
    o += r'\usepackage[utf8]{inputenc}'
    o += r'\usepackage{url}'
    o += r'\usepackage{listings}' 
    o += r'\usepackage{lmodern}\usepackage{color}\usepackage{lettrine}' 
    o += r'\usepackage{graphicx}\usepackage{tikz}\usetikzlibrary{calc,3d}'+ '\n'
    o += r'\newcommand{\oeu}{\textsc{\OE vote}}\newcommand{\pyt}{\emph{Python}}\newcommand{\id}{\textsc{id}}\newcommand{\pdf}{\textsc{pdf}}\newcommand{\pp}{\textsc{p2p}}\newcommand{\sha}{\textsc{sha1}}' + '\n'
    o += r'\title{\bf \oeu{} -- The Open Electronic voting system}' + '\n'
    o += r'\begin{document}' + '\n'
    o += r'\lstset{language=Python}'
    o += r'\author{\copyright{} %s \url{openurn@gmail.com}}'%__author__ + '\n'
    o += r'\maketitle' + '\n'
    o += r'\begin{center}' 
    k = itob64(Crypto.PublicKey.RSA.importKey(open('keys/laurent.pem').read()).publickey().n)
    o += r'Version: \emph{%s} -- Digest:\footnote{the first five hexadecimal bytes of the \sha{} digest. Please first check that you are reading the last revision of the document by comparing this digest code with the one given on the \oeu{} project Web page on Internet \url{https://github.com/oeu/OpenElectronicUrn}, and second by downloading (also from this web site) the source file \texttt{oeu.py} and running an external utility like \texttt{sha1sum} on it. If the result is the same digest, it means that you are probably reading the non altered \oeu{} official document. Running the \texttt{oeu.py} \pyt{} file with a \LaTeX{} suite installed shall rebuild the document named \texttt{oeu.pdf}.} \texttt{%s}\\'%(__version__,digest[:10]) + '\n'
    o += r'Public key: \small $\verb!%s!$\\$\verb!%s!$\footnote{the quote printable base64 encoded RSA $n$ parameter on length 1024 bits with $e=0x10001$.} \normalsize \\'%(k[:80],k[80:]) 
    o += r'\end{center}'
    o += abstract(res) + '\n'
    o += expand_tag(__doc__) + '\n'
    o += r'\onecolumn\\'
    o += r'\section{Designer\textquoteright s Signature}\\' 
    IKey = Crypto.PublicKey.RSA.importKey(open('keys/laurent.pem').read())
    o += r'\begin{description}\\'
    o += r'\item The designer\textquoteright s digital signature of this document (the source file \texttt{oeu.py}) is: \tiny $$\verb!%s!$$ \normalsize'%rsa(IKey).sign(open(__file__).read()) + '\n'
    
    #o += r'\item How to verif the signature manually ? $msg =? s^e mod n$'
    #return int(hashlib.sha1(x[:4]+msg).hexdigest(),16) == pow(b64toi(x[4:]),self.kl.e,self.kl.n)
    
    o += r'\end{description}'
    o += r'\section{The \pyt{} Code}' + '\n'
    o += r'\subsection{The Ring Signature}'+ '\n'
    o += r'The \texttt{ring} \pyt{} class provides anonymous signature in a set of signers; the ring.'
    o += insert_code(r'class\s+ring:')
    o += r'The \texttt{ringB} \pyt{} class provides a variation of the initial ring signature not using $E^{-1}$ permutation function.'
    o += insert_code(r'class\s+ringB\(')
    o += r'The \texttt{RSA} \pyt{} class provides a individual RSA signature.'
    #o += insert_code(r'class\s+RSA\(')
    o += r'The \texttt{ringBL} \pyt{} class is derived from ring signature with linkability.'
    #o += insert_code(r'class\s+ringBL\(')
    o += r'\subsection{The validation function}' + '\n' 
    #o += insert_code(r'def\s+validate\(')
    o += r'\section{The Data}\\See generated \texttt{%s} text file (size:%s kbytes).\\'%(box,(os.path.getsize(box)//1024))
    o += r'The first line show it is a format for \oeu{} followed by a code difining uniquelly a \oeu{} revision for a particular designer.\\'
    o += r'The second line defines election attributes; name, id, box number, date to start and end voting and url of the timestamper site.\\'
    o += r'The third line defines all candidates (White ballot is automatically added), with the name of the organization.\\'
    o += r'The line starting with \texttt{"\%"} character defines blabla.\\' 
    o += r'Lines starting with \texttt{"@"} character are signatures.\texttt{@S},\texttt{@M},\texttt{@D} are respectivelly signature of the Timestamer, the Manager and the Designer.\\' 
    o += r'Lines starting with \texttt{";"} character are encrypted voting ballots.\\'
    o += r'Lines starting with \texttt{"."} character are voters public key and their credential signature. The visible 8 first characters of the credential are the id given during the registration. Voter can visually check if he is registered with that id.\\' 
    o += r'Lines starting with \texttt{"!"} character are encrypted voting ballots.\\'
    o += r'Line starting with \texttt{"\$"} character is cleartext election result.\\'
  
    o += r'\tiny \begin{verbatim}' + '\n' 
    if os.path.isfile(box):
        bal,size = open(box),184
        for l in bal.readlines():
            o += l[:size]+r'...'+'\n' if len(l) > size else l
    bal.close()    
    o += r'\end{verbatim}\normalsize' + '\n' 
    o += r'\section{User\textquoteright s guide}\\'

    o += r'If you just want to participate to a vote, you should first get an empty \oeu{} box python file. Usually, the organizer of the vote had published this file on one or more Web servers, but you can also get a copy from anyone you know. Just be carefull that the name of election and \id{} are the ones your are looking for. The organizer had also published a digest of his public key. Check that is the right one. A malicious person may initiate an election with the same name and publish it widelly so people do not know who is the official. There is little centralization on \oeu{} team in a way that the \oeu{} project repository\footnote{\url{https://github}} can register election names and will return a unique election \id{}. \\'
    o += r'Just run the downloaded file \texttt{oeu.py}; double click on its icon if your are using a graphic file manager or run the commande line: \texttt{oeu.py} in a terminal (you may run \texttt{python oeu.py} depending on the file rights)\\'

    o += r'If you are interrested in a new election run, the box is in the state \emph{registration}. Open the generated \pdf{} file (\texttt{oeu.pdf}) and you will see the document you are currently reading but instanciated for the election you are seeking. You will see an image of the ballot files for each acandidate of the election.'

    o += r'\section{Ballots}\\'
    for c in res[8].keys():
        o += r'\fbox{\includegraphics[scale=0.4]{%s}} '%os.path.abspath(re.sub(r'\s','_','%s.pdf'%c))
        
    o += '\n' + r'\begin{flushright}\emph{The end of the document}\end{flushright}' + r'\end{document}'+'\n'
    print '...build oeu.tex file for LaTeX'
    open('oeu.tex','w').write(o)
    export_pdf('oeu.tex')

def gen_keys_old(name):
    """ generate PEM format keys """
    d = 'keys'
    if not os.path.isdir(d):
        os.mkdir(d)
    if not os.path.isfile('%s/%s.pem'%(d,name)):
        open('%s/%s.pem'%(d,name),'w').write(Crypto.PublicKey.RSA.generate(1024,os.urandom).exportKey('PEM')) 

def gen_mail(players,election,manager):
    """ """
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
        o += r'\documentclass{letter}\\\signature{The manager}\\'
        o += r'\address{%s\\%s \\ City \\ Country}\\'%(name,players[name])
        o += r'\usepackage[margin=2cm]{geometry}\\'
        o += r'\usepackage[utf8]{inputenc}'
        o += r'\usepackage{url}\\'
        o += r'\newcommand{\oeu}{\textsc{\OE vote}}\\'
        o += r'\begin{document}\\'
        o += r'\begin{letter}'
        o += r'{Election ID: %s\\ Manager: %s \\ Web Site:\url{http:\....} \\France}\\'%(voteID,manager)
        o += r'\opening{Dear %s:}\\'%name
        o += r'Please Find bellow your personnal ID code for registering to \emph{%s} elections\\\\'%election

        o += r'\begin{verbatim}' + '\n\n\t\t%s\n\n'%theid + r'\end{verbatim}\\'

        o += r'Keep it secret until you registered for this election.\\\\'
        o += r'When you are registered, this code is public and you can share it as a proof of registration.\\'
        o += r'You should have received this letter in a well sealed envelope.\\'
        o += r'\oeu{} team strongly recommand to manager to send this by regular mail, not e-mail because your main living address is for us a good proof of your identity.\\'
        o += r'If by chance, you should not but you received several letters like this, so several ID, for the same election. This means that the manger knows you with different identities. This is an error of the manager, not the \oeu{} team. The manager should take all means, including geographical investigation, meeting you physically, to insure unicity of your identity on its list. He/she will be gracefull from you to know that error and fix it.\\\\'
        o += r'If someone else than you has opened the envelope, or just seen and copy your personnal ID,\\'
        o += r'please contact the election manager for requesting another personnal ID. He will recovate this one.\\\\'
        o += r'If you are not willing to vote for this election, you should destroy this letter\\'
        o += r'Just be aware that anyone getting access to your ID can register in your place,\\'
        o += r'and will be able to vote for you if you are not contacting the manager to revocate the ID.\\\\\\'
        o += r'\closing{Enjoy \oeu{},}\\'
        o += r'\ps{P.S. Contact \oeu{} project team for any security related question.}\\'
        o += r'\encl{A copy of \oeu{} full document, can also be downloaded at: \\ \url{https://github/oeu/OpenElectronicUrn/blob/master/oeu.pdf?raw=true}}\\'
        o += r'\end{letter}\\'
        o += r'\end{document}' + '\\'
        open('mail/%s.tex'%name,'w').write(o) 
        export_pdf('mail/%s.tex'%name)
    open('id.txt','w').write(oi + '# end\n')

def get_candidates(box):
    """ """
    for l in open(box).readlines():
        if re.match(r'%\s(\{.*)$',l):
            return eval(l[1:])
    return {}

def init_stamper(box,stamper,endDate):
    """ """
    endDate = get_close_date(box)
    StamperKey = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%stamper).read())
    open('election.pem','w').write(Crypto.PublicKey.RSA.generate(1024,os.urandom).exportKey('PEM')) 
    electionKey = Crypto.PublicKey.RSA.importKey(open('election.pem').read())
    pub,xcode = electionKey.n,b64toi(rsa(StamperKey).sign('%s'%endDate))^electionKey.d
    open(box,'a').write('%% Election:%s %s\n'%(itob64(pub),itob64(xcode)))
    return pub,xcode

def request_stamper(stamper,now):
    """ """
    StamperKey = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%stamper).read())
    return rsa(StamperKey).sign('%s'%now)

def create_box(box,digest,manager,stamper,poll,candidates,bD,eD,nb=100):
    """ """
    vID,n,c = h2b64(hashlib.sha1(poll).hexdigest()[:10]),0,{0:'White Ballot'}
    ManagerKey = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%manager).read()) 
    StamperKey = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%stamper).read())
    for x in candidates:
        n += 1
        c[n] = x
    h = '%% OE v%s SHA1:%s Election:"%s" ID:%s Start:[%s] Stop:[%s] Nb:%d\n%% %s\n'%(__version__,digest,poll,vID,bD,eD,nb,c)
    h += '%% Manager:%s\n'%itob64(ManagerKey.publickey().n)
    h += '%% Stamper:%s\n'%itob64(StamperKey.publickey().n)
    open(box,'w').write('%s@ %s\n'%(h,rsa(ManagerKey).sign(h)))

def get_pub_key(box,t):
    """ """
    for l in open(box).readlines():
        m = re.match('%\s(Manager|Stamper):([\w\-]+)$',l)
        if m and t == m.group(1):
            return b64toi(m.group(2))    
    return None

def get_el_pub_key(box):
    """ """
    for l in open(box).readlines():
        m = re.match('%\sElection:([\w\-]+)\s([\w\-]+)$',l)
        if m:
            return b64toi(m.group(1)),b64toi(m.group(2))    
    return None

def get_close_date(box):
    """ """
    for l in open(box).readlines():
        m = re.search('Stop:\[([^\]]+)\]',l)
        if m:
            return m.group(1)
    return None

def register(box,I,z):
    """ """
    ManagerPubKey = None
    myK = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%I).read())
    seen,i,mngrk,name,num = {},0,None,'',0
    for l in open(box).readlines(): 
        if re.match(r'\(',l):
            name,ha,num,d1,d2,url = eval(l)
        elif re.match(r'%\s[\w\-]{10,200}$',l):
            mngrk = l[2:-1]
        elif mngrk and reg(re.match(r'\;([\w\-]{10,200})$',l)):
            if rsa(myKey(b64toi(mngrk))).verify('%d_%s_%d'%(i,name,num),z+reg.v.group(1)):
                open(box,'a').write('.%s %03d %s %s\n'%(z,i,itob64(myK.publickey().n),rsa(myK).sign(z)))
                create_ballots(box,I,z)
            i += 1

def check_registration(box,I):
    """ """
    ManagerKey = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%I).read())
    lid,revocable,seen = {},{},{}
    for l in open('id.txt').readlines():
        m = re.match(r'\d+\s(\S+)\s(\S+)$',l)
        if m:   
            lid[m.group(1)] = m.group(2)
    for l in open(box).readlines():
        m = re.match(r'#\s([\w\-]+)\s([\w\-]+)$',l)
        if m: 
            currentK = myKey(b64toi(m.group(1)))
            a,found = rsa(currentK),False
            for item in lid.keys():
                if a.verify(item,m.group(2)):
                    if seen.has_key(lid[item]):
                        revocable[m.group(1)] = True
                    found,seen[lid[item]] = True,True
            if not found:
                revocable[m.group(1)] = True
    if revocable: # FIX BOX
        for l in open(box).readlines():
            print revocable,seen
    shutil.move(box,box+'~')
    o,p,header = '',None,''
    for l in open(box+'~').readlines():
        m = re.match(r'@\s([\w\-]+)\s([\w\-]+)$',l)
        if m:
            p = m.group(1)
        elif re.match(r'#\s([\w\-]+)\s([\w\-]+)$',l):
            o += l
        elif re.match(r'%',l):
            header += l
    open(box,'w').write(header + '@ %s %s\n'%(p,rsa(ManagerKey).sign(header+o)) + o)

def check_registration_old(box,I,theId):
    """ """
    o,manS,manK,youarein = '',None,None,False
    for l in open(box).readlines():
        m = re.match('@\s([\w\-]+)\s([\w\-]+)$',l)
        if m:
            manK = myKey(b64toi(m.group(1)))
            manS = m.group(2)
        else:
            o += l
    #assert manK and manS and rsa(manK).verify(o,manS)
    # find her entry
    aKey = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%I).read())
    for l in open(box).readlines():
        m = re.match(r'#\s(%s)\s([\w\-]+)$'%itob64(aKey.publickey().n),l)
        if m:
            if rsa(aKey).verify(theId,m.group(2)): 
                youarein = True
    return youarein

def cast(box,I,choice='White Ballot'):
    """ I select choice in candidat list """
    smallringsize = __smallringsize__
    IKey = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%I).read())
    fullring,index,i,crypted,d2s,found,cands = [],0,0,None,[],False,{}
    for l in open(box).readlines():
        if re.match(r'\(',l):
            name,h,num,d1,d2,url = eval(l)
            tsprk = urllib.urlopen(url).read()
            d2s = eval(urllib.urlopen(url+'?d='+d2).read())
        elif re.match(r'\{',l):
            cands = eval(l)
            cands['White Ballot'] = 'ok'
        elif reg(re.match(r'\.([\w\-]{10})\s(\d{0,10})\s([\w\-]{10,200})\s([\w\-]{10,200})$',l)):
            if reg.v.group(3) == itob64(IKey.n):
                index,found = i,True
                fullring.append(IKey)
            else:
                fullring.append(myKey(b64toi(reg.v.group(3))))
            i += 1
    if not found:
        return '\'%s\' is not registered!'%I
    if not cands.has_key(choice):
        return '\'%s\' choice is not one of selectable'%choice
    crypted = rsa(myKey(b64toi(d2s[0]))).encrypt(b64toi(base64.urlsafe_b64encode(choice)))
    pos,lind = setsample(len(fullring),index,smallringsize)
    smallring = getsample(fullring,lind,smallringsize) if lind else fullring
    open(box,'a').write('!%s %s %s\n'%(lind,crypted,ringBL(smallring).sign(crypted,pos)))  

def vote_old(box,I,choice,pub_el):
    """ I select choice (number) in box """
    aKey = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%I).read())
    fullring,i,index = [],0,0
    for l in open(box).readlines():
        m = re.match(r'#\s([\w\-]+)\s([\w\-]+)$',l)
        if m:
            k = b64toi(m.group(1))
            if k == aKey.publickey().n:
                fullring.append(aKey)
                index = i
            else:
                fullring.append(myKey(k))
            i += 1
    # clear
    sig = ringB(fullring).sign('<%d>'%choice,index)
    #open(box,'a').write('<%d> %s\n'%(choice,sig))
    # encrypted
    z = rsa(myKey(pub_el))
    encr = z.encrypt(choice)
    sig = ringB(fullring).sign(encr,index)
    open(box,'a').write('%s %s\n'%('<%s> '%encr,sig))
    create_pdf('receipt.pdf','%s'%datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),itob64(aKey.n))
    #pw = getpass.getpass()

def timestamp(box,I):
    d2, StprKey = '',Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%I).read()) 
    for l in open(box).readlines():
        if re.match(r'\(',l):
            name,h,n,d1,d2 = eval(l)
    return rsa(StprKey).sign(d2)

def is_good_race(box,pub,el):
    name = ''
    for l in open(box).readlines():
        if re.match(r'\(',l):
            name,h,n,d1,d2,url = eval(l)
        elif reg(re.match(r'~\s([\w\-]{10,200})$',l)):
            if name == el and rsa(myKey(b64toi(pub))).verify(name,reg.v.group(1)):
                return True
    return False
    
def tally(box):
    """ tally box """
    d2,tsprk = '',None
    lcand,lcrypted,res = ['White Ballot',],[],{}
    nreg,nvot = 0,0
    for l in open(box).readlines():
        if re.match(r'\(',l):
            name,h,n,d1,d2,url = eval(l)
            tsprk = urllib.urlopen(url).read()
            d2s = eval(urllib.urlopen(url+'?d='+d2).read())
        elif re.match(r'\{',l):
            lcand += eval(l).keys()
        elif reg(re.match(r'!([\w\-]{2,100})\s([\w\-]{100,200})\s(.+)$',l)):
            nvot += 1
            lcrypted.append(reg.v.group(2)) 
        elif re.match(r'\.([\w\-]{10})\s(\d{0,10})\s([\w\-]{10,200})\s([\w\-]{10,200})$',l):
            nreg += 1
    for x in lcand: res[x] = 0
    for i in lcrypted:
        res[itos(rsa(myKey(b64toi(d2s[0]),b64toi(d2s[1])^b64toi(d2s[2]))).decrypt(i))] += 1
    open(box,'a').write('$ %s/%s %s\n'%(nvot,nreg,res))

def approve(box,man):
    o = open(box).read()
    MngrKey = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%man).read()) 
    open(box,'a').write('@ %s\n'%rsa(MngrKey).sign(o))

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
    """ Defines RSA key Public key:n,e Private key:d"""
    def __init__(self,n,d=None,e=0x10001,l=1024):
        self.n,self.d,self.e,self.l = n,d,e,l

class mydsaKey:
    """ Defines RSA key Public key:n,e Private key:d"""
    """ y,g,p,q public """
    def __init__(self,n,d=None,e=0x10001,l=1024):
        self.n,self.d,self.e,self.l = n,d,e,l


class myKey2:
    """ Defines RSA key Public key:n,e Private key:d"""
    def __init__(self,n,d=None,p=None,q=None,e=0x10001,l=1024):
        self.n,self.d,self.p,self.q,self.e,self.l = n,d,p,q,e,l

def itob64(n):
    """ utility to transform int to base64) """
    c = hex(n)
    c = c[2:-1] if c[-1] == 'L' else c[2:]
    if len(c)%2:
        c = '0'+c
    x = base64.urlsafe_b64encode(c.decode('hex'))
    return re.sub(r'=*$','',x)

def btob64(b):
    """ transform binary to base64) """
    x = base64.urlsafe_b64encode(b)
    return re.sub(r'=*$','',x)

def b64toi(c):
    """ transform base64 to int """
    if c == '': return 0
    v = c + '='*((4-len(c)%4)%4)
    x = base64.urlsafe_b64decode(v)
    return int(x.encode('hex'),16)

def b64tob(c):
    """ transform base64 to binary """
    v = c + '='*((4-len(c)%4)%4)
    return base64.urlsafe_b64decode(v)

def itos(nb):
    c = itob64(nb)
    v = c + '='*((4-len(c)%4)%4)
    return base64.urlsafe_b64decode(v)

def h2b64(c):
    """ """
    if len(c)%2:
        c = '0'+c
    x = base64.urlsafe_b64encode(c.decode('hex'))
    return re.sub(r'=*$','',x)

class ring:
    """ RSA Ring Signature from Rivest, Shamir and Tauman
    Usage: r is a ring of RSA keys, S is the signature
    Assume signer is here the second members in the ring
      a = oeu.ring(r)
      S = a.sign('hello world!',2) 
      assert a.verify('hello world!',S)
    """
    # see \cite{Rivest01}
    def __init__(self,kl,l=1024):
        """ Set public keys, RSA size """
        self.kl,self.l = kl,l
            
    def permut(self,msg):
        """ Define permutation list from message """
        x = int(hashlib.sha1(msg).hexdigest(),16)
        self.p,self.p1 = [],[]
        while x > self.l:
            q,r = x//self.l,x%self.l
            self.p.append(r)
            self.p1.insert(0,r)
            x = q
        
    def E(self,x,w=True):
        """ Apply Message Permutations """
        # $E_k()$ and $E_k^{-1}()$ functions in the paper
        p = self.p if w else self.p1
        for i in range(len(p)-1):
            y = ((x>>p[i])^(x>>p[i+1]))&1
            x = x^((y<<p[i])|(y<<p[i+1]))
        return x

    def trap(self,x,e,n):
        """ Modified RSA trap """
        # $g()$ function in \cite{Rivest01}      
        q,r = x//n,x%n
        return q*n + pow(r,e,n) if (q+1)*n <= 1<<(self.l-1) else x

    def sign(self,msg,s): 
        """
        Find ys solution of:
        """
        # $y_s = E_k^{-1} \left( y_{s+1} \oplus \dots E_k^{-1} \left( y_n \right)\dots\right) \oplus E_k \left( y_{s-1} \oplus \dots E_k \left( y_1 \right)\dots\right)$
        self.permut(msg)
        x,y = [],[]
        for i in range(len(self.kl)):
            if i != s:
                xi = random.randint(0,2**self.l-1)
                x.append(xi)
                y.append(self.trap(xi,self.kl[i].e,self.kl[i].n))
        ya = reduce (lambda ya,i:self.E(i^ya),y[:s],0)
        yb = reduce (lambda yb,i:i^self.E(yb,False),reversed(y[s:]),0)
        x.insert(s,self.trap(ya^self.E(yb,False),self.kl[s].d,self.kl[s].n))
        return ' '.join('%s'%itob64(xi) for xi in x)

    def verify(self,msg,X):
        """ Check this equation: """
        # $E_k \left( y_n \oplus E_k \left( y_{n-1} \oplus E_k \left( \dots\oplus E_k \left( y_1 \right) \dots \right) \right) \right) \equiv 0$
        self.permut(msg)
        x = []
        for xi in X.split(): x.append(b64toi(xi))
        Y = map(lambda i,j:self.trap(i,j.e,j.n),x,self.kl)
        return reduce (lambda x,y:self.E(x^y),Y,0) == 0

class ringB(ring):
    """ 
    Improved Ring Signature
    """
    # see \cite{Bresson01}
    def sign(self,msg,s): 
        """
        Find ys such that E(yn....^E(y2^E(y1^E(y0)))) = 0 
        ys = E1(ys+1^...E(yn)) ^ E(ys-1^...E(y1^E(y0)))
        """
        # $y_s = E_k^{-1} \left( y_{s+1} \oplus \dots E_k^{-1} \left( y_n \oplus E_k^{-1} \left(z\right)\right)\dots\right) \oplus E_k \left( y_{s-1} \oplus \dots E_k \left( y_1 \oplus v \right)\dots\right)$
        self.permut(msg)
        x,y = [],[]
        for i in range(len(self.kl)):
            if i != s:
                xi = random.randint(0,2**self.l-1)
                x.append(xi)
                y.append(self.trap(xi,self.kl[i].e,self.kl[i].n))
        vi = reduce (lambda vi,i:self.E(i^vi),y[s:],0)
        yc = reduce (lambda yc,i:self.E(i^yc),y[:s],vi)
        x.insert(s,self.trap(yc,self.kl[s].d,self.kl[s].n))
        return itob64(vi) + ' ' + ' '.join('%s'%itob64(xi) for xi in x)

    def verify(self,msg,X):
        """ E(yn....^E(y2^E(y1^E(y0)))) =? vi """
        # $y_s = E_k^{-1} \left( y_{s+1} \oplus \dots E_k^{-1} \left( y_n \oplus E_k^{-1} \left(z\right)\right)\dots\right) \oplus E_k \left( y_{s-1} \oplus \dots E_k \left( y_1 \oplus v \right)\dots\right)$
        self.permut(msg)
        x = []
        for xi in X.split(): x.append(b64toi(xi))
        Y = map(lambda i,j:self.trap(i,j.e,j.n),x[1:],self.kl)
        return reduce (lambda x,y:self.E(x^y),Y,x[0]) == x[0]

class ringBL(ring):
    """ 
    Improved Ring Signature with linkability
    """
    # see \cite{Liu01}
    def sign(self,msg,s): 
        """
        Find ys such that E(yn....^E(y2^E(y1^E(y0)))) = 0 
        ys = E1(ys+1^...E(yn)) ^ E(ys-1^...E(y1^E(y0)))
        """
        # $y_s = E_k^{-1} \left( y_{s+1} \oplus \dots E_k^{-1} \left( y_n \oplus E_k^{-1} \left(z\right)\right)\dots\right) \oplus E_k \left( y_{s-1} \oplus \dots E_k \left( y_1 \oplus v \right)\dots\right)$
        root_link,limit = 1234567,56 # find a more secure root and an optimal limit!
        link = itob64(pow(root_link,self.kl[s].p + self.kl[s].q,self.kl[s].n)%(1<<limit))
        #link = itob64(1000000L) easy to tally !
        self.permut(msg + link)
        x,y = [],[]
        for i in range(len(self.kl)):
            if i != s:
                xi = random.randint(0,2**self.l-1)
                x.append(xi)
                y.append(self.trap(xi,self.kl[i].e,self.kl[i].n))
        vi = reduce (lambda vi,i:self.E(i^vi),y[s:],0)
        yc = reduce (lambda yc,i:self.E(i^yc),y[:s],vi)
        x.insert(s,self.trap(yc,self.kl[s].d,self.kl[s].n))
        return link + ' ' + itob64(vi) + ' ' + ' '.join('%s'%itob64(xi) for xi in x)

    def verify(self,msg,X):
        """ E(yn....^E(y2^E(y1^E(y0)))) =? vi """
        # $y_s = E_k^{-1} \left( y_{s+1} \oplus \dots E_k^{-1} \left( y_n \oplus E_k^{-1} \left(z\right)\right)\dots\right) \oplus E_k \left( y_{s-1} \oplus \dots E_k \left( y_1 \oplus v \right)\dots\right)$
        x = []
        self.permut(msg + X.split()[0])
        for xi in X.split(): x.append(b64toi(xi))
        Y = map(lambda i,j:self.trap(i,j.e,j.n),x[2:],self.kl)
        return reduce (lambda x,y:self.E(x^y),Y,x[1]) == x[1]

class dsa:
    """ DSA signature """
    # see ...
    def __init__(self,pkey,skey=None):
        # genkeys TODO!
        g = 3 # TODO
        # Choisir un nombre premier p de Lec 512 ≤ L ≤ 1024, et L est divisible par 64
        p = 13 # TODO
        lp = len(bin(p)[2:])
        # Choisir un nombre premier q de 160 bits, tel que p−1=qz, z entier
        q = 7 # TODO 
        lq = len(bin(q)[2:])
        # Choisir h, avec 1 < h < p−1 tel que g=h^z mod p > 1
        h = 11 # TODO
        x = random.randint(0,q)
        y = pow(g,x,p)
        # til use outside keys
        self.sk,self.pk = skey,pkey

    def sign(self,msg):
        """ x private key """
        s0 = random.randint(3,self.pk.q-1)
        s1 = pow(self.pk.g,s0,self.pk.p)%self.pk.q
        s22 = (int(hashlib.sha1(msg).hexdigest(),16) + s1*self.sk.x)%self.pk.q
        s2 = (s22*rev_mod(s0,self.pk.q))%self.pk.q
        return [itob64(s1),itob64(s2)]

    def verify(self,msg,X):
        """ y,g,p,q public """
        print 'G %s'%self.pk.g
        print 'P %s'%self.pk.p
        print 'Q %s'%self.pk.q
        s1,s2 = b64toi(X[0]),b64toi(X[1])
        w = rev_mod(s2,self.pk.q)
        u1,u2 = (int(hashlib.sha1(msg).hexdigest(),16)*w)%self.pk.q, (s1*w)%self.pk.q
        return ((pow(self.pk.g,u1,self.pk.p)*pow(self.pk.y,u2,self.pk.p))%self.pk.p)%self.pk.q == s1

class rsa:
    """ RSA signature and encryption
    Usage: k is a public key, S is the signature
      a = rsa.ring(k)
      S = a.sign('hello world!') 
      assert a.verify('hello world!',S)
    """
    # see ...
    def __init__(self,kl,salt=64,l=1024):
        """ Set public keys, RSA size """
        self.kl,self.s,self.l = kl,salt,l
            
    def sign(self,msg):
        """ Signature """
        # $s = H(msg)^{d} mod n$ 
        h = msg.encode('hex') if len(bin(self.kl.n)) < 162 else hashlib.sha1(msg).hexdigest()
        assert len(h) <= len(bin(self.kl.n))//4
        return itob64(pow(int(h,16),self.kl.d,self.kl.n))

    def verify(self,msg,x):
        """ Verification """
        # $msg^{e} mod n \equiv H(msg)$
        h = msg.encode('hex') if len(bin(self.kl.n)) < 162 else hashlib.sha1(msg).hexdigest()
        return int(h,16) == pow(b64toi(x),self.kl.e,self.kl.n) 

    def encrypt(self,num):
        """ input num should be long integer! """
        assert len(bin(num)) <= len(bin(self.kl.n))-self.s
        return itob64(pow(random.randint(0,(1<<self.s)-1)+(num<<self.s),self.kl.e,self.kl.n))

    def decrypt(self,encr):
        """ output is also integer """
        return pow(b64toi(encr),self.kl.d,self.kl.n)>>self.s 

class elgamal:
    """ ElGamal encryption """
    # see ...
    def __init__(self):
        """ keygen """
        k = Crypto.PublicKey.ElGamal.generate(1024,os.urandom)
        self.x, self.p, self.g = k.x, k.publickey().p, k.publickey().g
        self.y = pow(self.g, self.x, self.p)

    def encrypt(self,m):
        """ """
        r = random.randint(0,self.p-2)
        return pow(self.g, r, self.p),(m*pow(self.y, r, self.p))%self.p

    def decrypt(self,c):
        """ """
        return (c[1]*rev_mod(pow(c[0], self.x, self.p), self.p))%self.p

def getd(da):
    """ """
    d = '/ts'
    dbf = '%s/oeu.db'%d # keep private !
    if not os.path.isdir(d):
        os.mkdir(d)
    if not os.path.isfile(dbf):
        db = dbhash.open(dbf,'c')
        k = Crypto.PublicKey.RSA.generate(1024,os.urandom)
        db['_'] = '%s'%[itob64(k.n),itob64(k.d)]
        db.close()
        return ''
    if not da:
        db = dbhash.open(dbf,'c')
        a = eval(db['_'])
        db.close()
        return a[0] 
    t,df,d1 = [None,None,None],'',None
    try:
        d1 = datetime.datetime.strptime(da,'%Y-%m-%d')
        df = d1.strftime('%Y-%m-%d')
    except:
        return ''
    db = dbhash.open(dbf,'w')
    if db.has_key(df):
        t = eval(db[df])
    else:
        k = Crypto.PublicKey.RSA.generate(1024,os.urandom)
        a = eval(db['_'])
        stprk = myKey(b64toi(a[0]),b64toi(a[1]))
        si = rsa(stprk).sign(df)
        t = [itob64(k.n),itob64(b64toi(si)^k.d),si]
        db[df] = '%s'%t
    db.close()
    return '%s'%(t[:-1] if datetime.datetime.now()-d1 < datetime.timedelta() else t)

def application(environ,start_response):
    """ TimeStamp Web application (for 2010-2019 decade only)"""
    start_response('200 OK',[('Content-type','text/plain')])
    return [getd(reg.v.group(1) if reg(re.search(r'd=(201\d\-\d{2}\-\d{2})$',urllib.unquote(environ['QUERY_STRING']))) else '')] 

#def update():
#    """ update file digest if changed"""
#    with open(__file__) as f:
#        l = list(f)
#        if '#%s\n'%hashlib.sha1('%s'%l[:-1]).hexdigest() != l[-1]:
#            open(__file__,'a').write('#%s\n'%hashlib.sha1('%s'%l).hexdigest())
#            print '...digest updated'

def get_list_voters(n):
    li = {}
    for x in range(n):
        li[itob64(int(hashlib.sha1('%d'%x).hexdigest()[:10],16))] = ''
    return li

def get_test_list_voters():
    return {'Alice':   '21 Place du Capitole 31000 Toulouse France',
            'Bob':     '24 Rue des Paradoux 31000 Toulouse France',
            'Robert':  '23 Avenue des Champs Elysées 75000 Paris France',
            'Carol':   '17 Place Colbert 69000 Lyon France',
            'Oscar':   '22 Rue Arago 31000 Toulouse France',
            'Eve':     '22 Rue Jean Jaures 31000 Toulouse France',
            'Mallory': '13 Rue Grognard 69000 Lyon France',
            'Trudy':   '12 Places aux Herbes 38000 Grenoble France',
            'Isaac':   '17 Place du Capitole 31000 Toulouse France',
            'Arthur':  '26 Rue Chappet 69000 Lyon France',
            'Merlin':  '87 Place de la Comédie 33000 Bordeaux France',
            'Peggy':   '19 Place de Jaude 63000 Clermont-Ferrand France',
            'Me':      '2  Bis Avenue de Mons 31280 Flourens France'}


def export_pdf(p):
    """ """
    if Popen(('which','pdflatex'),stdout=PIPE).communicate()[0]:
        Popen(('cd /tmp; pdflatex -interaction=batchmode %s 1>/dev/null'%os.path.abspath(p)), shell=True).communicate()
        name = os.path.basename(p)[:-4]
        shutil.move('/tmp/%s.pdf'%name,'%s.pdf'%p[:-4]) 
    else:
        print 'pdflatex not installed!'

def test():
    """ ring test """
    #num,z = 12345678,elgamal()
    #assert num == z.decrypt(z.encrypt(num))
    #z = rsa(Crypto.PublicKey.RSA.importKey(open('keys/Alice.pem').read()))
    #for i in range(10):
    #    enc = z.encrypt(i)
    #    print i, enc, z.decrypt(enc)

    IK = Crypto.PublicKey.RSA.importKey(open('keys/Alice.pem').read())
    msg = 2
    k0 = myKey(IK.n,IK.d,IK.e,1024)
    k1 = myKey(10,3,3,4)
    k2 = myKey(253,27,163,8)
    k3 = myKey(1073,1079,71,11)
    k4 = myKey(IK.n,IK.d)
    
    b1 = rsa(k4,34)
    s = b1.sign('A')
    #print s,b1.verify('A',s)

    s = b1.sign('A')
    #print s,b1.verify('A',s)

    #b = rsa(k3,2)
    #s = b.sign('A')
    #print s,b.verify('A',s)
    #print s,b.verify('B',s)

    k = Crypto.PublicKey.DSA.generate(1024, os.urandom)
    c = dsa(k.publickey(),k)
    for x in range(1):
        s = c.sign('A')
        #print 'DSA',s,c.verify('A',s)
    k = Crypto.PublicKey.DSA.generate(1024, os.urandom)
    c = dsa(k.publickey(),k)
    for x in range(1):
        s = c.sign('A')
        #print 'DSA',s,c.verify('A',s)

    #a = ring((k1,k2),8)
    #for i in range(len(kk)):
    #    s = a.sign(msg,i)
    #    print a.verify(msg,s)
    
    #enc = b.encrypt(msg)
    #print msg,b64toi(enc),b.decrypt(enc)
    #enc = b.encrypt(msg)
    #print msg,b64toi(enc),b.decrypt(enc)

    players,kk = get_players('list.txt'),[]
    for name in players.keys():
        kk.append(Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%name).read()))
    msg,msg1 = 'hello world!','hello world!x'
    a = ring(kk)
    for i in range(len(kk)):
        s = a.sign(msg,i)
        print len(s),a.verify(msg,s)
    a = ringB(kk)
    for i in range(len(kk)):
        s = a.sign(msg,i)
        #print a.verify(msg,s)
    b = ringBL(kk)
    for i in range(len(kk)):
        s = b.sign(msg,i)
        #print (s.split()[0],i,b.verify(msg,s),s[:30])
        s = b.sign(msg,i)
        #print (s.split()[0],i,b.verify(msg,s),s[:30])
    for i in kk:
        b = rsa(i)
        s = b.sign(msg)
        #print b.verify(msg,s)

def rand_prime(k=10):
    """ select random prime of k bits length """ 
    i = random.randint(2**(k-2),2**(k-1))
    i,l=2*i+1,0
    while True:
        j = 3
        l +=1
        while i%j!=0:
            j += 1
        if i == j:
            return i
            #return i,len(bin(i)[2:]),l
        i += 2

def gcd(x,y):
    i = x if x<y else y
    while i>1:
        if x%i == 0 and y%i == 0:
            return i
        i-=1
    return 1

def rev_mod(a,b):
    """ """
    r,r1,u,u1 = a,b,1,0
    while r1:
        q = r//r1
        rs,us = r,u
        r,u = r1,u1
        r1,u1 = rs - q*r1, us - q*u1
    return u

def rev_mod_extented(a,b):
    """ """
    r,r1,u,v,u1,v1 = a,b,1,0,0,1
    while r1:
        q = r//r1
        rs,us,vs = r,u,v
        r,u,v = r1,u1,v1
        r1,u1,v1 = rs - q*r1, us - q*u1, vs -q*v1
    return u

def create_pdf(f,s1,s2='',s3=''):
    # does not need reportlab!
    """%PDF-1.\n1 0 obj<</F1 2 0 R>>endobj 2 0 obj<</BaseFont/Helvetica/Encoding/WinAnsiEncoding/Name/F1/Subtype/Type1/Type/Font>>endobj 3 0 obj<</Contents 7 0 R/MediaBox[0 0 421 298]/Parent 6 0 R/Resources<</Font 1 0 R/ProcSet[]>>/Type/Page>>endobj 4 0 obj<</PageMode/UseNone/Pages 6 0 R>>endobj 6 0 obj<</Count 1/Kids[3 0 R]/Type/Pages>>endobj 7 0 obj<</Filter[/FlateDecode]"""
    if s1 == 'White Ballot': s1 = '"'+'_'*10+'"'
    cod = zlib.compress('BT /F1 16 Tf ET\r\nBT 300 270 Td (%s) Tj ET\r\nBT /F1 48 Tf ET\r\nBT 5 180 Td (%16s) Tj ET\r\nBT /F1 12 Tf ET\r\nBT 10 50 Td (%s) Tj ET'%(s3,s1,s2))
    open(f,'w').write(create_pdf.__doc__ + '/Length %d>>\nstream\n'%len(cod) + cod + 'endstream endobj\ntrailer<</Root 4 0 R>>')
    
def extract_txt_from_pdf(f):
    """ """
    start,tot,size = False,'',0
    for l in open(f).readlines():
        m = re.search('Length\s(\d+)',l)
        if m:
            size = int(m.group(1))
        m1 = re.match('(.*)endstream',l)
        if m1:
            tot += m1.group(1)
            start = False
        elif start:
            tot += l
        elif re.match('stream',l):
            start = True
    raw = zlib.decompress(tot)
    res = []
    for l in raw.split('\n'):
        m = re.search('Td\s\(\s*([^\)]+)\)\sTj',l)
        if m:
            res.append(m.group(1))
    return res

def create_ballots(box,I,z):
    IKey = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%I).read())
    lcand,name = ['White Ballot',],''
    for l in open(box).readlines():
        if re.match(r'\(',l):
            name,h,n,d1,d2,url = eval(l)
        elif re.match(r'\{',l):
            lcand += eval(l).keys()
    for c in lcand:
        create_pdf(re.sub(r'\s','_',c+'.pdf'),c,z,name) 
        #print extract_txt_from_pdf(re.sub(r'\s','_',c+'.pdf'))

def gen_keys(lname,dsa=False):
    """ generate PEM format rsa keys """
    d = 'keys'
    if not os.path.isdir(d):
        os.mkdir(d)
    for n in lname:
        if not os.path.isfile('%s/%s.pem'%(d,n)):
            key = Crypto.PublicKey.DSA.generate(512, os.urandom) if dsa else Crypto.PublicKey.RSA.generate(1024,os.urandom)
            open('%s/%s.pem'%(d,n),'w').write(key.exportKey('PEM')) 

def validate(box,lid,dsgnk,sig,progress=0):
    """ returns 28 error types and build a valid box if not exists"""
    digest = hashlib.sha1(open(__file__).read()).hexdigest()
    dsgn_ok,lastlM,smallringsize,maxi_nreg, = False,0,__smallringsize__,1000
    name,num = '',0
    state,mngrk,tsprk,d1s,d2s,nreg,nvot,rev,fullring,myregs,res = preSt,None,None,[],[],0,0,{},[],[],{}
    lcand = ['White Ballot',]
    if os.path.isfile(box):
        i,current,seen1,seen_link,d1,d2,dt1,dt2,lcrypted = 0,'',{},{},'','',None,None,[]
        for l in open(box).readlines():
            if i == 0 and reg(re.match(r'OEvote\s([a-f\d]+)\s*$',l)):
                if not reg.v.group(1) == digest[:10]:
                    #print 'oeu digest should be %s'%digest[:10]
                    return 1,'oeu digest should be %s'%digest[:10]
            elif i == 1 and re.match(r'\(',l):
                name,ha,num,d1,d2,url = eval(l)
                tsprk = urllib.urlopen(url).read()
                d1s = eval(urllib.urlopen(url+'?d='+d1).read())
                d2s = eval(urllib.urlopen(url+'?d='+d2).read())
                if len(d1s) == 3:
                    assert rsa(myKey(b64toi(tsprk))).verify(d1,d1s[2])
                if len(d2s) == 3:
                    assert rsa(myKey(b64toi(tsprk))).verify(d2,d2s[2])
                ekeys = d2s
                dt1,dt2 = datetime.datetime.strptime(d1,'%Y-%m-%d'),datetime.datetime.strptime(d2,'%Y-%m-%d')
                if re.match(r'[\w ]{3,40}$',name):
                    if ha != h2b64(hashlib.sha1(name).hexdigest()[:10]):
                        return 2,'election name digest should be %s'%h2b64(hashlib.sha1(name).hexdigest()[:10])
                else:
                    return 3,'bad election name'
                if int(num) < 0 or int(num) > (1<<30): # 10^9 maxi!
                    return 4,'bad box number'
                if dt2-dt1 < datetime.timedelta(days=31):
                    return 5,'duration two short %s %s'%(d1,d2)
            elif i == 2 and re.match(r'\{',l):
                cands = eval(l)
                if len(cands.keys()) > 20:
                    return 6,'too many candidates'
                for c in cands:
                    if re.search(r'(white|blanc|ballot|bulletin|nul)',c,re.I):
                        return 7,'\'%s\' forbidden name'%c
                    if len(cands[c]) > 20:
                        return 8,'\'%s\' attribute too long'%cand[c]
                lcand += cands.keys()
                for x in lcand: res[x] = 0
            elif i == 3 and re.match(r'%\s[\w\-]{10,200}$',l):
                mngrk = l[2:-1]
            elif reg(re.match(r'@\s([\w\-]{10,200})$',l)):
                if mngrk:
                    if lastlM == i-1:
                        return 9,'Manager signature on two consecutive lines'
                    lastlM = i
                    if state == preSt:
                        state = regSt
                    if not rsa(myKey(b64toi(mngrk))).verify(current,reg.v.group(1)):
                        return 10,'wrong manager signature'
                else:
                    return 11,'bad or unknown manager key' 
            elif state == preSt and reg(re.match(r'~\s([\w\-]{10,200})$',l)):
                if not dsgn_ok:
                    dsgn_ok = True
                    if not rsa(myKey(b64toi(dsgnk))).verify(name,reg.v.group(1)):
                        return 12,'wrong designer signature'
                else:
                    return 13,'already signed by designed' 
            elif state == regSt and reg(re.match(r'\;([\w\-]{10,200})$',l)):
                myregs.append(reg.v.group(1))
            elif state == regSt and reg(re.match(r'\.([\w\-]{10})\s(\d{0,10})\s([\w\-]{10,200})\s([\w\-]{10,200})$',l)):
                nreg += 1
                if nreg >= maxi_nreg:
                    return 14,'too many registered'%(i+1)  
                else:
                    if seen1.has_key(reg.v.group(1)):
                        return 15,'id already used %s'%reg.v.group(1)
                    else:
                        seen1[reg.v.group(1)] = True
                    fullring.append(myKey(b64toi(reg.v.group(3))))
                    pos = int(reg.v.group(2))
                    if pos < len(myregs):
                        if not rsa(myKey(b64toi(mngrk))).verify('%d_%s_%d'%(pos,name,num),reg.v.group(1)+myregs[pos]):
                            return 16,'wrong signed id'
                        if not rsa(myKey(b64toi(reg.v.group(3)))).verify(reg.v.group(1),reg.v.group(4)):
                            return 17,'bad registered signature'
                    else:
                        return 18,'bad index %s %s'%(pos,len(myregs))
            elif len(d1s) and reg(re.match(r'!([\w\-]{2,100})\s([\w\-]{100,200})\s(.+)$',l)):
                state = votSt
                link = reg.v.group(3).split()[0]
                if seen_link.has_key(link):
                    return 19,'multiple vote not allowed'
                else:
                    seen_link[link] = True
                smallring = fullring if reg.v.group(1) == 'None' else getsample(fullring,reg.v.group(1),smallringsize)
                if smallring == None:
                    return 20,'small ring shall include differents public keys'
                if ringBL(smallring).verify(reg.v.group(2),reg.v.group(3)):
                    nvot += 1
                    lcrypted.append(reg.v.group(2))
                else:
                    return 21,'bad vote signature'
            elif reg(re.match(r'\$\s(\d+)\/(\d+)\s+(\{.*)$',l)): 
                state = cloSt
                res,res1,tot = eval(reg.v.group(3)),{},0
                for x in res.keys():
                    tot += res[x] 
                if len(d2s) == 3:
                    for x in lcand: res1[x] = 0
                    for y in lcrypted:
                        res1[itos(rsa(myKey(b64toi(d2s[0]),b64toi(d2s[1])^b64toi(d2s[2]))).decrypt(y))] += 1
                    if res != res1:
                        return 22,'bad result'
                else:
                    return 23,'no timestamp signature'
                if nreg != int(reg.v.group(2)) or nvot != int(reg.v.group(1)) or tot != nvot:
                    return 24,'bad tally'
            else:
                return 25,'bad line %s state %s'%((i+1),state)     
            i += 1
            current += l
        if rev:
            return 26,'need revocation of %s'%rev.keys()
        if mngrk == tsprk or mngrk == dsgnk or tsprk == dsgnk:
            return 27,'manager, designer and timestamper should be different'
        if not dsgn_ok:
            return 28,'missing designer signature'
        if lastlM + 1 != i:
            return 29,'missing end manager signature'            
    else:
        name,num,url = 'Poll Test',1234,'http://localhost/oeu'
        d1,d2 = datetime.datetime(2011,1,1).strftime('%Y-%m-%d'),datetime.datetime(2011,5,21).strftime('%Y-%m-%d')
        cand = {'Marcel Dupond':'AXT', 'Joe Smith':'BZM', 'David Cohen':'CPZ', 'Bob Ryan':'DBS', 'Carol Wu':'EIC'}
        lcand = cand.keys()+['White Ballot',]
        for x in lcand: res[x] = 0
        o = "OEvote %s\n('%s', 'jbve4R0', %d, '%s', '%s','%s')\n%s\n"%(digest[:10],name,num,d1,d2,url,cand)
        gen_keys(('manager','stamper','election'))
        MngrKey = Crypto.PublicKey.RSA.importKey(open('keys/manager.pem').read()) 
        o += '%% %s\n~ %s\n'%(itob64(MngrKey.publickey().n),sig)
        o += '@ %s\n'%rsa(MngrKey).sign(o)
        lv = get_list_voters(100)
        gen_keys(lv.keys())
        seen,i,nreg,nvot = {},0,len(lv.keys()),len(lv.keys())
        for x in lv.keys():
            idk = rsa(MngrKey).sign('%d_%s_%d'%(i,name,num))
            seen[idk[:10]] = (x,i)
            o += ';%s\n'%(idk[10:])
            i += 1
        open(lid,'w').write('%s'%seen)
        o += '@ %s\n'%rsa(MngrKey).sign(o)
        if progress == 0 or progress == 1:
            for z in seen.keys():
                k = Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%seen[z][0]).read()) 
                o += '.%s %03d %s %s\n'%(z,seen[z][1],itob64(k.n),rsa(k).sign(z))
            o += '@ %s\n'%rsa(MngrKey).sign(o)
        if progress == 0:
            for x in lv.keys():
                fullring.append(Crypto.PublicKey.RSA.importKey(open('keys/%s.pem'%x).read()))
            lcrypted = []
            d1s = eval(urllib.urlopen(url+'?d='+d1).read())
            d2s = eval(urllib.urlopen(url+'?d='+d2).read())
            for i in range(len(lv.keys())):
                crypted = rsa(myKey(b64toi(d2s[0]))).encrypt(b64toi(base64.urlsafe_b64encode(random.choice(lcand))))
                lcrypted.append(crypted)
                pos,lind = setsample(len(fullring),i,smallringsize)
                smallring = getsample(fullring,lind,smallringsize) if lind else fullring
                o += '!%s %s %s\n'%(lind,crypted,ringBL(smallring).sign(crypted,pos))    
            for i in lcrypted:
                res[itos(rsa(myKey(b64toi(d2s[0]),b64toi(d2s[1])^b64toi(d2s[2]))).decrypt(i))] += 1
            o += '$ %s/%s %s\n'%(nvot,nreg,res)
            o += '@ %s\n'%rsa(MngrKey).sign(o)
        open(box,'w').write(o)
        print 'creates \'box.txt\' for progress %d'%progress
        return
    return 0,name,num,d1,d2,state,nreg,nvot,res

def setsample(z,k,n):
    """ returns sampling of n elements from list size z with the element in position k, all differents and sorted"""
    if n >= z:
        return k,None
    x = range(z)
    x.remove(k)
    x = random.sample(x,n-1)
    x.append(k)
    x.sort()
    y,p = [],-1
    for i in x:
        y.append(i-p-1)
        p = i
    return x.index(k),btob64(struct.pack('%dB'%n,*(i for i in y)))

def getsample(r,u,n):
    """ """
    x,p,seen = [],-1,{}
    for i in struct.unpack('%dB'%n,b64tob(u)):
        p += i+1 
        if seen.has_key(p):
            return None
        seen[p] = True
        x.append(r[p])
    return x

def reg(value):
    """ function attribute is a way to access matching group in one line test """
    reg.v = value
    return value

if __name__ == '__main__':
    """ test """
    #print 'Running test:\n...wait!'
    opts, args = getopt.getopt(sys.argv[1:], 'htdi:v:', ['help', 'id=','register='])
    for r in opts:
        if r[0] in ('-h','--help'):
            help(os.path.basename(sys.argv[0])[:-3])
        if r[0] in ('-r','--register'):
            pass
    #test()

    name = 'Poll Test'
    mypubkey = 'oF8IxWaWWMt6TMcTu9Tyrkft7kFn-_7HlavugMMxUSLmacaNW1bQuQ4BKjPOf7HI_pzTHoteWalqRg9Mj4PCLu15y57PfplJC0lEnpu_JqyyZlC777YV8Mf3DTmXLnqObNbb6229U98cypVFlOEOsezqC7LrH_7rGY2y7_TsPL8'
    sig = 'UDK9V_JSfCBG-CjsNaVqO1KmwF36aKoaPCzW50NwfC_xx-IAN2vIteiXv4YYNexxLSueEHBImOxAHgk1nHRrNBZzUFRKVRqbl0I8KwDWOt9GaJtMG6I3HN_DZcKpJYAMmtGYucVqDF68FnKto0kPMRlPT-FzlPKp5AXN59fY1WQ'

    digest,box = hashlib.sha1(open(__file__).read()).hexdigest(),'box.txt'
    #if not reg.v.group(1) == digest[:10]:
    
    progress = 0
    res = validate(box,'id.txt',mypubkey,sig,progress)
    if res: 
        if res[0] == 0:
            print 'Building documentation:' 
            make_document(box,digest,res)
            make_readme(digest)
            make_apache(digest)
        else:
            print 'error on \'%s\' file; %s %s'%((box,)+res)
    else:
        if progress == 2:
            register(box,'s39t3O8','Wb_HUk1JbR')
            approve(box,'manager')
            cast(box,'s39t3O8','White Ballot')
            tally(box)
            approve(box,'manager')
        elif progress == 1:
            cast(box,'kQnIWkU','Joe Smith')
            cast(box,'s39t3O8','White Ballot')
            if len(sys.argv) == 2:
                if os.path.isfile(sys.argv[1]):
                    if re.search('\.pdf$',sys.argv[1]):
                        if os.path.getsize(sys.argv[1]) < 550:
                            cont = extract_txt_from_pdf(sys.argv[1])
                            if is_good_race(box,mypubkey,cont[0]):
                                cast(box,'Me',cont[1])
                                # request password
            tally(box)
            approve(box,'manager')
    raw_input('press enter to close ...')
# end

