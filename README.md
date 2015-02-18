# SENG-371

## Project Question
What is the relation between software development methodologies, and development time per feature (ie. patches) release in a software system?

## Methodology
We will gather the information from the issue tracking software used by the selected codebases' (Jira and Github) by creating a Python script. For Jira issue tracking we will use JiraPython, and for Gitgub we will use <b>N/A</b>. Once we gather the appropriate information we will use a C++ program, using OpenGL, to create an appropriate graph.

Our primary method for visualizing the information to answer our project question would be to store the information gathered from multiple different code bases and compare the code bases we collect. For every entered code base, you will have to input what software development method they used manually. From here, you can create a single average function release time vs time graph that will represent all the collected data for all different software development methods. Each project will be its own line on the graph, and eatch line will be colored according to its software development method. From here we should be able to view the differences for average feature completion time for each software development method.
Another desired feature would be to take the average of all the graphs for each software development method and create another graph to represent it. This would be represented in the same color, but a differently formatted line (ie. dotted line). This could give us a more accurate view of the differences between the software development methods.

If we have the time, we could also represent the information by taking the average feature completion time for the whole project(average of [end day-start day] for each feature)/average estimated completion time for the whole project(average of [planned end day-start day] for each feature) ratios for each project, and visualize it.

## Codebases/Systems/Metrics
* <a href="https://github.com/okamstudio/godot">Godot</a> (Open-source)
* <a href="https://github.com/torvalds/linux">Linux</a> (<a href="http://www.linuxfoundation.org/what-is-linux">Open-source</a>)
* <a href="https://github.com/SonarSource/sonarqube">SonarQube</a> (Open-source agile)
* <a href="https://github.com/thinkaurelius/titan">Titan</a> (<a href="https://groups.google.com/forum/?utm_medium=email&utm_source=footer#!msg/aureliusgraphs/cIcJpwOnZMw/_Whhegn10t4J">Open-source agile</a>)
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
* Performed data collection - Defined specific metrics that will help analyze our assertion
* Analyzed the data collection to support/refute the assertion
* Refined our methodology
Begin working on project deliverable for answeringthe project question.

### Milestone 4 - Providing Deliverables (February 24)
Provide deliverables for answering the project question.

## Current Issues
N/A

<b>Members</b>:
Tyler Potter,
Mitchell Rivett
