# SENG-371
The following is a SENG 371 project being developed by <b>Mitchell Rivett</b> and <b>Tyler Potter</b>.

## Project Question
What is the relation between software development methodologies and development time per feature in a software system?

## Methodology
To answer our project question we will gather the starting and finishing time of every completed feature listed in the issue tracking software used by the selected codebases (Jira and Github), as well as the time they started using the issue tracking software, and the time they last made any changes. This will be done by creating a Python script. I AM HERE <b>Our program will assume that Jira was used throughout the entire project lifespan.</b> This Python script will also calculate the average feature development time for all the collected information. Collected feature information will filter outliers by collecting features that were completed in over 30 minutes, and less than one year. For Jira issue tracking we will use JiraPython, and for Gitgub we will use <b>N/A</b>. When you collect the information, it will be stored in an external file to use for visualization. For every collected code base, you will have to input what software development method they used manually. We will use these files in a C++ program with OpenGL to create an appropriate graph.

Our primary method for visualizing the information would be to simply compare the them on a graph. This portion of the program will create a single 'average function release time vs project time' graph that will represent all the collected data for all different software development methods. Each project will be its own line on the graph, and eatch line will be colored according to its software development method. From here we should be able to view the differences for average feature completion time for each software development method.

### Additional Features
* Take the average of all the graphs for each software development method and create another line to represent it. This would be represented in the same color, the line would be formatted differently (ie. dotted line). This could give us a more accurate view of the differences between the software development methods.
* Take the average feature completion time for the whole project (average of [end day-start day] for each feature) and divide the average estimated completion time for the whole project (average of [planned end day-start day] for each feature) to get the feature completion time ratios for each project. This would be visualized using a 'completion time ratio vs project' bar graph. An additional graph could be provided to show the average feature completion time ratios of all the projects in the same software development methods, plotted with other development methods. This graph would be a 'completion time ratio vs software development method' bar graph.

## Codebases/Systems/Metrics
### Jira Issue Tracking
* <a href="https://github.com/SonarSource/sonarqube">SonarQube</a> (Open-source agile)
* <a href="https://github.com/micromata/projectforge-webapp">ProjectForge</a> (<a href="http://www.projectforge.org/">Open-source</a>)
* <a href="https://github.com/thinkaurelius/titan">Titan</a> (<a href="https://groups.google.com/forum/?utm_medium=email&utm_source=footer#!msg/aureliusgraphs/cIcJpwOnZMw/_Whhegn10t4J">Open-source agile</a>)

### Other
* <a href="https://github.com/okamstudio/godot">Godot</a> (Open-source)
* <a href="https://github.com/torvalds/linux">Linux</a> (<a href="http://www.linuxfoundation.org/what-is-linux">Open-source</a>)
<br>Firefox could also be an option, as it uses an agile open source development methodology.

## Project Milestones

### Milestone 1 - <a href="https://github.com/ycoady/UVic-Software-Evolution/issues/9">Project Setup</a> (January 28)
Defining:
* Project question
* Methodology (including the tools we expect to use)
* Codebases/Systems we will analyze
* Project milestones

### Milestone 2 - <a href="https://github.com/ycoady/UVic-Software-Evolution/issues/10">Data Collection and Experimentation</a> (February 04)
Conducted an experiment based on our research question:
* Came up with an assertion 
* Performed data collection - Defined specific metrics that will help analyze our assertion
* Analyzed the data collection to support/refute the assertion

### Milestone 3 - Data Collection and Experimentation (February 18)
Continuing experiments based on our research question:
* Begin working on the deliverable to answer our project question
* Refined our methodology
* Refining what resources/codebases we require

### Milestone 4 - Providing Deliverables (February 24)
* Provide deliverables for answering the project question.

## Current Issues
* What other code bases use Jira for their issue tracking, and do not use open-source, or open-source agile development methods?
* How we can extract the initial commit on a feature, and the closing commit for a feature through Github?

## Instructions
The following are directions on how to run the application in its current version:
<ol>
<li>Download 'SEng_371_Python_Script.py'.
<li>Download the pip tool and install the <a href = "http://jira-python.readthedocs.org/en/latest/">Jira-python library </a>.
<li>For python versions 2.7.9 and 3.40 use "python -m pip install jira".
<li>For versions below, use the <a href="https://pip.pypa.io/en/latest/installing.html">pip support</a>.
<li>Open command prompt.
<li>Change directory to the downloaded location.
<li>Type "python SEng_371_Python_Script.py PROJECT_NAME" and replace PROJECT_NAME with the project name as it is referred to as in the Jira database.
</ol>
This will return a list of feature development times, and the average of the list of feature development times.
