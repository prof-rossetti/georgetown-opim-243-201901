# "Deploy a Script to Production" Exercise

## Objectives

Learn how to "deploy" a Python script to a "production" environment, namely an application server hosted by Heroku. And to schedule regular execution of the script.

## Prerequisites

  + ["Refresh your Fork" Exercise](/exercises/refresh-fork.md)
  + [Heroku](/notes/heroku.md) (sign up for a account, install the Heroku CLI, and login via the command line)

## Instructions

Follow the instructions below to obtain an example Python script, configure an application server, deploy the script to the server, and schedule the script's execution at regular intervals.

### Repo Setup

Fork [this repository](______________________) which contains a simple Python script for sending emails ("app/send_email.py").

Clone your fork to download it onto your local computer and automatically associate it with a remote address named "origin".

```sh
git clone __________
```

Navigate into your local repo before running any of the other commands below:

```sh
cd _________
```

### Server Setup

First, [install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install), and make sure you can login and list your applications.

```sh
heroku login

heroku apps:list
```

Then use the online [Heroku Dashboard](https://dashboard.heroku.com/) or the command-line (instructions below) to create a new application server, specifying a unique name (e.g. "notification-app-123", but yours will likely need to be different):

```sh
heroku apps:create notification-app-123
```

Verify the app has been created:

```sh
heroku apps:list
```

If you created the application server from the command-line within your project repository, this process might automatically associate the repository with that server. Check to see whether you see a remote address called "heroku":

```sh
git remote -v
```

If you don't see the remote address called "heroku", manually associate the repo with the application server:

```sh
heroku git:remote -a notification-app-123
```

At this point, you should be able to verify the remote address:

```sh
git remote -v
```

### Server Configuration

Next, configure environment variables on the server, via the application's "" settings in the online console, or from the command line (instructions below):

```sh
heroku config -a notification-app-123

heroku config:set SENDGRID_API_KEY="abc123" notification-app-123
heroku config:set MY_EMAIL_ADDRESS="someone@gmail.com" notification-app-123
```

At this point, you should be able to verify the production environment has been configured with the proper environment variable values:

```sh
heroku config -a notification-app-123
```

### Deploying

After this configuration process is complete, you are ready to "deploy" the application's source code to the Heroku server:

```sh
git push heroku master
```

### Invoking the Script

Once you've deployed the source code to the Heroku server, login to the server to see the files there, and take an opportunity to test your ability to run the script that now lives on the server:

```sh
heroku run bash -a notification-app-123 # login to the server
ls -al # optionally see the files, nice!
python app/notifier.py # see the output, nice!
exit # logout

# or alternatively, without login and logout:
heroku run "python app/notifier.py" -a notification-app-123
```

### Scheduling the Script

Finally, provision and configure the server's "Heroku Scheduler" resource to run the notification script at specified intervals, for example once per day.

Monitor your inbox over the specified time period and witness your notification service in action!
