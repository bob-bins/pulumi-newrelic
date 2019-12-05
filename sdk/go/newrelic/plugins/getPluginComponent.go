// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package plugins

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get information about a single plugin component in New Relic.
// 
// Each plugin component reporting into to New Relic is assigned a unique ID. Once you have a plugin component reporting data into your account, its component ID can be used to create Plugins Alert Conditions.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/d/plugin_component.html.markdown.
func LookupPluginComponent(ctx *pulumi.Context, args *GetPluginComponentArgs) (*GetPluginComponentResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
		inputs["pluginId"] = args.PluginId
	}
	outputs, err := ctx.Invoke("newrelic:plugins/getPluginComponent:getPluginComponent", inputs)
	if err != nil {
		return nil, err
	}
	return &GetPluginComponentResult{
		HealthStatus: outputs["healthStatus"],
		Id: outputs["id"],
		Name: outputs["name"],
		PluginId: outputs["pluginId"],
	}, nil
}

// A collection of arguments for invoking getPluginComponent.
type GetPluginComponentArgs struct {
	// The name of the plugin component.
	Name interface{}
	// The ID of the plugin instance this component belongs to.
	PluginId interface{}
}

// A collection of values returned by getPluginComponent.
type GetPluginComponentResult struct {
	// The health status of the plugin component.
	HealthStatus interface{}
	// The ID of the plugin component.
	Id interface{}
	Name interface{}
	PluginId interface{}
}