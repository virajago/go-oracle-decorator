# GO Oracle Decorator

This is a [decorator](https://github.com/cf-platform-eng/meta-buildpack/blob/master/README.md#decorators) buildpack
for Cloud Foundry that installs Oracle Client libraries for any GO application that needs to connect to an Oracle Database, and requiring *zero application code changes*.

When this decorator (and the [meta-buildpack](https://github.com/cf-platform-eng/meta-buildpack)) is present in your Cloud Foundry deployment, all you will have to do to install an Oracle client into your application container is to set an environment variable INCLUDE_ORACLE_CLIENT=Y 
