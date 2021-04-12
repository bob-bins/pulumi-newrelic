// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package newrelic

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "newrelic:index/alertChannel:AlertChannel":
		r = &AlertChannel{}
	case "newrelic:index/alertCondition:AlertCondition":
		r = &AlertCondition{}
	case "newrelic:index/alertMutingRule:AlertMutingRule":
		r = &AlertMutingRule{}
	case "newrelic:index/alertPolicy:AlertPolicy":
		r = &AlertPolicy{}
	case "newrelic:index/alertPolicyChannel:AlertPolicyChannel":
		r = &AlertPolicyChannel{}
	case "newrelic:index/apiAccessKey:ApiAccessKey":
		r = &ApiAccessKey{}
	case "newrelic:index/dashboard:Dashboard":
		r = &Dashboard{}
	case "newrelic:index/entityTags:EntityTags":
		r = &EntityTags{}
	case "newrelic:index/eventsToMetricsRule:EventsToMetricsRule":
		r = &EventsToMetricsRule{}
	case "newrelic:index/infraAlertCondition:InfraAlertCondition":
		r = &InfraAlertCondition{}
	case "newrelic:index/nrqlAlertCondition:NrqlAlertCondition":
		r = &NrqlAlertCondition{}
	case "newrelic:index/nrqlDropRule:NrqlDropRule":
		r = &NrqlDropRule{}
	case "newrelic:index/oneDashboard:OneDashboard":
		r = &OneDashboard{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:newrelic" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, err := PkgVersion()
	if err != nil {
		fmt.Println("failed to determine package version. defaulting to v1: %v", err)
	}
	pulumi.RegisterResourceModule(
		"newrelic",
		"index/alertChannel",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"newrelic",
		"index/alertCondition",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"newrelic",
		"index/alertMutingRule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"newrelic",
		"index/alertPolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"newrelic",
		"index/alertPolicyChannel",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"newrelic",
		"index/apiAccessKey",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"newrelic",
		"index/dashboard",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"newrelic",
		"index/entityTags",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"newrelic",
		"index/eventsToMetricsRule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"newrelic",
		"index/infraAlertCondition",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"newrelic",
		"index/nrqlAlertCondition",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"newrelic",
		"index/nrqlDropRule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"newrelic",
		"index/oneDashboard",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"newrelic",
		&pkg{version},
	)
}
