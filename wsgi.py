#!/usr/bin/env python
# https://blog.openshift.com/how-to-install-and-configure-a-python-flask-dev-environment-deploy-to-openshift/
from run import app as application

#
# Below for testing only
#
if __name__ == "__main__":
    application.run(debug=True)  # We will set debug false in production
