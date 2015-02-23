# SENG-371
The following is a SENG 371 project being developed by <b>Mitchell Rivett</b> and <b>Tyler Potter</b>.

## Project Question
What is the relation between software development methodologies and development time per feature in a software system?

## Metrics
The following is required information that is needed to carry out our methodology:
* Starting date of completed 'major' priority features.
* Finishing date of completed 'major' priority features.
* Starting date of issue tracking use.

## Methodology
To answer our project question we will gather the starting and finishing dates of every completed feature listed in the issue tracking software that is used by the selected codebases (Jira and Github). <b>We will also collect the date they started using the issue tracking software so we can measure the time they have completed features relitave to their progression in the project.</b> These metrics will be collected by creating a Python script. Our program will assume that the same issue tracking software was used throughout the entire project lifespan. This Python script will also calculate the average feature development time for the lifespan of the project that is entered. Collected feature information will filter outliers by collecting 'major' priority features that were completed in over 30 minutes, and less than one year. For Jira issue tracking we will use JiraPython<b>, and for Gitgub we will use N/A</b>. For every collected codebase, you will have to input what software development method they used manually. When the information is collected, it will be stored in an external file to use for the visualization part of the program. We will use these files in a C++ program with OpenGL to create an appropriate graph.

Our primary method for visualizing the information will be to compare each of the different codebases on a single 'average function release time vs project time' line graph. Each project will be its own line on the graph, and each line will be colored according to its software development method. From here we should be able to view the differences for average feature completion time for each software development method.

### Additional Features
* Take the average of all the graphs for each software development method and create another line to represent it. This would be represented in the same color, the line would be formatted differently (ie. dotted line). This could give us a more accurate view of the differences between the software development methods.
* Take the average feature completion time for the whole project (average of [end day-start day] for each feature) and divide the average estimated completion time for the whole project (average of [planned end day-start day] for each feature) to get the feature completion time ratios for each project. This would be visualized using a 'completion time ratio vs project' bar graph. An additional graph could be provided to show the average feature completion time ratios of all the projects in the same software development methods, plotted with other development methods. This graph would be a 'completion time ratio vs software development method' bar graph.

## Codebases/Systems
### Jira
* <a href="https://github.com/SonarSource/sonarqube">SonarQube</a> (Open-source agile)
* <a href="https://github.com/micromata/projectforge-webapp">ProjectForge</a> (<a href="http://www.projectforge.org/">Open-source</a>)
* <a href="https://github.com/apache/marmotta"></a>Marmotta</a> (Open-source agile)

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
* What other codebases use Jira for their issue tracking, and do not use open-source agile development methods?
* How we can extract the initial commit on a feature, and the closing commit for a feature through Github?
* What other issue tracking software allows us to collect our metrics?

## Instructions
The following are directions on how to run the application in its current version:
<ol>
<li>Download 'SEng_371_Python_Script.py'.
<li>Download the pip tool and install the <a href = "http://jira-python.readthedocs.org/en/latest/">Jira-python library </a>.
<li>For python versions 2.7.9 and 3.40 use "python -m pip install jira".
<li>For versions below, use the <a href="https://pip.pypa.io/en/latest/installing.html">pip support</a>.
<li>Open command prompt.
<li>Change directory to the downloaded location.
<li>Change the 'server' variable in the source code to the appropriate project's server.
<li>Type "python SEng_371_Python_Script.py PROJECT_NAME" and replace PROJECT_NAME with the project name as it is referred to as in the Jira database.
</ol>
This will return a list of feature development times, and the average of the list of feature development times.
