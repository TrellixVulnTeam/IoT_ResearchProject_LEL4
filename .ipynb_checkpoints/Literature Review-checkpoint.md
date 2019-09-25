

# Convenience-Based Periodic Composition of IoT Services @
@article{huang2018}

## Abstract
_We propose a novel service mining framework to personalize services in an IoT based smart home. We describe a new technique based on the concept ofconvenienceto discover periodic composite IoTservices to suit the smart home occupant’s convenience needs. The keyfeatures of convenience is the ability to model the spatio-temporal aspects as occupants move in time and space within the smart home. We propose a novel framework for the transient composition of spatio-temporal IoT service. We design two strategies to prune non-promising compositions. Specifically, a significance model is proposed to prune insignificant com-posite IoT services. We describe a spatio-temporalproximitytechniqueto prune loosely correlated composite IoT services. A periodic composite IoT service model is proposed to model theregularityof composite IoT services occurring at a certain location in a given time interval. The experimental results on real datasets show the efficiency and effectiveness of our proposed approach._

## Objective 
Propose a novel service mining framework to personalize services in an IoT-based smart home. Using this framework, IoT services can be composed in a periodic fashion, for the convenience of the end user / consumer.
* Use intelligence to compose IoT services for the convenience of the end user / consumer

## Domain
IoT service, high-level intelligence in smart homes, Service composition, Spatial and temporal correlation, Service Mining

## Input
Data from domestic IoT services (with corresponding timestamp for usage)

## Technology
IoT, Sensors, Periodic Composite IoT Service Miner (PCMiner)

## Output

1. An IoT service model and a composite IoT service model (based on spatio-temporal features)
2. A significance model – to prune insignificant composite IoT services
3. A periodic composite IoT service model to represent the regularity of composite IoT services occuring at a certain location at a certain time interval
4. A convenience model, to measure the benefits of applying periodic composite IoT services
5. A novel PCMiner algorithm (Periodic Composite IoT Service Miner) 

* Significance model (prune insignificant composite IoT services)
* patterns (useage data) can be used to design intelligent control of IoT services in smart homes to reduce residents’ interactions with IoT services
* Reducing such interactions provides more convenience for residents / end users

## Notes

* Talk about quantification – e.g., quantify convenience (???)
* The traditional Web of Data is tranforming into a Web of Semantic Data and Services
* Not only data, but also now services can be mined
* Previous work in service mining has centered around the identification / composition of potentially interesting and useful services
* Huang et al, propose a novel service mining framework based on the concept of convenience via periodic composition 
* A fundamental task to provide convenience is to augment IoT services with capabilities of understanding the periodic usage of composite IoT services
* ‘End User’ performs daily activities by interacting with IoT services, these interactions are recorded as IoT service event sequences
Key Points
* The internet is evolving from interconnecting computers to interconnecting things
* Internet of Things (IoT) paradigm enables physical devices to connect and exchange information
* IoT devices allow objects to be sensed or controlled through the internet
* Key challenge = IoT devices are highly heterogeneous in terms of supporting infrastructure, ranging from networking to programming abstraction
* Service-oriented Computing (SOC) is a promising solution for abstracting things on the Internet as services by hiding the complex and diverse supporting infrastructure – this abstraction can shift the focus from dealing with technical details to how services are to be used
* A light connected to the internet = ‘a light service’
* Periodic composite IoT services can be loosely defined as the composite IoT services’ repeating occurrence at certain lications with regular time intervals
* Periodic composition of IoT services can provide 
* If an IoT service usage fails to follow its regular periodic composition, it could be a signal of abnormality
Questions
* At what point does intelligence take precedence over a pre-defined set of steps, for example, in an industrial / manufacturing process? Domestic patterns / behaviours ARE more dynamic than industry

---

# Service Mining on the Web @
@article{zheng2009}

## Abstract 
_The Web is transforming from a Web of data to a Web of both Semantic data and services. This trend is providing us with increasing opportunities to compose potentially interesting and useful services from existing services. While we may not sometimes have the specific queries needed in top-down service composition approaches to identify them, the early and proactive exposure of these opportunities will be key to harvest the great potential of the large body of Web services. In this paper, we propose a Web service mining framework that allows unexpected and interesting service compositions to automatically emerge in a bottom-up fashion. We present several mining techniques aiming at the discovery of such service compositions. We also present evaluation measures of their interestingness and usefulness. As a novel application of this framework, we demonstrate its effectiveness and potential by applying it to service-oriented models of biological processes for the discovery of interesting and useful pathways._ 

## Objective

## Domain
Service Mining, Service Recognition

## Input
Web Service Operation, 

## Technology
Service mining tool, Web Service Mining

## Output
Composed Web Services

## Notes

Web Service Composition
* Aims at providing value-added services through composing existing services
* Traditionally taken a ‘top-down’ approach
* Challenge: If the search terms are to specific the user may not be able to find an appropriate composed service
* ‘Bottom-up’ approach also possible
* E.g., Aim to discover any interesting and useful services with a general interest in Chinese medicine in mind, using a Service Mining Tool, may find – A service composition that takes as input a biological sample from a subject, determined the corresponding genome and the possible diseases the subject is predisposed to, and finally generates a list of treatment recommendation and/or life style suggestions.
* Bottom-up is ‘serendipidous’ in nature, has the ability of finding unexpected interesting and useful service compositions
* It is essential to be able to proactively discover opportunities for composing useful services, even when the goals are unspecified at the moment, or simply hard to imagine or unknown
* Much like the easy access to a glut of data has provided a fertile ground for data mining research, there is an expectation that an increase in Web services’ availability will also spur both the need and opportunities to break new ground on Web Services Mining
* We define Web Service Mining as a bottom-up search process aimed at the proactive discovery of potentially interesting and useful web services from existing services.
* Two Main Challenges
1. Combinatorial Explosion
2. Evaluation of interestingness and usefulness

---

# Why does real-time information reduce energy consumption? @

@article{lynham2016}

## Absract

 A number of studies have estimated how much energy conservation is achieved by providing households with real-time information on energy use via in-home displays. However, none of these studies tell us why real-time information changes energy-use behavior. We explore the causal mechanisms through which real-time information affects energy consumption by conducting a randomized-control trial with residential households. The experiment attempts to disentangle two competing mechanisms: (i) learning about the energy consumption of various activities, the “learning effect”, versus (ii) having a constant reminder of energy use, the “saliency effect”. We have two main results. First, we find a statistically significant treatment effect from receiving real-time information. Second, we find that learning plays a more prominent role than saliency in driving energy conservation. Our findings support the use of energy conservation programs that target consumer knowledge regarding the energy use of different devices and activities.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# White goods for white people? Drivers of electric appliance growth in emerging economies @

@article{rao2017}

## Absract

 Will everybody want and have a refrigerator, television and washing machine as incomes rise? Considerable uncertainty surrounds the likely increase in energy consumption and carbon emissions from rising incomes among the world's poor. We examine drivers of and predict appliance ownership using machine learning and other techniques with household survey data in India, South Africa and Brazil. Televisions and refrigerators are consistently preferred over washing machines. Income is still the predominant driver of aggregate penetration levels, but its influence differs by appliance and by region. The affordability of appliances, wealth, race and religion together, among other household characteristics, help explain the heterogeneity in appliance ownership at lower income levels. Understanding non-income drivers can be helpful to identify barriers to appliance uptake and to better forecast near term residential energy demand growth within countries.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Which electricity market design to encourage the development of demand response? @

@article{rious2015}

## Absract

Demand response is a cornerstone problem in electricity markets under climate change constraints. Most liberalized electricity markets have a poor track record at encouraging the deployment of smart meters and the development of demand response. In Europe, different models are considered for demand response, from a development under a regulated regime to a development under competitive perspectives. In this paper focusing on demand response and smart metering for mid-size and small consumers, we investigate which types of market signals should be sent to demand managers to see demand response emerge as a competitive activity. Using data from the French power system over nine years, we compare the possible market design options which would enable the development of demand response. Our simulations demonstrate that under the current market rules demand response is not a profitable activity in the French electricity industry. Introducing a capacity market could bring additional revenues to demand response providers and improve incentives to put in place demand response programs in a market environment.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---

# Web Service Mining, Application to Discoveries of Biological Pathways @

@article{zheng2010}

## Absract

The growing popularity of the Web and Web services has provided a great potential for a new research discipline, aka, Web service mining, as we have identified here. An effective service mining tool would allow potentially interesting and useful compositeWeb services to be discovered based on the availability of component services, rather than solely on human intuition or knowledge about the composability of these component services, as do traditional top down service composition approaches. We proposed a Web service mining framework that aims at the proactive discovery of interesting and useful service compositions. We also applied the framework to the discovery of useful pathways linking service-oriented models of biological processes. We summarize the main contributions of our research below.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Weather sensitivity in household appliance energy end-use @

@article{hart2004}

## Absract

Data from a Residential Energy Study (RES) were used to examine the weather sensitivity of various household appliances located in households within the Sydney metropolitan area. Thermal environmental indices effective temperature (ET∗), standard effective temperature (SET∗) and simple air temperature degree–days were used to quantify the dependence of household appliance energy consumption on outdoor weather. Specific appliances included: room air-conditioners, room heaters, refrigerators, freezers and domestic hot-water systems, all of which exhibited some degree of weather sensitivity, particularly space heating and cooling devices. Probit regression techniques were used to predict the degree–day values at which households tend to switch on heating and cooling appliances. All appliances demonstrated weather sensitivity to varying degrees, and this was universally stronger during the cooling season (summer) than during the heating season (winter). The outdoor SET∗ version of the degree–day index demonstrated a stronger statistical association with space-cooling energy consumption than conventional air temperature degree–days. The mean daily temperature associated with minimum heating and cooling energy consumption for Sydney indicated that a temperature of 18°C was the most appropriate base temperature for calculation of both heating and cooling degree–days.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Using smart meter data to estimate demand response potential, with application to solar energy integration @

@article{dyson2014}

## Absract

This paper presents a new method for estimating the demand response potential of residential air conditioning (A/C), using hourly electricity consumption data (“smart meter” data) from 30,000 customer accounts in Northern California. We apply linear regression and unsupervised classification methods to hourly, whole-home consumption and outdoor air temperature data to determine the hours, if any, that each home׳s A/C is active, and the temperature dependence of consumption when it is active. When results from our sample are scaled up to the total population, we find a maximum of 270–360MW (95\% c.i.) of demand response potential over a 1-h duration with a 4°F setpoint change, and up to 3.2–3.8GW of short-term curtailment potential. The estimated resource correlates well with the evening decline of solar production on hot, summer afternoons, suggesting that demand response could potentially act as reserves for the grid during these periods in the near future with expected higher adoption rates of solar energy. Additionally, the top 5\% of homes in the sample represent 40\% of the total MW-hours of DR resource, suggesting that policies and programs to take advantage of this resource should target these high users to maximize cost-effectiveness.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Use of Raman spectroscopy to screen diabetes mellitus with machine learning tools. @

@article{guevara2018}

## Absract

Type 2 diabetes mellitus (DM2) is one of the most widely prevalent diseases worldwide and is currently screened by invasive techniques based on enzymatic assays that measure plasma glucose concentration in a laboratory setting. A promising plan of action for screening DM2 is to identify molecular signatures in a non-invasive fashion. This work describes the application of portable Raman spectroscopy coupled with several supervised machine-learning techniques, to discern between diabetic patients and healthy controls (Ctrl), with a high degree of accuracy. Using artificial neural networks (ANN), we accurately discriminated between DM2 and Ctrl groups with 88.9-90.9\% accuracy, depending on the sampling site. In order to compare the ANN performance to more traditional methods used in spectroscopy, principal component analysis (PCA) was carried out. A subset of features from PCA was used to generate a support vector machine (SVM) model, albeit with decreased accuracy (76.0-82.5\%). The 10-fold cross-validation model was performed to validate both classifiers. This technique is relatively low-cost, harmless, simple and comfortable for the patient, yielding rapid diagnosis. Furthermore, the performance of the ANN-based method was better than the typical performance of the invasive measurement of capillary blood glucose. These characteristics make our method a promising screening tool for identifying DM2 in a non-invasive and automated fashion.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Unveiling Contextual Similarity of Things via Mining Human-Thing Interactions in the Internet of Things @

@article{yao2015}

## Absract

None

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Transactions on Computational Systems Biology III @

@article{cardelli2005}

## Absract

Living cells are extremely well-organized autonomous systems, consisting of discrete interacting components. Key to understanding and modeling their behavior is modeling their system organization. Four distinct chemical toolkits (classes of macromolecules) have been characterized, each combinatorial in nature. Each toolkit consists of a small number of simple components that are assembled (polymerized) into complex structures that interact in rich ways. Each toolkit abstracts away from chemistry; it embodies an abstract machine with its own instruction set and its own peculiar interaction model. These interaction models are highly effective, but are not ones commonly used in computing: proteins stick together, genes have fixed output, membranes carry activity on their surfaces. Biologists have invented a number of notations attempting to describe these abstract machines and the processes they implement. Moving up from molecular biology, systems biology aims to understand how these interaction models work, separately and together.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# The Short-Run and Long-Run Effects of Behavioral Interventions: Experimental Evidence from Energy Conservation @

@article{allcott2014}

## Absract

None

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# The question of energy reduction: The problem(s) with feedback @

@article{buchanan2015}

## Absract

With smart metering initiatives gaining increasing global popularity, the present paper seeks to challenge the increasingly entrenched view that providing householders with feedback about their energy usage, via an in-home-display, will lead them to substantially reduce their energy consumption. Specifically, we draw on existing quantitative and qualitative evidence to outline three key problems with feedback, namely: (a) the limited evidence of efficacy, (b) the need for user engagement, and (c) the potential for unintended consequences. We conclude by noting that, in their current form, existing in-home-displays may not induce the desired energy-reduction response anticipated by smart metering initiatives. Instead, if smart metering is to effectively reduce energy consumption there is a clear need to develop and test innovative new feedback devices that have been designed with user engagement in mind.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# The Pathway Tools software @

@article{karp2002}

## Absract

Motivation: Bioinformatics requires reusable software tools for creating model-organism databases (MODs). Results: The Pathway Tools is a reusable, production-quality software environment for creating a type of MOD called a Pathway/Genome Database (PGDB). A PGDB such as EcoCyc (see http://ecocyc.org) integrates our evolving understanding of the genes, proteins, metabolic network, and genetic network of an organism. This paper provides an overview of the four main components of the Pathway Tools: The PathoLogic component supports creation of new PGDBs from the annotated genome of an organism. The Pathway/Genome Navigator provides query, visualization, and Web-publishing services for PGDBs. The Pathway/Genome Editors support interactive updating of PGDBs. The Pathway Tools ontology defines the schema of PGDBs. The Pathway Tools makes use of the Ocelot object database system for data management services for PGDBs. The Pathway Tools has been used to build PGDBs for 13 organisms within SRI and by external users. Availability: The software is freely available to academics and is available for a fee to commercial institutions. Contact ptools-support@ai.sri.com for information on obtaining the software. Contact: pkarp@ai.sri.com Keywords: Bioinformatics; model organism database; genome analyses; metabolic pathways.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# The Internet of Things: A survey @

@article{atzori2010}

## Absract

This paper addresses the Internet of Things. Main enabling factor of this promising paradigm is the integration of several technologies and communications solutions. Identification and tracking technologies, wired and wireless sensor and actuator networks, enhanced communication protocols (shared with the Next Generation Internet), and distributed intelligence for smart objects are just the most relevant. As one can easily imagine, any serious contribution to the advance of the Internet of Things must necessarily be the result of synergetic activities conducted in different fields of knowledge, such as telecommunications, informatics, electronics and social science. In such a complex scenario, this survey is directed to those who want to approach this complex discipline and contribute to its development. Different visions of this Internet of Things paradigm are reported and enabling technologies reviewed. What emerges is that still major issues shall be faced by the research community. The most relevant among them are addressed in details.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# The evolving role of information technology in the drug discovery process @

@article{augen2002}

## Absract

Information technologies for chemical structure prediction, heterogeneous database access, pattern discovery, and systems and molecular modeling have evolved to become core components of the modern drug discovery process. As this evolution continues, the balance between in silico modeling and ‘wet’ chemistry will continue to shift and it might eventually be possible to step through the discovery pipeline without the aid of traditional laboratory techniques. Rapid advances in the industrialization of gene sequencing combined with databases of protein sequence and structure have created a target-rich but lead-poor environment. During the next decade, newer information technologies that facilitate the molecular modeling of drug–target interactions are likely to shift this balance towards molecular-based personalized medicine – the ultimate goal of the drug discovery process.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# The electricity generation adequacy problem: Assessing dynamic effects of capacity remuneration mechanisms @

@article{hary2016}

## Absract

Following liberalization reforms, the ability of power markets to provide satisfactory incentives for capacity investments has become a major concern. In particular, current energy markets can exhibit a phenomenon of investment cycles, which generate phases of under and over-capacity, and hence additional costs and risks for generation adequacy. To cope with these issues, new mechanisms, called capacity remuneration mechanisms (CRM), have been (or will be) implemented. This paper assesses the dynamic effects of two CRMs, the capacity market and the strategic reserve mechanism, and studies to what extent they can reduce the investment cycles. Generation costs and shortage costs of both mechanisms are also compared to conclude on their effectivity and economic efficiency. A simulation model, based on system dynamics, is developed to study the functioning of both CRMs and the related investment decisions. The results highlight the benefits of deploying CRMs to solve the adequacy issue: shortages are strongly reduced compared to an energy-only market. Besides, the capacity market appears to be more beneficial, since it experiences fewer shortages and generation costs are lower. These comparisons can be used by policy makers (in particular in Europe, where these two CRMs are mainly debated) to determine which CRM to adopt.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# The effect of appliance energy efficiency improvements on domestic electric loads in European households @

@article{borg2011}

## Absract

Across Europe domestic electricity consumption is on the rise. In an attempt to counter this increase, various initiatives have been introduced to promote the replacement of less energy-efficient appliances with more efficient ones. Whilst the likely aggregate effect of such measures over long time periods has been modelled extensively, little is known about the affect that a change to higher efficiency appliances will have on the electrical demand profile of individual households at higher temporal resolutions. To address this issue a means by which established approaches to detailed electrical demand modelling can be adapted to simulate the improvements in the efficiency of appliances is elaborated in this paper. A process is developed by which low-resolution empirical appliance demand data can be transformed to produce high-resolution electrical demand data for different periods in the year, factoring in improvements in appliance performance. The process is applied to simulate the effects a changeover to more energy-efficient appliances would have on the minute resolution demand profiles of a group of households. Results indicate that improving the energy-efficiency of appliances in households leads to a significant reduction in electrical energy requirements but does not appear to have a significant affect on the peak electrical demand.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# The 2nd DBCLS BioHackathon: interoperable bioinformatics Web services for integrated applications @

@article{katayama2011}

## Absract

The interaction between biological researchers and the bioinformatics tools they use is still hampered by incomplete interoperability between such tools. To ensure interoperability initiatives are effectively deployed, end-user applications need to be aware of, and support, best practices and standards. Here, we report on an initiative in which software developers and genome biologists came together to explore and raise awareness of these issues: BioHackathon 2009. Developers in attendance came from diverse backgrounds, with experts in Web services, workflow tools, text mining and visualization. Genome biologists provided expertise and exemplar data from the domains of sequence and pathway analysis and glyco-informatics. One goal of the meeting was to evaluate the ability to address real world use cases in these domains using the tools that the developers represented. This resulted in i) a workflow to annotate 100,000 sequences from an invertebrate species; ii) an integrated system for analysis of the transcription factor binding sites (TFBSs) enriched based on differential gene expression data obtained from a microarray experiment; iii) a workflow to enumerate putative physical protein interactions among enzymes in a metabolic pathway using protein structure data; iv) a workflow to analyze glyco-gene-related diseases by searching for human homologs of glyco-genes in other species, such as fruit flies, and retrieving their phenotype-annotated SNPs. Beyond deriving prototype solutions for each use-case, a second major purpose of the BioHackathon was to highlight areas of insufficiency. We discuss the issues raised by our exploration of the problem/solution space, concluding that there are still problems with the way Web services are modeled and annotated, including: i) the absence of several useful data or analysis functions in the Web service "space"; ii) the lack of documentation of methods; iii) lack of compliance with the SOAP/WSDL specification among and between various programming-language libraries; and iv) incompatibility between various bioinformatics data formats. Although it was still difficult to solve real world problems posed to the developers by the biological researchers in attendance because of these problems, we note the promise of addressing these issues within a semantic framework.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Taking demand management into the future: Managing flexible loads on the electricity network using smart appliances and controlled loads @

@article{swinson2015}

## Absract

Unprecedented changes have occurred over the last five years in the way customers use electricity. These changes are driving electricity distributors to evolve and extend their demand management capabilities to include grid balancing, respond to localised demand and promote and activate smart appliances. In South East Queensland, Australia, two successful forward looking demand management programs are well established. More than 50,000 demand response ready air conditioners have been connected to the network and are able to be controlled by the distributor. Results show that demand reductions from these air conditioners are reliable and sustained for the period of demand events. A second program uses controlled load electric hot water systems as a ‘solar sponge’ to integrate renewables into the network. This article highlights the potential demand management benefits of using hot water systems to reduce the localised peaks and fill the midday demand trough. The results from both programs show the capability of these demand management tools to improve network utilisation and grid balancing and reduce overall network expenditure. A further demand management initiative identified as having the greatest likelihood of success in delivering benefits to both the utility and customer are tariff structures which incorporate cost reflective pricing. In this way, time of use and magnitude of demand are addressed and positive price signals encouraging load control of appliances are provided. This coupling of demand management and tariffs is shown to be highly effective in achieving demand reductions. Automated load control can support customers’ acceptance of new pricing approaches and provide a ‘set and forget’ solution for optimising the benefits of cost reflective tariffs. The challenge for distributors is how to transition the existing demand management incentives and tariffs to a sustainable future program in an increasingly disaggregated and competitive market.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Smart Energy Management and Demand Reduction by Consumers and Utilities in an IoT-Fog based Power Distribution System @

@article{tom2019}

## Absract

The growing demand for energy and the increasing carbon footprint in the globe has made electricity utilities to move from non-renewable energy to renewable energy. The integration of renewables into the electric grid is increasing day-by-day. The consumers’ energy consumption needs to be managed wisely and effectively. The Internet of Things has helped in connecting all homes and appliances to the Internet. With smart homes, it is possible to study consumer’s usage patterns and their demand for energy. During peak hours of the day, the demand for energy increases and have to be met by the utilities by starting up additional coal-fired generation. This makes peak hour usage of electricity costly. This paper studies the usage behavior of consumers from their historical data and predicts the demand for energy every hour for the individual consumer for the next 72 hours using time series analysis. Also, the work statistically studies the usage pattern of appliances in every home thereby finding which appliances play a significant role during the peak hour usage. This work will help utilities understand how their consumers use electricity and can encourage consumers to shift usage of peak hour appliances to non-peak hours. Also, consumers can grant control of individual appliances to utilities, to curtail the load during peak hours to reduce the demand.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Service-Oriented Computing, 16th International Conference, ICSOC 2018, Hangzhou, China, November 12-15, 2018, Proceedings @

@article{huang2018}

## Absract

We propose a novel service mining framework to personalize services in an IoT based smart home. We describe a new technique based on the concept of convenience to discover periodic composite IoT services to suit the smart home occupant’s convenience needs. The key features of convenience is the ability to model the spatio-temporal aspects as occupants move in time and space within the smart home. We propose a novel framework for the transient composition of spatio-temporal IoT service. We design two strategies to prune non-promising compositions. Specifically, a significance model is proposed to prune insignificant composite IoT services. We describe a spatio-temporal proximity technique to prune loosely correlated composite IoT services. A periodic composite IoT service model is proposed to model the regularity of composite IoT services occurring at a certain location in a given time interval. The experimental results on real datasets show the efficiency and effectiveness of our proposed approach.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Service-Oriented Computing, 14th International Conference, ICSOC 2016, Banff, AB, Canada, October 10-13, 2016, Proceedings @

@article{huang2016}

## Absract

A service mining framework is proposed that enables discovering interesting relationships in Internet of Things services bottom-up. The service relationships are modeled based on spatial-temporal aspects, environment, people, and operation. An ontology-based service model is proposed to describe services. We present a set of metrics to evaluate the interestingness of discovered service relationships. Analytical and simulation results are presented to show the effectiveness of the proposed evaluation measures.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Service-based analysis of biological pathways @

@article{zheng2009}

## Absract

Computer-based pathway discovery is concerned with two important objectives: pathway identification and analysis. Conventional mining and modeling approaches aimed at pathway discovery are often effective at achieving either objective, but not both. Such limitations can be effectively tackled leveraging a Web service-based modeling and mining approach. Inspired by molecular recognitions and drug discovery processes, we developed a Web service mining tool, named PathExplorer, to discover potentially interesting biological pathways linking service models of biological processes. The tool uses an innovative approach to identify useful pathways based on graph-based hints and service-based simulation verifying user's hypotheses. Web service modeling of biological processes allows the easy access and invocation of these processes on the Web. Web service mining techniques described in this paper enable the discovery of biological pathways linking these process service models. Algorithms presented in this paper for automatically highlighting interesting subgraph within an identified pathway network enable the user to formulate hypothesis, which can be tested out using our simulation algorithm that are also described in this paper.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Service Pattern Discovery of Web Service Mining in Web Service Registry-Repository @

@article{liang2006}

## Absract

This paper presents and elaborates the concept of Web service usage patterns and pattern discovery through service mining. We define three different levels of service usage data: i) user request level, ii) template level and iii) instance level. At each level, we investigate patterns of service usage data and the discovery of these patterns. An algorithm for service pattern discovery at the template level is presented. We show the system architecture of a service-mining enabled service registry repository. Web service patterns, pattern discovery and pattern mining supports the discovery and composition of complex services, which in turn supports the application of web services to increasingly complex business processes and applications.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Service Mining: Using Process Mining to Discover, Check, and Improve Service Behavior @

@article{aalst2012}

## Absract

Web services are an emerging technology to implement and integrate business processes within and across enterprises. Service orientation can be used to decompose complex systems into loosely coupled software components that may run remotely. However, the distributed nature of services complicates the design and analysis of service-oriented systems that support end-to-end business processes. Fortunately, services leave trails in so-called event logs and recent breakthroughs in process mining research make it possible to discover, analyze, and improve business processes based on such logs. Recently, the task force on process mining released the process mining manifesto. This manifesto is supported by 53 organizations and 77 process mining experts contributed to it. The active participation from end-users, tool vendors, consultants, analysts, and researchers illustrate the growing significance of process mining as a bridge between data mining and business process modeling. In this paper, we focus on the opportunities and challenges for service mining, i.e., applying process mining techniques to services. We discuss the guiding principles and challenges listed in the process mining manifesto and also highlight challenges specific for service-orientated systems.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Service Mining on the Web @

@article{zheng2009}

## Absract

The Web is transforming from a Web of data to a Web of both Semantic data and services. This trend is providing us with increasing opportunities to compose potentially interesting and useful services from existing services. While we may not sometimes have the specific queries needed in top-down service composition approaches to identify them, the early and proactive exposure of these opportunities will be key to harvest the great potential of the large body of Web services. In this paper, we propose a Web service mining framework that allows unexpected and interesting service compositions to automatically emerge in a bottom-up fashion. We present several mining techniques aiming at the discovery of such service compositions. We also present evaluation measures of their interestingness and usefulness. As a novel application of this framework, we demonstrate its effectiveness and potential by applying it to service-oriented models of biological processes for the discovery of interesting and useful pathways.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Semantic Web Services, Advancement through Evaluation @

@article{bansal2012}

## Absract

Service-oriented computing (SOC) has emerged as the eminent market environment for sharing and reusing service-centric capabilities. For Web services to become practical, an infrastructure needs to be supported that allows users and applications to discover, deploy, compose and synthesize services automatically. This automation can take place effectively only if formal semantic descriptions of Web services are available. In this chapter we report on an implementation of a semantics-based automated service discovery and composition engine that we have developed. This engine employs a multi-step narrowing algorithm and is efficiently implemented using the constraint logic programming technology. The salient features of our engine are its scalability, i.e., its ability to handle very large service repositories, and its extremely efficient processing times for discovery and composition queries. This implementation was evaluated at the Web Services Challenge (WSC) in 2006 and 2007 (Blake et al. (2006) WSC-06: the web service challenge. In: Joint proceedings of the CEC/EEE, San Francisco, The Web Services Challenge (2007) http://www.wschallenge.org/wsc07/).

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Self-Recalibrating Surface EMG Pattern Recognition for Neuroprosthesis Control Based on Convolutional Neural Network @

@article{zhai2017}

## Absract

Hand movement classification based on surface electromyography (sEMG) pattern recognition is a promising approach for upper limb neuroprosthetic control. However, maintaining day-to-day performance is challenged by the non-stationary nature of sEMG in real-life operation. In this study, we propose a self-recalibrating classifier that can be automatically updated to maintain a stable performance over time without the need for user retraining. Our classifier is based on convolutional neural network (CNN) using short latency dimension-reduced sEMG spectrograms as inputs. The pretrained classifier is recalibrated routinely using a corrected version of the prediction results from recent testing sessions. Our proposed system was evaluated with the NinaPro database comprising of hand movement data of 40 intact and 11 amputee subjects. Our system was able to achieve \textbackslashtextasciitilde10.18\% (intact, 50 movement types) and \textbackslashtextasciitilde2.99\% (amputee, 10 movement types) increase in classification accuracy averaged over five testing sessions with respect to the unrecalibrated classifier. When compared with a support vector machine (SVM) classifier, our CNN-based system consistently showed higher absolute performance and larger improvement as well as more efficient training. These results suggest that the proposed system can be a useful tool to facilitate long-term adoption of prosthetics for amputees in real-life applications.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Robust Location-Aware Activity Recognition Using Wireless Sensor Network in an Attentive Home @

@article{lu2009}

## Absract

This paper presents a robust location-aware activity recognition approach for establishing ambient intelligence applications in a smart home. with observations from a variety of multimodal and unobtrusive wireless sensors seamlessly integrated into ambient-intelligence compliant objects (AICOs), the approach infers a single resident's interleaved activities by utilizing a generalized and enhanced Bayesian Network fusion engine with inputs from a set of the most informative features. These features are collected by ranking their usefulness in estimating activities of interest. Additionally, each feature reckons its corresponding reliability to control its contribution in cases of possible device failure, therefore making the system more tolerant to inevitable device failure or interference commonly encountered in a wireless sensor network, and thus improving overall robustness. This work is part of an interdisciplinary Attentive Home pilot project with the goal of fulfilling real human needs by utilizing context-aware attentive services. We have also created a novel application called “Activity Map” to graphically display ambient-intelligence-related contextual information gathered from both humans and the environment in a more convenient and user-accessible way. All experiments were conducted in an instrumented living lab and their results demonstrate the effectiveness of the system. Note to Practitioners—This system aims to achieve non-obtrusive and location-aware activity recognition, and the authors have successfully prototyped several AICOs to naturally collect interactions from residents or status from the environment. In addition, these AICOs have the potential to be commercialized in the future due to practicability and near-term advances in embedded systems. Furthermore, other potential advantages of an AICO lie in its applicability to other domains beyond just the home environment. Our initial work has yielded high overall accuracy, therefore, suggesting that it is a feasible approach that may lead to practical ambient intelligent applications (such as the Activity Map in this work). The limitations are that some currently available sensors cannot measure specific desired observations, or, in some cases, require users to carry them to operate.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Robotics Research, The 13th International Symposium ISRR @

@article{douillard2010}

## Absract

This paper presents a general probabilistic framework for multi-sensor multi-class object recognition based on Conditional Random Fields (CRFs) trained with virtual evidence boosting. The learnt representation models spatial and temporal relationships and is able to integrate arbitrary sensor information by automatically extracting features from data. We demonstrate the benefits of modelling spatial and temporal relationships for the problem of detecting seven classes of objects using laser and vision data in outdoor environments. Additionally, we show how this framework can be used with partially labeled data, thereby significantly reducing the burden of manual data annotation.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Responsiveness of residential electricity demand to dynamic tariffs: Experiences from a large field test in the Netherlands @

@article{klaassen2016}

## Absract

To efficiently facilitate the energy transition it is essential to evaluate the potential of demand response in practice. Based on the results of a Dutch smart grid pilot, this paper assesses the potential of both manual and semi-automated demand response in residential areas. To stimulate demand response, a dynamic tariff and smart appliances were used. The participating households were informed about the tariff day-ahead through a home energy management system, connected to a display installed on the wall in their living room. The tariff was intuitively displayed: self-consumption of photovoltaic generation was stimulated by means of a low tariff, but also the generation itself played a central role on the display. Household flexibility is analyzed, focusing on: (i) the load shift of (smart) appliances, and (ii) the response of the (overall) peak load towards the dynamic tariff. To assess the latter, i.e. price responsiveness, the participants were split up in two comparable groups which were subject to a different moment of evening peak-pricing. Based on the results, it is concluded that mainly the flexibility of the white goods (i.e. the washing machine, tumble dryer and dishwasher) is used for demand response. The main part of the flexible load of these (smart) appliances is shifted from the evening to the midday, to match local generation. This load shift remained stable over a long period of time (>1year) and is not responsive to the exact moment of peak-pricing. Therefore, it is concluded that a simple and transparent design for dynamic tariffs is sufficient and most effective to stimulate (manual) residential demand response. Such a tariff should emphasize the ‘right’ moments to use electricity, intuitively linked to renewable generation.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Ranking appliance energy efficiency in households: Utilizing smart meter data and energy efficiency frontiers to estimate and identify the determinants of appliance energy efficiency in residential buildings @

@article{kavousian2015}

## Absract

 This paper offers a novel method to rank residential appliance energy efficiency utilizing energy efficiency frontiers. The method is validated using a real-world case study of 4231 buildings in Ireland. Our results show that structural factors have the largest impact on energy efficiency, followed by socioeconomic factors and behavioral factors. For example, households with high penetration of efficient lightbulbs and double-glazed windows were on average 4 and 3.5\% more efficient than others. Households with the head of household having higher education are on average 1.3\% more efficient than their peers. Finally, households that track their energy savings are on average 0.4\% more efficient than others. Furthermore, installing heater timers, wall insulation, and living in owned residences were correlated with higher efficiency. Generally, families with kids who have full-time employment and are highly-educated are more efficient compared to families with no kids, or families with retirees or unemployed members. This result has important implications for both targeting and messaging of energy efficiency programs. Some behavioral factors demonstrated significant impact on appliance energy efficiency. For instance, households that expressed interest in making major energy-saving lifestyle changes scored higher efficiency ranks on average. Conversely, households that expressed doubt about their motivation to save energy ranked lower in efficiency. This finding validates the role of educational programs to increase awareness about energy efficiency and its importance. In short, our results show that a data-driven analysis of a population is needed to develop a balanced view of the drivers of energy efficiency, and to devise a targeted approach to improve homes’ energy efficiency.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Prediction of Human Activity by Discovering Temporal Sequence Patterns @

@article{li2014}

## Absract

Early prediction of ongoing human activity has become more valuable in a large variety of time-critical applications. To build an effective representation for prediction, human activities can be characterized by a complex temporal composition of constituent simple actions and interacting objects. Different from early detection on short-duration simple actions, we propose a novel framework for long -duration complex activity prediction by discovering three key aspects of activity: Causality, Context-cue, and Predictability. The major contributions of our work include: (1) a general framework is proposed to systematically address the problem of complex activity prediction by mining temporal sequence patterns; (2) probabilistic suffix tree (PST) is introduced to model causal relationships between constituent actions, where both large and small order Markov dependencies between action units are captured; (3) the context-cue, especially interactive objects information, is modeled through sequential pattern mining (SPM), where a series of action and object co-occurrence are encoded as a complex symbolic sequence; (4) we also present a predictive accumulative function (PAF) to depict the predictability of each kind of activity. The effectiveness of our approach is evaluated on two experimental scenarios with two data sets for each: action-only prediction and context-aware prediction. Our method achieves superior performance for predicting global activity classes and local action units.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Prediction of appliances energy use in smart homes @

@article{arghira2012}

## Absract

This paper presents methods for prediction of energy consumption of different appliances in homes. The aim is to predict the next day electricity consumption for some services in homes. Historical data for a set of homes in France was used. Two basic predictors are tested and a stochastic based predictor is proposed. The performance of the predictors is studied and it shows that the proposed predictor gives better results than other approaches. Two processings are proposed to improve the performance of the predictor, segmentation and aggregation of data. Application results are provided.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Predictability of Energy Use in Homes @

@article{lachut2014}

## Absract

Predictability of home energy usage forms the basis of many home energy management and demand-response systems. While existing studies focus on designing more accurate prediction algorithms, a comprehensive energy management solution requires a broad understanding of prediction accuracy at different granularities, for example appliance and home, as well as different time horizons, for example an hour, day, or week into the future. In this paper, we undertake an analysis of predictability of power draw of appliances and whole-home energy consumption at four different time horizons: an hour, a quarter-day, a day, and a week in the future. Our analysis presents two research contributions. Our first contribution is a diverse dataset, GreenHomes, that includes appliance power draw and whole-home energy consumption data from seven homes across three states in the United States over a two-year period. Our second and primary contribution is a set of insights into the predictability of home energy usage. We show that simple statistic-based algorithms perform as well as sophisticated machine learning algorithms and time-series based predictors. These simple algorithms can considerably reduce the computational need for large-scale predictive analysis of home energy data. We also show that appliance-level power draw is more predictable than whole-home energy consumption at shorter time horizons while home-level energy consumption is more predictable at longer time horizons. Finally, we show that there is large variation in predictability across homes. This variation may be attributed to home type and points to the need for personalized energy management systems.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Mining frequent and top-K High Utility Time Interval-based Events with Duration patterns @

@article{huang2019}

## Absract

Traditional frequent sequential pattern mining only considers the time point-based item or event in the patterns. However, in many application, the events may span over multiple time points and the relations among events are also important. Time interval-based pattern mining is proposed to mine the interesting patterns of events that span over some time periods and also by considering the relations among events. Previous works of time interval-based pattern mining focused on the relations between events without considering the duration of each event. However, the same event with different time duration may cause different results. In this work, we propose two algorithms, SARA and SARS, for mining frequent time interval-based events with duration, TIED, patterns. TIED patterns not only keep the relations between two events but also reveal the time periods when each event happens and ends. For the performance evaluation, we propose a naive algorithm and modify a previous algorithm along with the implementation of SARA and SARS. The experimental results show that SARA and SARS are more efficient in terms of execution time and memory usage than other two algorithms. Moreover, we extend this work by considering utility value or importance of event in each time stamp. Therefore, we propose another new High Utility Time Interval-based Events with Duration, HU-TIED, pattern. HU-TIED incorporates the concept of utility pattern mining and TIED pattern mining. We design an algorithm, LMSpan, to mine top-K HU-TIED patterns. For the performance evaluation, we design a baseline algorithm, GenerateNCheck to compare with LMSpan. LMSpan takes less time and memory and generates less candidates than GenerateNCheck.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Latent feature learning for activity recognition using simple sensors in smart homes @

@article{chen2018}

## Absract

Activity recognition is an important step towards monitoring and evaluating the functional health of an individual, and it potentially promotes human-centric ubiquitous applications in smart homes particularly for senior healthcare. The nature of human activity characterized by a high degree of complexity and uncertainty, however, poses a great challenge to the design of good feature representations and the optimization of classifiers towards building a robust model for human activity recognition. In this study, we propose to exploit deep learning techniques to automatically learn high-level features from the binary sensor data under the assumption that there exist discriminative latent patterns inherent in the simple low-level features. Specifically, we extract high-level features with a stacked autoencoder that has a deep and hierarchy architecture, and combine feature learning and classifier construction into a unified framework to obtain a jointly optimized activity recognizer. Besides, we investigate two different original feature representations of the sensor data for latent feature learning. To evaluate the performance of the proposed method, we conduct extensive experiments on three publicly available smart home datasets, and compare it with a range of shallow models in terms of time-slice accuracy and class accuracy. Experimental results show that our proposed model achieves better recognition rates and generalizes better across different original feature representations, indicating its applicability to the real-world activity recognition.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Internet of things: Vision, applications and research challenges @

@article{miorandi2012}

## Absract

The term “Internet-of-Things” is used as an umbrella keyword for covering various aspects related to the extension of the Internet and the Web into the physical realm, by means of the widespread deployment of spatially distributed devices with embedded identification, sensing and/or actuation capabilities. Internet-of-Things envisions a future in which digital and physical entities can be linked, by means of appropriate information and communication technologies, to enable a whole new class of applications and services. In this article, we present a survey of technologies, applications and research challenges for Internet-of-Things.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Integration scenarios of Demand Response into electricity markets: Load shifting, financial savings and policy implications @

@article{feuerriegel2016}

## Absract

Demand Response allows for the management of demand side resources in real-time; i.e. shifting electricity demand according to fluctuating supply. When integrated into electricity markets, Demand Response can be used for load shifting and as a replacement for both control reserve and balancing energy. These three usage scenarios are compared based on historic German data from 2011 to determine that load shifting provides the highest benefit: its annual financial savings accumulate to €3.110M for both households and the service sector. This equals to relative savings of 2.83\% compared to a scenario without load shifting. To improve Demand Response integration, the proposed model suggests policy implications: reducing bid sizes, delivery periods and the time-lag between market transactions and delivery dates in electricity markets.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Hybrid Sankey diagrams: Visual analysis of multidimensional data for understanding resource use @

@article{lupton2017}

## Absract

Sankey diagrams are used to visualise flows of materials and energy in many applications, to aid understanding of losses and inefficiencies, to map out production processes, and to give a sense of scale across a system. As available data and models become increasingly complex and detailed, new types of visualisation may be needed. For example, when looking for opportunities to reduce steel scrap through supply chain integration, it is not enough to consider simply flows of “steel” — the alloy, thickness, coating and forming history of the metal can be critical. This paper combines data-visualisation techniques with the traditional Sankey diagram to propose a new type of “hybrid” Sankey diagram, which is better able to visualise these different aspects of flows.There is more than one way to visualise a dataset as a Sankey diagram, and different ways are appropriate in different situations. To facilitate this, a systematic method is presented for generating different hybrid Sankey diagrams from a dataset, with an accompanying open-source Python implementation. A common data structure for flow data is defined, through which this method can be used to generate Sankey diagrams from different data sources such as material flow analysis, life-cycle inventories, or directly measured data. The approach is introduced with a series of visual examples, and applied to a real database of global steel flows.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# How smart do smart meters need to be? @

@article{mogles2017}

## Absract

Governments across the world are investing in smart metering devices that report energy use to the user with the aim of reducing consumption. However, the effectiveness of such In-Home Displays (IHDs) has been questioned, since savings are small. This is possibly because informing the consumer of their consumption in kWh, or monetary units, fails to give context, or inform of possible actions to reduce consumption. We investigate, for the first time, the effect of replacing the simple statement of energy use an IHD gives, with a detailed array of information specifically designed to improve consumer energy literacy and suggest behaviour change through personalised actionable messages set against a series of psychological value systems for context, and which can identify potential profligacy. The results from a carefully controlled field experiment show: 1) value framing and action prompts have a significant effect on occupants' behaviour, with the mean temperature of homes being reduced from 22.4 °C to 21.7 °C, and a marked reduction in gas consumption—22.0\% overall and 27.2\% in high consumers; 2) energy literacy increasing from 0.52 to 1.28 (on a 0–4 scale); 3) it is possible to target potentially profligate households, without inappropriately messaging others; 4) engagement is high, with 82\% of the participants finding the system useful. These results emphasize the necessity of improving energy literacy when encouraging energy efficient behaviours and point to a new generation of smart meters with the potential to increase energy literacy, make much greater savings and impact climate change policy.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Householders’ Mental Models of Domestic Energy Consumption: Using a Sort-And-Cluster Method to Identify Shared Concepts of Appliance Similarity @

@article{gabethomas2016}

## Absract

If in-home displays and other interventions are to successfully influence people’s energy consumption, they need to communicate about energy in terms that make sense to users. Here we explore householders’ perceptions of energy consumption, using a novel combination of card-sorting and clustering to reveal shared patterns in the way people think about domestic energy consumption. The data suggest that, when participants were asked to group appliances which they felt naturally ‘went together’, there are relatively few shared ideas about which appliances are conceptually related. To the extent participants agreed on which appliances belonged together, these groupings were based on activities (e.g., entertainment) and location within the home (e.g., kitchen); energy consumption was not an important factor in people’s categorisations. This suggests messages about behaviour change aimed at reducing energy consumption might better be tied to social practices than to consumption itself.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Household electricity demand profiles – A high-resolution load model to facilitate modelling of energy flexible buildings @

@article{marszalpomianowska2016}

## Absract

The objective is to present a high-resolution model of household electricity use developed based upon a combination of measured and statistical data. It is a bottom-up model, which uses the 1-min cycle power use characteristics of a single appliance as the main building block. The effect of parameters, such as the number of occupants and their attitude towards energy use is included in the model. Moreover, the model accounts for phenomena related to unexpected weather conditions and local/national events, e.g. TV shows. The main aim of model is to generate high-resolution household load profiles for investigation of flexibility potential of domestic appliances and network modelling.The model is validated with two datasets of 1-h and 5-min data from 89 to 16 households, respectively. The comparison between measured and modelled values indicates that model well captures the characteristics of domestic electricity load profiles on a daily as well seasonal basis. For high-resolution data, the model represents well the differences in demand between households of dissimilar size as well as the diversity of demand between households of the same size. For the individual household, the high-end power consumption is under-represented since the timing of peaks is more diverse in the model.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Household appliances penetration and ownership trends in residential buildings @

@article{cabeza2018}

## Absract

 Understanding the development of the trends in the ownership of different appliances in a historic context in various countries of the world can not only provide important insights for understanding the dynamics of adoption of different appliances, but can also help with foresight: how the future may develop for these or other, new appliances on the market. Although available literature in household appliances energy consumption, energy management and energy efficiency has seen some advances, there is a clear lack in the literature on household appliance ownership. In this paper, historic data is gathered and analysed for several groups of appliance types (white appliances, brown appliances and small appliances) for 12 countries representing four continents, when available since 1970 to date. Countries representing different parts of the world were selected to present an overview on household appliances ownership and energy consumption. One of the first conclusions of the study is that there is little or no information in many countries from South America, Africa or South Asia. Refrigerators, freezers and washing machines ownership are an example of most other white goods. Brown goods appeared in the market at very different time, depending on each one (from the 70s to the late 90s) and their ownership growth is much higher than for the previous ones. Most of small line appliances ownership has not reached saturation yet.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Feeding back about eco-feedback: How do consumers use and respond to energy monitors? @

@article{buchanan2014}

## Absract

To date, a multitude of studies have examined the empirical effect of feedback on energy consumption yet very few have examined how feedback might work and the processes it involves. Moreover, it remains to be seen if the theoretical claims made concerning how feedback works can be substantiated using empirical data. To start to address this knowledge gap, the present research used qualitative data analysis to examine how consumers use and respond to energy monitors. The findings suggest feedback may increase both the physical and conscious visibility of consumption as well as knowledge about consumption. Accordingly, support was evident for the theoretical assertions that feedback transforms energy from invisible to visible, prompts motivated users to learn about their energy habits, and helps address information deficits about energy usage. We conclude by evaluating the feasibility of feedback to substantially reduce consumption and discuss ways in which feedback could be improved to aid its effectiveness in the long term before discussing the implication our findings may have for government policy.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Evaluation of Household Electricity Savings. Analysis of Household Electricity Demand Profile and User Activities @

@article{laicane2015}

## Absract

To achieve reduction in electricity consumption, it is vital to have current information about household electricity use. This allows to draw user behaviour profile based on household electricity demand for a specific time of the day. Activities involving the use of electricity for certain purposes, time of use survey and smart metering data of a four people family were analysed in this study. Household energy efficiency performance till 2020 was evaluated based on increase of equipment energy efficiency driven by technological progress. The results of energy efficiency evaluation for particular household shows that 1219 kWh savings can be achieved due to improvements of energy performance of some mostly used appliances until 2020 (i.e., reduction in electricity consumption of 13\% if compared to present scenario). However, the results imply that user behaviour change is also important to implement the measures associated with energy efficiency improvements in households.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Emerging Chemical Patterns:  A New Methodology for Molecular Classification and Compound Selection @

@article{auer2006}

## Absract

None

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Efficient Mining of Discriminating Relationships Among Attributes Involving Arithmetic Operations @

@article{duan2016}

## Absract

Contrast patterns describe differences between two or more data sets or data classes; they have been proven to be useful for solving many kinds of problems, such as building accurate classifiers, defining clustering quality measures, and analyzing disease subtypes. This article investigates the mining of a new kind of contrast patterns, namely discriminating inter-attribute functions (DIFs), which represent arithmetic-expression-based inter-attribute relationships that distinguish classes of data. DIFs are an expressive and practical alternative of item-based contrast patterns and can express discriminating relationships such as “weight/(height)2 is more likely to be ≤25 in one class than in another class.” Besides introducing the DIF mining problem, this article makes theoretical and algorithmic contributions on the problem. We prove that DIF mining is MAX SNP-hard. Regarding how to efficiently mine DIFs, we present a set of rules to prune the search space of arithmetic expressions by eliminating redundant ones (equivalent to some others). We give two algorithms: one for finding all DIFs satisfying given thresholds and another for finding certain optimal DIFs using genetic computation techniques. The former is useful when the number of attributes is small, whereas the latter is useful when that number is large; both use the redundant arithmetic-expression pruning rules. A performance study shows that our techniques are effective and efficient for finding DIFs.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Effects of continuous feedback on households’ electricity consumption: Potentials and barriers @

@article{nilsson2014}

## Absract

Two field experiments were carried out to study (a) the effects on energy savings of continuous visual feedback via in-home displays, and (b) the motives for responding or not. In study 1, 40 participants living in separate or semi-detached houses in two different towns participated. All participants received a questionnaire and a list of possible energy saving measures. Households were then randomly assigned to an experimental condition (display) or a control condition (no display). In study 2, 32 households in rented apartments participated. No significant differences between the conditions were found for either of the studies. In study 2, semi-structured interviews were conducted among nine of the households. Through an analysis of interview transcripts barriers were identified explaining why the feedback intervention was not sufficient to change behaviour and reduce consumption. The barriers experienced indicate that there is a risk of overconfidence in IHDs. For the development of energy policies and more wide-scale implementation, it is important to be aware of the potential obstacles to success.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# E-CELL: software environment for whole-cell simulation. @

@article{tomita1999}

## Absract

MOTIVATION: Genome sequencing projects and further systematic functional analyses of complete gene sets are producing an unprecedented mass of molecular information for a wide range of model organisms. This provides us with a detailed account of the cell with which we may begin to build models for simulating intracellular molecular processes to predict the dynamic behavior of living cells. Previous work in biochemical and genetic simulation has isolated well-characterized pathways for detailed analysis, but methods for building integrative models of the cell that incorporate gene regulation, metabolism and signaling have not been established. We, therefore, were motivated to develop a software environment for building such integrative models based on gene sets, and running simulations to conduct experiments in silico. RESULTS: E-CELL, a modeling and simulation environment for biochemical and genetic processes, has been developed. The E-CELL system allows a user to define functions of proteins, protein-protein interactions, protein-DNA interactions, regulation of gene expression and other features of cellular metabolism, as a set of reaction rules. E-CELL simulates cell behavior by numerically integrating the differential equations described implicitly in these reaction rules. The user can observe, through a computer display, dynamic changes in concentrations of proteins, protein complexes and other chemical compounds in the cell. Using this software, we constructed a model of a hypothetical cell with only 127 genes sufficient for transcription, translation, energy production and phospholipid synthesis. Most of the genes are taken from Mycoplasma genitalium, the organism having the smallest known chromosome, whose complete 580 kb genome sequence was determined at TIGR in 1995. We discuss future applications of the E-CELL system with special respect to genome engineering. AVAILABILITY: The E-CELL software is available upon request. SUPPLEMENTARY INFORMATION: The complete list of rules of the developed cell model with kinetic parameters can be obtained via our web site at: http://e-cell.org/.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Discovering Spatio-Temporal Relationships among IoT Services @

@article{huang2018}

## Absract

We propose a framework to discover proximate IoT service relationships based on spatio-temporal features. We introduce a spatio-temporal proximity model in terms of spatial-proximity and temporal-proximity to discard insignificant IoT service relationships. The proximity model focuses on quantifying the correlation strength among IoT services from time and location aspects. A new algorithm is proposed to discover proximate spatio-temporal IoT service relationships. We also present preliminary experimental results.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Development and analysis of residential change-point models from smart meter data @

@article{perez2017}

## Absract

As access to residential energy use data becomes more widely available, it is possible to identify significant energy consumers and provide guidance on mitigating such large loads. In hotter climates, such as Texas, air-conditioning (AC) systems are important contributors to overall residential electricity demand. Providing a quick, simple and effective framework to describe and compare electricity demand patterns between different houses is valuable to identify potential candidates for peak load reduction and overall energy use mitigation. In this study, we evaluate the application of daily change-point models to describe the demand patterns of residential AC systems for 45 actual houses in Austin, TX during 2013. While previous research regarding change-point models has been focused on monthly data for commercial buildings, this study extends its application to daily residential energy use. The resulting models describe a behavior where energy consumption with relation to outdoor dry-bulb temperature is negligible up until a change-point, after which AC energy use increases linearly and results in an “energy slope.” An analysis of the neighborhood shows the distribution of the AC “energy slopes” is left-skewed and centered on 0.08kW per °C dry bulb temperature. Energy audit information found eight house characteristics to be correlated with a higher energy slope. A subsequent parametric analysis using data from the energy simulation software BEopt confirmed the direction of the correlation. This work provides a screening tool to compare energy demand patterns of houses and target houses with the largest magnitude of energy slopes for future energy audits.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Detecting Group Differences: Mining Contrast Sets @

@article{bay2001}

## Absract

A fundamental task in data analysis is understanding the differences between several contrasting groups. These groups can represent different classes of objects, such as male or female students, or the same group over time, e.g. freshman students in 1993 through 1998. We present the problem of mining contrast sets: conjunctions of attributes and values that differ meaningfully in their distribution across groups. We provide a search algorithm for mining contrast sets with pruning rules that drastically reduce the computational complexity. Once the contrast sets are found, we post-process the results to present a subset that are surprising to the user given what we have already shown. We explicitly control the probability of Type I error (false positives) and guarantee a maximum error rate for the entire analysis by using Bonferroni corrections.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Demand response flexibility and flexibility potential of residential smart appliances: Experiences from large pilot test in Belgium @

@article{dhulst2015}

## Absract

This paper presents a well-founded quantified estimation of the demand response flexibility of residential smart appliances. The flexibility from five types of appliances available within residential premises (washing machines, tumble dryers, dishwashers, domestic hot water buffers and electric vehicles), is quantified based on measurements from the LINEAR pilot, a large-scale research and demonstration project focused on the introduction of demand response at residential premises in the Flanders region in Belgium. The flexibility potential of the smart appliances, or the maximal amount of time a certain increase or decrease of power can be realized within the comfort requirements of the user, is calculated. In general, the flexibility potential varies during the day, and the potential for increasing or decreasing the power consumption is in general not equal. Additionally, an extrapolation of the flexibility potential of wet appliances is presented for Belgium. The analysis shows that, using smart wet appliances, an average maximum increase of 430W per household can be realized at midnight, and a maximum decrease of 65W per household can be realized in the evening. The resulting flexibility potential can be used as an instrument to determine the impact or economic viability of demand response programs for residential premises.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Deep Convolutional Neural Network Based ECG Classification System Using Information Fusion and One-Hot Encoding Techniques @

@article{li2018}

## Absract

Although convolutional neural networks (CNNs) can be used to classify electrocardiogram (ECG) beats in the diagnosis of cardiovascular disease, ECG signals are typically processed as one-dimensional signals while CNNs are better suited to multidimensional pattern or image recognition applications. In this study, the morphology and rhythm of heartbeats are fused into a two-dimensional information vector for subsequent processing by CNNs that include adaptive learning rate and biased dropout methods. The results demonstrate that the proposed CNN model is effective for detecting irregular heartbeats or arrhythmias via automatic feature extraction. When the proposed model was tested on the MIT-BIH arrhythmia database, the model achieved higher performance than other state-of-the-art methods for five and eight heartbeat categories (the average accuracy was 99.1\% and 97\%). In particular, the proposed system had better performance in terms of the sensitivity and positive predictive rate for V beats by more than 4.3\% and 5.4\%, respectively, and also for S beats by more than 22.6\% and 25.9\%, respectively, when compared to existing algorithms. It is anticipated that the proposed method will be suitable for implementation on portable devices for the e-home health monitoring of cardiovascular disease.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Data driven prediction models of energy use of appliances in a low-energy house @

@article{candanedo2017}

## Absract

This paper presents and discusses data-driven predictive models for the energy use of appliances. Data used include measurements of temperature and humidity sensors from a wireless network, weather from a nearby airport station and recorded energy use of lighting fixtures. The paper discusses data filtering to remove non-predictive parameters and feature ranking. Four statistical models were trained with repeated cross validation and evaluated in a testing set: (a) multiple linear regression, (b) support vector machine with radial kernel, (c) random forest and (d) gradient boosting machines (GBM). The best model (GBM) was able to explain 97\% of the variance (R2) in the training set and with 57\% in the testing set when using all the predictors. From the wireless network, the data from the kitchen, laundry and living room were ranked the highest in importance for the energy prediction. The prediction models with only the weather data, selected the atmospheric pressure (which is correlated to wind speed) as the most relevant weather data variable in the prediction. Therefore, atmospheric pressure may be important to include in energy prediction models and for building performance modeling.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Consumer preferences for feedback on household electricity consumption @

@article{karjalainen2011}

## Absract

Numerous studies have shown that feedback on energy consumption can work to effectively reduce household energy consumption. However, relatively little work has been done on the best ways to present information in order to maximise energy savings. In this work, different ways of presenting feedback on electricity consumption were systematically analysed and user interface prototypes were developed based on the analysis. The prototypes were shown to consumers in qualitative interviews to gain information on how well they understood them and what kind of feedback they prefer to receive on their electricity consumption. The results show that the following features of feedback on electricity consumption are most valued by consumers: presentations of costs (over a period of time), appliance-specific breakdown, i.e. information on what proportion is consumed by each appliance, and historical comparison, i.e. comparison with their own prior consumption.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Composing Web services on the Semantic Web @

@article{medjahed2003}

## Absract

Service composition is gaining momentum as the potential silver bullet for the envisioned Semantic Web. It purports to take the Web to unexplored efficiencies and provide a flexible approach for promoting all types of activities in tomorrow’s Web. Applications expected to heavily take advantage of Web service composition include B2B E-commerce and E-government. To date, enabling composite services has largely been an ad hoc, time-consuming, and error-prone process involving repetitive low-level programming. In this paper, we propose an ontology-based framework for the automatic composition of Web services. We present a technique to generate composite services from high-level declarative descriptions. We define formal safeguards for meaningful composition through the use of composability rules. These rules compare the syntactic and semantic features of Web services to determine whether two services are composable. We provide an implementation using an E-government application offering customized services to indigent citizens. Finally, we present an exhaustive performance experiment to assess the scalability of our approach.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Cloud forecasting system for monitoring and alerting of energy use by home appliances @

@article{chou2019}

## Absract

 Inrecentyears,energy information systems have had an important role in the operational optimization of intelligent buildings to provide such benefits as high efficiency, energy savings and smart services. Interest in the intelligent management of home energy consumption using data mining and time series analysis is increasing. Therefore, this work develops an efficient web-based energy information management system for the power consumption of home appliances that monitors the energy load of a home, analyzes its energy consumption based on machine learning, and then sends information to various stakeholders. It interacts with the end-user through energy dashboards and emails. The web-based system includes a novel hybrid artificial intelligence model to improve its prediction of energy usage. An automatic warning function is also developed to identify anomalous energy consumption in a home in real time. The cloud system automatically sends a message to the user's email whenever a warning is necessary. End-users of this system can use forecast information and anomalous data to enhance the efficiency of energy usage in their buildings especially during peak times by adjusting the operating schedule of their appliances and electrical equipment.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Causal Mechanism Graph ─ A new notation for capturing cause-effect knowledge in software dependability @

@article{huang2017}

## Absract

Understanding cause-effect relations between concepts in software dependability engineering is fundamental to various research or industrial activities. Cognitive maps are traditionally used to elicit and represent such knowledge; however they seem incapable of accurately representing complex causal mechanisms in dependability engineering. This paper proposes a new notation called Causal Mechanism Graph (CMG) to elicit and represent the cause-effect domain knowledge embedded in experts’ minds or described in the literature. CMG contains a new set of symbols elicited from domain experts to capture the recurring interaction mechanisms between multiple concepts in software dependability engineering. Furthermore, compared to major existing graphic methods, CMG is particularly robust and suitable for mental knowledge elicitation: it allows one to represent the full range of cause-effect knowledge, accurately or fuzzily as one sees fit depending on the depth of knowledge he/she has. This feature combined with excellent reliability and validity poses CMG as a promising method that has the potential to be used in various areas, such as software dependability requirement elicitation, software dependability assessment and dependability risk control.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# CASCOM: Intelligent Service Coordination in the Semantic Web @

@article{botelho2008}

## Absract

Semantic service discovery is the process of locating Web Services based on the description of their functional and non-functional semantics. Both service oriented computing and the semantic Web envision intelligent agents to proactively pursue this task on behalf of their clients. Service discovery can be performed in different ways depending on the service description framework, on means of service selection, and on its coordination through assisted mediation or in a peer-to-peer fashion.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Bioinformatics Research and Applications, 6th International Symposium, ISBRA 2010, Storrs, CT, USA, May 23-26, 2010. Proceedings @

@article{higa2010}

## Absract

A popular model for gene regulatory networks is the Boolean network model. In this paper, we propose an algorithm to perform an analysis of gene regulatory interactions using the Boolean network model and time-series data. Actually, the Boolean network is restricted in the sense that only a subset of all possible Boolean functions are considered. We explore some mathematical properties of the restricted Boolean networks in order to avoid the full search approach. We applied the proposed algorithm in a case study of the budding yeast cell cycle network using an artificial dataset. The results show that some interactions can be fully or, at least, partially determined under the Boolean model considered. We have shown that this analysis can be used as the first step for gene relationships detection with a high flexibility to include biological knowledge. What we envisage with our method is a model that points out which connections should be checked in the wet lab and consequently facilitate some biological experiments.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Big Data Mining of Energy Time Series for Behavioral Analytics and Energy Consumption Forecasting @

@article{singh2018}

## Absract

Responsible, efficient and environmentally aware energy consumption behavior is becoming a necessity for the reliable modern electricity grid. In this paper, we present an intelligent data mining model to analyze, forecast and visualize energy time series to uncover various temporal energy consumption patterns. These patterns define the appliance usage in terms of association with time such as hour of the day, period of the day, weekday, week, month and season of the year as well as appliance-appliance associations in a household, which are key factors to infer and analyze the impact of consumers’ energy consumption behavior and energy forecasting trend. This is challenging since it is not trivial to determine the multiple relationships among different appliances usage from concurrent streams of data. Also, it is difficult to derive accurate relationships between interval-based events where multiple appliance usages persist for some duration. To overcome these challenges, we propose unsupervised data clustering and frequent pattern mining analysis on energy time series, and Bayesian network prediction for energy usage forecasting. We perform extensive experiments using real-world context-rich smart meter datasets. The accuracy results of identifying appliance usage patterns using the proposed model outperformed Support Vector Machine (SVM) and Multi-Layer Perceptron (MLP) at each stage while attaining a combined accuracy of 81.82\%, 85.90\%, 89.58\% for 25\%, 50\% and 75\% of the training data size respectively. Moreover, we achieved energy consumption forecast accuracies of 81.89\% for short-term (hourly) and 75.88\%, 79.23\%, 74.74\%, and 72.81\% for the long-term; i.e., day, week, month, and season respectively.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# arxiv.org 7/24/2019, 11:04:49 PM.pdf @

@article{anonymous}

## Absract

None

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Appliance usage prediction using a time series based classification approach @

@article{basu2012}

## Absract

Energy management for residential homes and offices require the prediction of the usage(s) or service request(s) of different appliances present in the house. The hardware requirement is more simplified and practical if the task is only based on energy consumption data and no other sensors are used. The proposed model tries to formalize such an approach using a time-series based multi-label classifier which takes into account correlation between different appliances among other factors. In this work, prediction results are shown for 1-hour in the future but this approach can be extended to predict more hours in the future as per the requirement(with restrictions). The learned models and decision tree showing the important factors in the input information is also discussed.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Appliance electrical consumption modelling at scale using smart meter data @

@article{murray2018}

## Absract

 The food industry is one of the world's largest contributors to carbon emissions, due to energy consumption throughout the food life cycle. This paper is focused on the residential consumption phase of the food life cycle assessment (LCA), i.e., energy consumption during home cooking. Specifically, while much effort has been placed on improving appliance energy efficiency, appliance models used in various applications, including the food LCA, are not updated regularly. This process is hindered by the fact that the cooking appliance models are either very cumbersome, requiring knowledge of parameters which are difficult to obtain or dependent on manufacturers' data which do not always reflect variable cooking behaviour of the general public. This paper proposes a methodology for generating accurate appliance models from energy consumption data, obtained by smart meters that are becoming widely available worldwide, without detailed knowledge of additional parameters such as food being prepared, mass of food, etc. Furthermore, the proposed models, due to the nature of smart meter data, are built incorporating actual usage patterns reflecting specific cooking practice. We validate our results from large, geographically spread energy datasets and demonstrate, as a case study, the impact of up-to-date models in the consumption phase of food LCA.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Appliance daily energy use in new residential buildings: Use profiles and variation in time-of-use @

@article{cetin2014}

## Absract

One of the largest user of electricity in the average U.S. household is appliances, which when aggregated, account for approximately 30\% of electricity used in the residential building sector. As influencing the time-of-use of energy becomes increasingly important to control the stress on today's electrical grid infrastructure, understanding when appliances use energy and what causes variation in their use are of great importance. However, there is limited appliance-specific data available to understand their use patterns. This study provides daily energy use profiles of four major household appliances: refrigerator, clothes washer, clothes dryer, and dishwasher, through analyzing disaggregated energy use data collected for 40 single family homes in Austin, TX. The results show that when compared to those assumed in current energy simulation software for residential buildings, the averaged appliance load profiles have similar daily distributions. Refrigerators showed the most constant and consistent use. However, the three user-dependent appliances, appliances which depend on users to initiate use, varied more greatly between houses and by time-of-day. During peak use times, on weekends, and in homes with household members working at home, the daily use profiles of appliances were less consistent.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Antioxidant capacity of betacyanins as radical scavengers for peroxyl radical and nitric oxide @

@article{taira2015}

## Absract

This study was designed to assess the antioxidant capacity of betacyanins as indole derived plant pigments, such as betanin, phyllocactin and betanidin. The antioxidant capacity of the betacyanins was evaluated as an index of radical scavenging ability using the peroxyl radical generating system in the presence of AAPH and NO generating system using NOR3 as an NO donor. The peroxyl radical scavenging capacity was dose-dependent in the low concentration range (25–100nM). The mol-Trolox equivalent activity/mol compound (mol-TEA/mol-compound) as an index of the antioxidant capacity indicated the following order at 10.70±0.01, 3.31±0.14 and 2.83±0.01mol-TEA/mol-compound for betanidin, betanin and phyllocactin, respectively. In addition, betacyanins reduced the nitrite-level in the low concentration range of 2.5–20μM. The IC50 values (μM) of nitrogen radical scavenging activity were 24.48, 17.51 and 6.81 for betanin, phyllocactin and betanidin. ESR studies provided evidence that the compounds directly scavenged NO. These results indicated that betacyanins have a strong antioxidant capacity, particularly betanidin with a catechol group had higher activity than those of the glycoside of betacyanins. This study demonstrated that the betacyanins will be useful as natural pigments to provide defence against oxidative stress.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# Advanced Web Services @

@article{zheng2013}

## Absract

We propose a service-oriented framework for exploring networks of processes modeled as Web services. In particular, we apply this approach to biological processes that builds upon and extends existing biological representation methodologies. We present our prototype service exploration tool, named PathExplorer, to discover potentially interesting biological pathways linking service models of biological processes. We describe an innovative approach used by PathExplorer to identify useful pathways and its service-based simulation strategy to support predictive analysis.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# A Web Service Mining Framework @

@article{zheng2007}

## Absract

We propose a service mining framework for exploring interesting compositions of existing Web services. The framework first screens Web services for composition leads using a “coarse-grained” filtering approach. It then verifies these leads based on runtime conditions. Top candidates are selected from the verified leads and evaluated for their interestingness. We present algorithms to automate the screening phase of the framework. Finally, we study the effects of key variables on lead compositions' interestingness. As a motivating example, we apply these algorithms to the field of biological pathway discovery and rely on knowledge obtained from reverse engineering online resources to assess their effectiveness.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# A service computing manifesto: the next 10 years @

@article{bouguettaya2017}

## Absract

Mapping out the challenges and strategies for the widespread adoption of service computing.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# A real-life assessment on the effect of smart appliances for shifting households’ electricity demand @

@article{kobus2015}

## Absract

Today’s major developments in the production and demand of electricity in domestic areas make it increasingly important that domestic electricity demand can respond to the availability of electricity. Energy management systems and smart appliances can facilitate this by supporting the user to shift electricity demand of appliances to moments in time when electricity is abundantly available. However, the benefits resulting from domestic demand response depend on household acceptance and behaviour change. This paper explores the real electricity demand shift of households in time and the role of smart appliances to bring about this shift. A longitudinal study was conducted among Dutch households over a period of one year. The households received a dynamic electricity tariff, an energy management system and a smart washing machine. Results show that households shift their usage of the smart washing machine mostly to the day when the sun is shining and electricity is produced by their own solar panels. Households who regularly used automation of the smart washing machine, which implicates that the use of the washing machine is automatically shifted to time periods where electricity supply is abundantly available, were more likely to shift their electricity usage. Furthermore, during the course of one year, the results remained stable, indicating a structural shift in demand.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# A Middleware based on Service Oriented Architecture for Heterogeneity Issues within the Internet of Things (MSOAH-IoT) @

@article{mesmoudi2018}

## Absract

 Nowadays, many Internet of Things (IoT) applications have been emerging as innovative solutions for daily life issues, in different fields such as smart cities, environmental surveillance, health care, traffic monitoring, etc. However, most of these solutions are built in a vertical way using proprietary solutions, which increase heterogeneity problems. To solve this issue, many research works have focused on middleware solutions. Nevertheless, such approaches have some kind of limitations. Throughout this work, we have designed and implemented a middleware based on service oriented architecture, capable to deal with the heterogeneity issues. The solution was implemented in three steps starting by collecting data from many heterogeneous sensors hardware using REST API, then heterogeneous networking interfaces have been introduced and finally the middleware have been tested on gateways working on different operating systems.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---
# A Boolean network inference from time-series gene expression data using a genetic algorithm @

@article{barman2018}

## Absract

Inferring a gene regulatory network from time-series gene expression data is a fundamental problem in systems biology, and many methods have been proposed. However, most of them were not efficient in inferring regulatory relations involved by a large number of genes because they limited the number of regulatory genes or computed an approximated reliability of multivariate relations. Therefore, an improved method is needed to efficiently search more generalized and scalable regulatory relations.

## Objective

## Domain

## Input

## Technology

## Output

## Notes

---




## Objective

## Domain

## Input

## Technology

## Output

## Notes

# TITLE

## Abstract

## Objective

## Domain

## Input

## Technology

## Output

## Notes

# TITLE

## Abstract

## Objective

## Domain

## Input

## Technology

## Output

## Notes

# TITLE

## Abstract

## Objective

## Domain

## Input

## Technology

## Output

## Notes

# TITLE

## Abstract

## Objective

## Domain

## Input

## Technology

## Output

## Notes

# TITLE

## Abstract

## Objective

## Domain

## Input

## Technology

## Output

## Notes

# TITLE

## Abstract

## Objective

## Domain

## Input

## Technology

## Output

## Notes

# TITLE

## Abstract

## Objective

## Domain

## Input

## Technology

## Output

## Notes
# TITLE

## Abstract

## Objective

## Domain

## Input

## Technology

## Output

## Notes




Hybrid Sankey diagrams: Visual analysis of multidimensional data for understanding resource use


# A Web Service Mining Framework @
@article{zheng2007}

## Abstract
_We propose a service mining framework for exploring interesting compositions of existing Web services. The frame-work first screens Web services for composition leads usinga “coarse-grained” filtering approach. It then verifies theseleads based on runtime conditions. Top candidates are se-lected from the verified leads and evaluated for their inter-estingness. We present algorithms to automate the screen-ing phase of the framework. Finally, we study the effects ofkey variables on lead compositions’ interestingness. As amotivating example, we apply these algorithms to the fieldof biological pathway discovery and rely on knowledge ob-tained from reverse engineering online resources to assesstheir effectiveness.

## Objective
SM framework

## Domain
IoT service, Web Service Models, Ontologies, Service composition, Spatial and temporal correlation, Service Mining 
* Unanticipated and interesting composition of web service

## Input

## Technology
IoT, Sensors

## Output
* Operation similarity value
* Interestingness
* Actionability
* Novelty
* Surprisingness

## Notes
* Direct and indirect recognition
* Two types of service recognition, promotion and inhibition