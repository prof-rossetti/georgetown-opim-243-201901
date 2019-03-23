# Self-Directed (a.k.a. "Freestyle") Project

The "Freestyle" Project provides students with the flexibility to follow their own interests by planning and implementing their own application software.

> PAIR PROGRAMMING OPTION: During the proposal phase, students will officially designate whether they would like to work independently, be paired with a random partner, or be paired with a partner of choice. For mutual partner selections, each student should designate the other as their partner. If pairing, students should strive to significantly increase their project's scope, and each student is expected to make significant contributions to the application's source code.

## Deliverables

Follow the links below for more information about each deliverable, including submission instructions and evaluation criteria.

### [Proposal](freestyle/proposal.md)

### [Requirements Document](freestyle/requirements.md)

### [Implementation](freestyle/implementation.md)

### [Demo](freestyle/demo.md)

## Guidelines

Each project's requirements will be unique, but students should strive to adhere to the spirit of the guidelines below.

### Scope

The scope of the application's functionality should be around one or two times greater than previous OPIM 243 projects like the ["Robo Advisor"](/projects/robo-advisor.md),

### Data Processing

The application should process (read and/or write) data in at least one of the following machine-readable formats:
CSV, JSON, HTML, XML, SQL, PDF.

The application should store data in a local file, a relational database, or a Google Sheets spreadsheet document (see the [`gspread`](/notes/python/packages/gspread.md) package).

### User Interface

The application's interface should be intuitive to use and simple to understand. It should provide clear instructions as necessary.

The user should be able to use the application through an interface other than, or in addition to, the command-line. These alternative interfaces include, but are not limited to:

  + A **Native Graphical User Interface (GUI)**, implemented with a package like [`tkinter`](/notes/python/packages/tkinter.md)
  + A **Web-based Graphical User Interface (GUI)**, implemented with a package like [`flask`](/notes/python/packages/flask.md)
  + A **Speech-based Interface**, implemented with a package like [`speech_recognition`](/notes/python/packages/speech_recognition.md)
  + etc.

### Network and Connectivity

The application should process data from the Internet by requesting data from, posting data to, or otherwise interfacing with one or more third-party web services (APIs).

The application may optionally be accessible to users over the Internet (i.e. production web application).

### Hardware Integration

The application may optionally be deployed to a remote server (i.e. production web application or scheduled notification service), or incorporate other physical devices such as sensors and scanners.
