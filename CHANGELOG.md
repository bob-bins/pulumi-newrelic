CHANGELOG
=========

## HEAD (Unreleased)
_(none)_

---

## 4.1.1 (2021-05-21)
* Update to v2.22.1 of the NewRelic Terraform Provider

## 4.1.0 (2021-05-12)
* Update to v2.22.0 of the NewRelic Terraform Provider

## 4.0.0 (2021-04-19)
* Update to v2.21.1 of the NewRelic Terraform Provider
* Depend on Pulumi 3.0, which includes improvements to Python resource arguments and key translation, Go SDK performance,
  Node SDK performance, general availability of Automation API, and more.

## 3.17.0 (2021-04-12)
* Upgrade to pulumi-terraform-bridge v2.23.0

## 3.16.1 (2021-03-23)
* Upgrade to pulumi-terraform-bridge v2.22.1  
  **Please Note:** This includes a bug fix to the refresh operation regarding arrays

## 3.16.0 (2021-03-15)
* Upgrade to pulumi-terraform-bridge v2.21.0
* Release macOS arm64 binary

## 3.15.0 (2021-03-09)
* Update to v2.21.0 of the NewRelic Terraform Provider

## 3.14.0 (2021-02-19)
* Update to v2.19.0 of the NewRelic Terraform Provider

## 3.13.1 (2021-02-16)
* Upgrade to pulumi-terraform-bridge v2.19.0  
  **Please Note:** This includes a bug fix that stops mutating resources options in the nodejs provider

## 3.13.0 (2021-02-16)
* Update to v2.18.0 of the NewRelic Terraform Provider

## 3.12.0 (2021-02-03)
* Upgrade to v2.17.0 of the NewRelic Terraform Provider

## 3.11.0 (2021-01-29)
* Upgrade to pulumi-terraform-bridge v2.18.1

## 3.10.1 (2021-01-27)
* Upgrade to v2.15.1 of the NewRelic Terraform Provider

## 3.10.0 (2021-01-19)
* Upgrade to v2.15.0 of the NewRelic Terraform Provider

## 3.9.1 (2021-01-13)
* Upgrade to v2.14.1 of the NewRelic Terraform Provider
* Upgrade to pulumi-terraform-bridge v2.17.0
* Upgrade to Pulumi v2.17.0

## 3.9.0 (2020-12-21)
* Upgrade to v2.14.0 of the NewRelic Terraform Provider

## 3.8.4 (2020-11-23)
* Upgrade to pulumi-terraform-bridge v2.13.2  
  * This adds support for import specific examples in documentation

## 3.8.3 (2020-11-17)
* Upgrade to v2.13.5 of the NewRelic Terraform Provider

## 3.8.2 (2020-11-09)
* Upgrade to pulumi-terraform-bridge v2.12.1

## 3.8.1 (2020-10-28)
* Upgrade to v2.13.3 of the NewRelic Terraform Provider

## 3.8.0 (2020-10-26)
* Upgrade to v2.13.1 of the NewRelic Terraform Provider
* Improving the accuracy of previews leading to a more accurate understanding of what will actually change rather than assuming all output properties will change.  
  ** PLEASE NOTE:**  
  This new preview functionality can be disabled by setting `PULUMI_DISABLE_PROVIDER_PREVIEW` to `1` or `false`.

## 3.7.0 (2020-10-19)
* Upgrade to Pulumi v2.12.0 and pulumi-terraform-bridge v2.11.0
* Upgrade to v2.13.0 of the NewRelic Terraform Provider

## 3.6.0 (2020-10-14)
* Upgrade to v2.12.0 of the NewRelic Terraform Provider
* Upgrade to pulumi-terraform-bridge v2.11.0
* Upgrade to Pulumi v2.11.2

## 3.5.0 (2020-10-01)
* Upgrade to v2.8.0 of the NewRelic Terraform Provider

## 3.4.3 (2020-09-25)
* Upgrade to v2.7.5 of the NewRelic Terraform Provider

## 3.4.2 (2020-09-21)
* Upgrade to v2.7.4 of the NewRelic Terraform Provider

## 3.4.1 (2020-09-14)
* Upgrade to v2.7.1 of the NewRelic Terraform Provider
* Upgrade to pulumi-terraform-bridge v2.8.0
* Upgrade to Pulumi v2.10.0

## 3.4.0 (2020-09-08)
* Upgrade to v2.7.0 of the NewRelic Terraform Provider

## 3.3.1 (2020-09-04)
* Upgrade to v2.6.1 of the NewRelic Terraform Provider

## 3.3.0 (2020-08-31)
* Upgrade to pulumi-terraform-bridge v2.7.3
* Upgrade to Pulumi v2.9.0, which adds type annotations and input/output classes to Python
* Upgrade to v2.6.0 of the NewRelic Terraform Provider

## 3.2.1 (2020-08-17)
* Upgrade to v2.5.1 of the NewRelic Terraform Provider

## 3.2.0 (2020-08-04)
* Upgrade to v2.5.0 of the NewRelic Terraform Provider

## 3.1.1 (2020-07-31)
* Upgrade to v2.4.2 of the NewRelic Terraform Provider

## 3.1.0 (2020-07-30)
* Upgrade to v2.4.1 of the NewRelic Terraform Provider
* Upgrade to Pulumi v2.7.1
* Upgrade to pulumi-terraform-bridge v2.6.0  

## 3.0.1 (2020-06-30)
* Upgrade to v2.1.2 of the NewRelic Terraform Provider

## 3.0.0 (2020-06-24)
* Upgrade to v2.1.1 of the NewRelic Terraform Provider
  ** Please Note: **
  The upstream provider has changed from terraform-providers/terraform-provider-newrelic to newrelic/terraform-provider-newrelic

## 2.4.1 (2020-06-12)
* Switch to GitHub actions for build

## 2.4.0 (2020-06-06)
* Upgrade to v1.19.0 of the NewRelic Terraform Provider

## 2.3.1 (2020-05-28)
* Upgrade to Pulumi v2.3.0
* Upgrade to pulumi-terraform-bridge v2.4.0

## 2.3.0 (2020-05-18)
* Upgrade to v1.18.0 of the NewRelic Terraform Provider

## 2.2.2 (2020-05-12)
* Upgrade to pulumi-terraform-bridge v2.3.1

## 2.2.1 (2020-05-05)
* Upgrade to v1.17.0 of the NewRelic Terraform Provider

## 2.2.0 (2020-05-04)
* Upgrade to v1.17.0 of the NewRelic Terraform Provider

## 2.1.0 (2020-04-28)
* Regenerate datasource examples to be async
* Upgrade to pulumi-terraform-bridge v2.1.0

## 2.0.0 (2020-04-17)
* Upgrade to Pulumi v2.0.0
* Upgrade to pulumi-terraform-bridge v2.0.0

## 1.11.0 (2020-04-14)
* Refactor layout to support Go modules

## 1.10.0 (2020-03-31)
* Upgrade to v1.16.0 of the NewRelic Terraform Provider

## 1.9.0 (2020-03-23)
* Upgrade to v1.15.1 of the NewRelic Terraform Provider
* Upgrade to Pulumi v1.12.1
* Upgrade to pulumi-terraform-bridge v1.8.2

## 1.8.0 (2020-03-09)
* Upgrade to v1.15.0 of the NewRelic Terraform Provider

## v1.7.0 (2020-02-24)
* Upgrade to v1.14.0 of the NewRelic Terraform Provider

## 1.6.1 (2020-02-19)
* Uprade to v1.13.1 of the NewRelic Terraform Provider

## 1.6.0 (2020-02-07)
* Upgrade to v1.13.0 of the NewRelic Terraform Provider

## 1.5.0 (2020-01-29)
* Upgrade to v1.12.2 of the NewRelic Terraform Provider
* Upgrade to pulumi-terraform-bridge v1.6.4

## 1.4.0 (2019-12-19)
* Namespace names in .NET SDK are adjusted to PascalCase
([#37](https://github.com/pulumi/pulumi-newrelic/pull/37)).
* Upgrade to v1.10.0 of the NewRelic Terraform Provider
* Upgrade to pulumi-terraform-bridge v1.5.2

## 1.3.0 (2019-12-09)
* Upgrade to v1.9.0 of NewRelic Terraform Provider

## 1.2.0 (2019-12-04)
* Upgrade to support go 1.13.x
* Upgrade to v1.8.0 of NewRelic Terraform Provider
* Upgrade to pulumi-terraform@dotnet

## 1.1.0 (2019-11-15)
* Removing redundant README.rst from Python package which causes installation problems

## 1.1.0 (2019-11-15)
* Add support for DotNet SDK Generation
* Upgrade to v1.7.0 of the NewRelic Terraform Provider

## 1.0.0 (2019-10-24)
* Regenerate SDK based on tf2pulumi 0.6.0
* Upgrade to v1.5.2 of the NewRelic Terraform Provider

## 0.18.10 (2019-09-05)
* Upgrade to Pulumi v1.0.0

## 0.18.9 (2019-08-29)
* Upgrade to pulumi-terraform 3f206601e7

## 0.18.8 (2019-08-20)
* Depend on latest pulumi package

## 0.18.7 (2019-08-09)
* Upgrade to pulumi-terraform@9db2fc93cd

## 0.18.6 (2019-08-08)
* Update to pulumi-terraform@013b95b1c8

## 0.18.5 (2019-07-11)
* Upgrade to v1.5.1 of the NewRelic Terraform Provider

## 0.18.4 (2019-07-09)
* Fix detailed diffs with nested computed values.

## 0.18.3 (2019-07-08)
* Communicate detailed information about the difference between a resource's desired and actual state during a Pulumi update

## 0.18.2 (2019-06-21)
* Add TypeScript type guards for each resource class ([7ace3e9b5f2d](https://github.com/pulumi/pulumi-terraform/commit/7ace3e9b5f2d))
* Update to pulumi-terraform@3635bed3a5 which stops maps containing `.` being treated as nested maps.

## 0.18.1 (2019-05-29)
* Fix an issue where configuration provided via the environment may not be honoured

## 0.18.0 (2019-04-10)
* Initial release of the New Relic provider, based on revision 3651ee8 of the New Relic Terraform provider
