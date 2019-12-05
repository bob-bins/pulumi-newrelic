module github.com/pulumi/pulumi-newrelic

go 1.13

require (
	github.com/hashicorp/terraform-plugin-sdk v1.4.0
	github.com/pkg/errors v0.8.1
	github.com/pulumi/pulumi v1.6.1
	github.com/pulumi/pulumi-terraform-bridge v1.4.3
	github.com/terraform-providers/terraform-provider-newrelic v1.9.0
)

replace github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
