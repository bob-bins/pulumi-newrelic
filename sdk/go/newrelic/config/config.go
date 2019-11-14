// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
	"github.com/pulumi/pulumi/sdk/go/pulumi/config"
)

func GetApiKey(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "newrelic:apiKey")
	if err == nil {
		return v
	}
	if dv, ok := getEnvOrDefault("", nil, "NEWRELIC_API_KEY").(string); ok {
		return dv
	}
	return v
}

func GetApiUrl(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "newrelic:apiUrl")
	if err == nil {
		return v
	}
	if dv, ok := getEnvOrDefault("https://api.newrelic.com/v2", nil, "NEWRELIC_API_URL").(string); ok {
		return dv
	}
	return v
}

func GetCacertFile(ctx *pulumi.Context) string {
	return config.Get(ctx, "newrelic:cacertFile")
}

func GetInfraApiUrl(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "newrelic:infraApiUrl")
	if err == nil {
		return v
	}
	if dv, ok := getEnvOrDefault("https://infra-api.newrelic.com/v2", nil, "NEWRELIC_INFRA_API_URL").(string); ok {
		return dv
	}
	return v
}

func GetInsecureSkipVerify(ctx *pulumi.Context) bool {
	return config.GetBool(ctx, "newrelic:insecureSkipVerify")
}
