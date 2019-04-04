
# OPIM 243 Projects, Revisited

## Learning Objectives

  + Improve the quality and maintainability of your application software.
  + Use familiar applications as a basis upon which to learn new techniques.
  + Follow quality control best practices like code simplification / refactoring, automated testing, and continuous integration.

## Requirements

For each of the previous OPIM 243 Projects, implement the general requirements described below, and consult each of the following documents for project-specific guidance:

  + ["Shopping Cart" Project, Revisited](/projects/shopping-cart/revisited.md)
  + ["Executive Dashboard" Project, Revisited](/projects/exec-dash/revisited.md)
  + ["Robo Advisor" Project, Revisited](/projects/robo-advisor/revisited.md)

See also the professor's example solutions:

  + [Testing the "Shopping Cart"](https://github.com/s2t2/shopping-cart-screencast/pull/2/files)
  + [Testing the "Exec Dash"](https://github.com/s2t2/exec-dash-starter-py/pull/1/files)
  + [Testing the "Robo Advisor"](https://github.com/s2t2/robo-advisor-screencast/pull/1/files)

### Documentation Requirements

Your project repository should contain a "README.md" file. The README file should provide instructions to help someone else install, setup, run, and test your program. This includes instructions for installing package dependencies, for example using Pip. It also includes instructions for setting environment variables as necessary.

As you document for your application, strive to make it as easy as possible for someone else (or even your future self) to install it, use it, and understand what it is about.

### Licensing Requirements

[Choose a software license](/notes/licensing.md), and include a corresponding file called "LICENSE" or "LICENSE.md" in the root directory of your repository.

### Security Requirements

If your program requires sensitive information like secret passwords, API keys, or other credentials, those secret values should absolutely not be included in the source code or its revision history.

Use environment variables in conjunction with a ".env" file and a ".gitignore" file to read sensitive information from the software's operating environment while excluding them from the source code.

### Quality Requirements

#### Code Simplification

Scan your application's codebase for duplication of terms, and refactor to remove that duplication.

Also, your codebase should be reasonably organized and well documented with comments, to help others (and your future self) understand the code.

#### Automated Tests

Implement automated tests using the `pytest` package. See project-specific guidance for more details. Try to implement at least one of the basic challenges and one of the intermediate challenges.

As you think about ways to test your application, consider asking yourself questions like the following:

  + As I was developing this application, what manual steps did I take to ensure it was functioning properly? Can I automate those manual processes?
  + Is it possible for the application to receive user inputs that are unexpected or invalid? How should the application handle various invalid inputs?
  + How should the application's component functions perform given various inputs, whether valid or invalid?
  + Are there any functions or sections of the code which aren't easy to read or understand? Is there a way to use examples to communicate what is supposed to happen?
  + If the application processes data from the Internet: Is there a way to test the application's functionality without making any additional network requests?
  + If the application processes data from a CSV file or database: Is there a way to test the application's functionality without affecting the development environment datastore?

#### Continuous Integration

Configure your GitHub repository to integrate with a continuous integration (CI) platform like [Travis CI](/notes/travis-ci.md), such that automated tests are run on a CI server whenever new code is pushed to the remote GitHub repository.

### Dev Process Requirements

Develop your updates [on a branch](/notes/git.md#branch-operations), push that branch to GitHub in order to create a Pull Request, where you can further review your proposed changes and allow automated tests to run and pass on the CI server before finally "merging" the code into the master branch.

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
Dev Process | Submitted via Git repository which reflects an incremental revision history, branch operations, and Pull Request workflow | 15%

If experiencing execution error(s) while evaluating or testing the application's required functionality, evaluators are advised to reduce the project's grade by anywhere between 15% and 50%, depending on the circumstances and severity of the error(s).
