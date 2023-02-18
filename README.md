# CSCE5290-NLPProject



# Title: Vulnerability Explanation using NLP

Github Project: [https://github.com/neffer77/CSCE5290-NLPProject](https://github.com/neffer77/CSCE5290-NLPProject)

Team Members: Connor Neff


# Motivation

In a software company there is a dependency between developers and security analysts when creating fixes for security issues on the product. Developers often depend on security analysts to explain what is wrong with the code, what could happen if the code is not fixed, and what is the best recommendation to fix the issue. Meanwhile, Security Analysts rely on developers to implement a fix in the code,  and ensure the existing functionality works with the security recommendation.

Often times there is a gap in knowledge between security analysts and developers. When Developers receive an issue from the Security Organization, they may not understand why there is an issue with the specific code. The motivation of this project is to simplify that process of explanation. 

Automating this process using NLP will help reduce the time it takes to create these extensive write ups as well as increase the accuracy and comprehension.


# Objective

Develop a system which can provide an explanation of the vulnerability to a developer. The explanation should be easy for a non-expert to understand and actionable to help implement a code fix. The user input would be a segment of vulnerable Java code. The output would be a text summarization of the issue, the impact of the issue, and translate the input code to give a recommendation on how to fix the issue. 


# Significance

Write ups for security analysts is a time consuming and laborious process. You are tasked with explaining an issue to a developer in a succinct way when you spent hours of time researching the issue.  In Addition, each security vulnerability is unique enough that generic templates do not work each time since the vulnerability root cause and specifics to exploit it are different each time. 

Security analysts can also often make assumptions about prior knowledge that a developer may not have. This can lead to confusion and the ensuing back and forth can sometimes take weeks to correct.

Having a common understanding can help fix issues faster, reduce rework for developers, and reduce security risk since they will get the fix done correctly the first time. 


# Features

This project will be broken down into 3 different features:



1. Text Classification

    The AI will take a Java code snippet as user input. From that, it will classify what type of vulnerability it is based off of keywords used in the code such as functions and the logic structure of the code. In order to understand the logic of the code, the AI must also parse the code into an Abstract Syntax Tree (AST). This will allow the AI to understand the vulnerable code from start to finish and look for potential logic errors. Currently it is unknown whether a user will need to submit a full class to produce an AST or whether the User intake process can accommodate for that. 


    

<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")



    Figure 1: Example Vulnerable Code that would be submitted. Instance of a relative path traversal vulnerability. [Source](https://samate.nist.gov/SARD/test-cases/134160/versions/1.0.0)

2. Text Summarization

    Once the AI has determined the vulnerability class, it will create a text summarization of the issue. It is important for the summary to contain a general overview of the issue as well as specific examples in the code to give more context. The summary will be produced in English. 


    

<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")



        Figure 2: Example code summary. Summarizes the method ‘equals’. [Source](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/Method.html#equals-java.lang.Object-)

3. Machine Translation

    Finally the AI will take the summary and user Java code input and translate that into potential impacts and recommended remediation. The remediation should include possible functions the developer could use or changes to the code to produce a fix. 




<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")


Figure 3. Example of Remediation. Give specific advice to developers on how to fix an issue. [Source](https://cwe.mitre.org/data/definitions/79.html).


# Resources

Works Cited


    Clement, Colin, et al. _PYMT5: Multi-Mode Translation of Natural Language and PYTHON Code with Transformers_.


    “Collection of Datasets for Vulnerability Prediction.” _GitHub_, 15 Feb. 2023, github.com/TQRG/security-patches-dataset. Accessed 18 Feb. 2023.


    Evangelista, Johnathan. “Cybersecurity Vulnerability Classification Utilizing Natural Language Processing Methods - ProQuest.” _Www.proquest.com_, 31 Aug. 2021, www.proquest.com/docview/2572603776?pq-origsite=gscholar&fromopenview=true. Accessed 18 Feb. 2023.


    _Literature Review on Vulnerability Detection Using NLP Technology_. 2021.


    “NIST Software Assurance Reference Dataset.” _NIST Software Assurance Reference Dataset_, samate.nist.gov/SARD. Accessed 18 Feb. 2023.


    “Secure Coding Guidelines for Java SE.” _Oracle.com_, 2019, www.oracle.com/java/technologies/javase/seccodeguide.html.


    Shamim, Hafiza Iqra, and Asghar Ali Shah. “Automated Vulnerability Detection for Software Using NLP Techniques.” _Journal of Information Communication Technologies and Robotic Applications_, 30 Dec. 2021, pp. 48–57, jictra.com.pk/index.php/jictra/article/view/272/140, https://doi.org/10.51239/jictra.v0i0.272. Accessed 18 Feb. 2023.
