
# The "Quality Control" Project

> a.k.a. "OPIM 243 Projects, Revisited"

## Learning Objectives

  + Improve the quality and maintainability of your application software.
  + Use familiar applications as a basis upon which to learn new techniques.
  + Follow quality control best practices like code simplification / refactoring, automated testing, and continuous integration.

## Requirements

For each of the previous OPIM 243 Projects, implement the general requirements described below, and consult each of the following documents for project-specific guidance:

  + ["Shopping Cart" Project, Revisited](/projects/shopping-cart/revisited.md)
  + ["Executive Dashboard" Project, Revisited](/projects/exec-dash/revisited.md)
  + ["Robo Advisor" Project, Revisited](/projects/robo-advisor/revisited.md)

### Documentation Requirements

Your project repository should contain a "README.md" file. The README file should provide instructions to help someone else install, setup, and run your program. This includes instructions for installing package dependencies, for example using Pip. It also includes instructions for setting environment variables as necessary.

As you document for your application, strive to make it as easy as possible for someone else (or even your future self) to install it, use it, and understand what it is about.

### Licensing Requirements

[Choose a license](/notes/licensing.md) and include a "LICENSE" or "LICENSE.md" file in the root directory of your repository.

### Security Requirements

TBA

### Quality Requirements

#### Code Simplification

TBA

#### Automated Tests

Implement automated tests using the `pytest` package. See project-specific guidance for more details.

As you think about ways to test your application, consider asking yourself questions like the following:

  + As I was developing this application, what manual steps did I take to ensure it was functioning properly? Can I automate those manual processes?
  + Is it possible for the application to receive user inputs that are unexpected or invalid? How should the application handle various invalid inputs?
  + How should the application's component functions perform given various inputs, whether valid or invalid?
  + Are there any functions or sections of the code which aren't easy to read or understand? Is there a way to use examples to communicate what is supposed to happen?
  + If the application processes data from the Internet: Is there a way to test the application's functionality without making any additional network requests?
  + If the application processes data from a CSV file or database: Is there a way to test the application's functionality without affecting the development environment datastore?

#### Continuous Integration

TBA

## Submission Instructions

No need to re-submit unless your previously-submitted repository address has changed. Consult the respective project's submission instructions and submissions.csv file to ensure it contains the desired repository address.

## Evaluation Criteria

Project submissions will be evaluated according to the requirements set forth above, as summarized by the rubric below:

Category | Requirement | Weight
--- | --- | ---
Documentation | Contains a comprehensive README file | 15%
Licensing | Contains an appropriate LICENSE file | 10%
Security | Excludes sensitive information and credentials | 15%
Quality | Simplified to remove or minimize code duplication | 15%
Quality | Contains relevant automated tests | 20%
Quality | Deployed to a continuous integration (CI) server | 10%
Maintainability | Submitted via Git repository which reflects an incremental revision history | 15%

If experiencing execution error(s) while evaluating or testing the application's required functionality, evaluators are advised to reduce the project's grade by anywhere between 15% and 50%, depending on the circumstances and severity of the error(s).
